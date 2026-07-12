from __future__ import annotations

import asyncio
import json
import time
from typing import Any, Dict, Optional, Tuple

from core.redis import redis_is_enabled, redis_make_key, redis_ops

from .config import ChatGptRegosAssistantConfig
from .models import json_dumps


_LOCAL_PENDING: Dict[str, Tuple[float, Dict[str, Any]]] = {}
_LOCAL_PENDING_LOCK = asyncio.Lock()
_LOCAL_SESSIONS: Dict[str, Tuple[float, Dict[str, Any]]] = {}
_LOCAL_SESSIONS_LOCK = asyncio.Lock()


class ChatGptRegosAssistantRedisState:
    @staticmethod
    def redis_key(*parts: Any) -> str:
        return redis_make_key("integration", ChatGptRegosAssistantConfig.INTEGRATION_KEY, *parts)

    @classmethod
    def confirmation_key(cls, connected_integration_id: str, confirmation_id: str) -> str:
        return cls.redis_key("confirm", connected_integration_id, confirmation_id)

    @classmethod
    def embed_session_key(cls, connected_integration_id: str, session_token: str) -> str:
        return cls.redis_key("embed", "session", connected_integration_id, session_token)

    @classmethod
    async def get(cls, key: str) -> Optional[str]:
        if not redis_is_enabled():
            return None
        return await redis_ops.get(key)

    @classmethod
    async def set(cls, key: str, value: str, ttl_sec: int) -> None:
        if redis_is_enabled():
            await redis_ops.set(key, value, ex=max(int(ttl_sec), 1))

    @classmethod
    async def delete(cls, *keys: str) -> None:
        valid = [key for key in keys if key]
        if valid and redis_is_enabled():
            await redis_ops.delete(*valid)

    @classmethod
    async def store_pending(
        cls,
        connected_integration_id: str,
        confirmation_id: str,
        payload: Dict[str, Any],
        ttl_sec: int,
    ) -> None:
        key = cls.confirmation_key(connected_integration_id, confirmation_id)
        raw = json_dumps(payload)
        if redis_is_enabled():
            await redis_ops.set(key, raw, ex=max(int(ttl_sec), 1))
            return

        now = time.monotonic()
        async with _LOCAL_PENDING_LOCK:
            for local_key, (expires_at, _) in list(_LOCAL_PENDING.items()):
                if expires_at <= now:
                    _LOCAL_PENDING.pop(local_key, None)
            _LOCAL_PENDING[key] = (now + max(int(ttl_sec), 1), payload)

    @classmethod
    async def pop_pending(
        cls, connected_integration_id: str, confirmation_id: str
    ) -> Optional[Dict[str, Any]]:
        key = cls.confirmation_key(connected_integration_id, confirmation_id)
        if redis_is_enabled():
            raw = await redis_ops.get(key)
            if raw:
                await redis_ops.delete(key)
                try:
                    payload = json.loads(raw)
                    return payload if isinstance(payload, dict) else None
                except Exception:
                    return None
            return None

        now = time.monotonic()
        async with _LOCAL_PENDING_LOCK:
            stored = _LOCAL_PENDING.pop(key, None)
            if not stored:
                return None
            expires_at, payload = stored
            if expires_at <= now:
                return None
            return payload

    @classmethod
    async def store_session_payload(
        cls, key: str, payload: Dict[str, Any], ttl_sec: int
    ) -> None:
        raw = json_dumps(payload)
        if redis_is_enabled():
            await redis_ops.set(key, raw, ex=max(int(ttl_sec), 1))
            return

        now = time.monotonic()
        async with _LOCAL_SESSIONS_LOCK:
            for local_key, (expires_at, _) in list(_LOCAL_SESSIONS.items()):
                if expires_at <= now:
                    _LOCAL_SESSIONS.pop(local_key, None)
            _LOCAL_SESSIONS[key] = (now + max(int(ttl_sec), 1), payload)

    @classmethod
    async def get_session_payload(cls, key: str) -> Optional[Dict[str, Any]]:
        if redis_is_enabled():
            raw = await redis_ops.get(key)
            if not raw:
                return None
            try:
                payload = json.loads(raw)
                return payload if isinstance(payload, dict) else None
            except Exception:
                return None

        now = time.monotonic()
        async with _LOCAL_SESSIONS_LOCK:
            stored = _LOCAL_SESSIONS.get(key)
            if not stored:
                return None
            expires_at, payload = stored
            if expires_at <= now:
                _LOCAL_SESSIONS.pop(key, None)
                return None
            return payload

    @classmethod
    async def store_embed_session(
        cls,
        connected_integration_id: str,
        session_token: str,
        payload: Dict[str, Any],
        ttl_sec: int,
    ) -> None:
        await cls.store_session_payload(
            cls.embed_session_key(connected_integration_id, session_token),
            payload,
            ttl_sec,
        )

    @classmethod
    async def get_embed_session(
        cls, connected_integration_id: str, session_token: str
    ) -> Optional[Dict[str, Any]]:
        return await cls.get_session_payload(
            cls.embed_session_key(connected_integration_id, session_token)
        )
