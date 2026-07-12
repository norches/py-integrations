# AI-ассистент REGOS

Integration key: `chatgpt_regos_assistant`

## Наименование интеграции

| Язык | Наименование |
| --- | --- |
| RU | AI-ассистент REGOS |
| UZ | REGOS AI yordamchisi |
| EN | REGOS AI Assistant |

## Краткое описание

| Язык | Описание |
| --- | --- |
| RU | AI-чат внутри REGOS: сотрудник пишет задачу обычными словами, ассистент ищет данные и выполняет действия через REGOS API только после подтверждения. |
| UZ | REGOS ichidagi AI-chat: xodim vazifani oddiy so'zlar bilan yozadi, yordamchi ma'lumot topadi va REGOS API orqali amallarni faqat tasdiqdan keyin bajaradi. |
| EN | An AI chat inside REGOS: a teammate writes a task in plain language, the assistant finds data and performs REGOS API actions only after confirmation. |

## Полное описание

| Язык | Описание |
| --- | --- |
| RU | AI-ассистент открывается прямо внутри REGOS во встроенном окне. Пользователь авторизуется через REGOS Embed SDK, поэтому все REGOS API действия выполняются от имени сотрудника, который открыл чат. Ассистент помогает искать товары, проверять остатки, смотреть складские документы, работать с клиентами, сделками, тикетами и чатами. Чтение выполняется сразу, а создание, изменение, проведение, закрытие или удаление всегда требуют явного подтверждения. |
| UZ | AI yordamchi REGOS ichida o'rnatilgan oynada ochiladi. Foydalanuvchi REGOS Embed SDK orqali avtorizatsiyadan o'tadi, shuning uchun REGOS API amallari chatni ochgan xodim nomidan bajariladi. Yordamchi tovarlarni qidirish, qoldiqlarni tekshirish, ombor hujjatlari, mijozlar, bitimlar, tiketlar va chatlar bilan ishlashga yordam beradi. O'qish amallari darhol bajariladi, yaratish, o'zgartirish, o'tkazish, yopish yoki o'chirish esa aniq tasdiqdan keyin bajariladi. |
| EN | The AI assistant opens inside REGOS as an embedded chat. The user is authorized through the REGOS Embed SDK, so REGOS API actions run on behalf of the teammate who opened the chat. The assistant helps search items, check stock, view warehouse documents, and work with clients, deals, tickets, and chats. Read-only requests run immediately, while create, update, perform, close, or delete actions always require explicit confirmation. |

## Список обрабатываемых вебхуков

Интеграция не подписывается на входящие REGOS-вебхуки и не создает подписки автоматически.

| Событие | Используется | Описание |
| --- | --- | --- |
| REGOS webhook | Нет | Входящие CRM/складские вебхуки не обрабатываются. |
| REGOS embed token | Да | UI получает `embed_token` через REGOS Embed SDK и передает его на backend для создания пользовательской сессии. |

## Какие действия выполняются автоматически

| Действие | Когда выполняется |
| --- | --- |
| Открытие UI | При переходе на `/external/{connected_integration_id}/ui`. |
| Авторизация пользователя | UI получает `embed_token` через REGOS Embed SDK, backend обменивает его на пользовательский REGOS access token. |
| Получение аккаунта | Перед обращением к OpenAI backend вызывает `Sys/GetInfo` и берет `result.api_login` для учета. |
| Обработка сообщения | UI отправляет текст пользователя в действие `chat`, backend вызывает OpenAI Responses API и подбирает нужные REGOS-инструменты. |
| Учет запроса | Запрос резервируется в MariaDB по `api_login`; дневной лимит и цена берутся из активного тарифа в БД. |
| Чтение данных REGOS | Запросы на поиск, получение списков, карточек, остатков и документов выполняются без дополнительного подтверждения. |
| Подготовка изменения | Для создания, редактирования, проведения, закрытия или удаления создается pending confirmation с ограниченным TTL. |
| Выполнение изменения | Выполняется только после подтверждения пользователем через `confirm_action`. |

## Возможности ассистента

| Направление | Доступные операции |
| --- | --- |
| Товары и справочники | Поиск и получение товаров, групп, штрихкодов, цен, складов, брендов, единиц измерения и типов цен; создание и изменение товаров, групп, штрихкодов и складов после подтверждения. |
| Остатки и склад | Получение остатков, текущего количества и складских операций по товарам. |
| Складские документы | Работа с инвентаризацией, перемещениями, приходом/списанием, закупками, оптовыми продажами и агрегацией остатков. |
| CRM | Получение, создание и изменение клиентов, сделок и тикетов; смена стадий и статусов; закрытие и удаление после подтверждения. |
| Чаты | Получение чатов и сообщений, отправка сообщения после подтверждения. |

## Настройки интеграции

У подключенной интеграции нет пользовательских OpenAI-настроек. Пользователь ничего не вводит вручную: REGOS Assistant работает только через серверный ключ, а лимиты и тарифы берутся из БД.

## Глобальные настройки сервиса

Эти параметры задаются на уровне backend-сервиса. Они общие для всех подключений интеграции.

| Ключ | Обяз. | Описание |
| --- | --- | --- |
| `oauth_endpoint` | Да | Базовый URL REGOS OAuth. Backend вызывает `{oauth_endpoint}/oauth/token`. |
| `oauth_client_id` | Да | OAuth client id приложения, зарегистрированного для работы с REGOS embed token. |
| `oauth_secret` | Да | OAuth secret приложения. |
| `integration_url` | Да | Публичный HTTPS URL сервиса интеграций, с которого открывается iframe UI. Используется для построения `/external/{connected_integration_id}/...`; `proxy_integration_url` не должен подменять origin для Embed OAuth. |
| `CHATGPT_REGOS_OPENAI_API_KEY` | Да | Серверный OpenAI API key. Пользователи не видят этот ключ и не могут заменить его в настройках подключения. |
| `CHATGPT_REGOS_OPENAI_MODEL` | Нет | Модель для ответов ассистента. По умолчанию `gpt-4.1-mini`. |
| `CHATGPT_REGOS_TEMPERATURE` | Нет | Вариативность ответов. Диапазон `0`-`2`, по умолчанию `0.2`. |
| `CHATGPT_REGOS_MAX_TOOL_ROUNDS` | Нет | Максимальное число последовательных обращений к REGOS API в одном сообщении. По умолчанию `5`. |
| `CHATGPT_REGOS_MAX_OUTPUT_TOKENS` | Нет | Максимальный размер финального ответа модели. По умолчанию `1200`. |
| `CHATGPT_REGOS_CONFIRMATION_TTL_SEC` | Нет | Сколько секунд pending confirmation остается доступным. По умолчанию `900`. |
| `CHATGPT_REGOS_PARENT_ORIGIN` | Нет | Origin родительского окна REGOS для Embed SDK. По умолчанию `https://regos.online`. |

## Биллинг и лимиты

Все запросы идут через серверный `CHATGPT_REGOS_OPENAI_API_KEY`. Перед обращением к OpenAI backend вызывает `Sys/GetInfo`, получает `api_login` текущего REGOS-аккаунта и резервирует запрос в БД. Дневной бесплатный лимит и цена платного запроса берутся из активного тарифа в `chatgpt_regos_assistant_tariff`.

Таблицы MariaDB:

| Таблица | Назначение |
| --- | --- |
| `chatgpt_regos_assistant_tariff` | Тарифы ассистента: код, дневной бесплатный лимит, цена платного запроса, валюта и флаг активного тарифа по умолчанию. |
| `chatgpt_regos_assistant_usage_daily` | Дневной агрегат по `usage_date` и `api_login`: количество запросов, бесплатные и платные запросы, токены. |
| `chatgpt_regos_assistant_usage_log` | Подробный лог каждого запроса: тариф, лимит на момент запроса, модель, статус, response id, токены, ошибки. |

Миграция создает дефолтный тариф `default`: 20 бесплатных запросов в день и цену `0.0000 UZS` для платных запросов. Реальные цены и лимиты меняются в БД без изменения настроек подключенной интеграции. Оплаты подключаются отдельным платежным слоем поверх `billable_request_count`: текущая интеграция уже готовит корректную базу для начислений по `api_login`.

## Порядок настройки

1. Зарегистрировать OAuth-приложение для REGOS embed token и заполнить `oauth_endpoint`, `oauth_client_id`, `oauth_secret`.
2. Убедиться, что backend интеграций доступен по публичному HTTPS URL и он указан в `integration_url`; этот origin должен совпадать с адресом, с которого REGOS открывает iframe.
3. Заполнить `CHATGPT_REGOS_OPENAI_API_KEY` на backend-сервисе.
4. Применить миграцию ассистента и при необходимости изменить дефолтный тариф в `chatgpt_regos_assistant_tariff`.
5. Создать подключение интеграции `chatgpt_regos_assistant` в REGOS.
6. Открыть `/external/{connected_integration_id}/ui` во фрейме REGOS.
7. Проверить вход пользователя через REGOS Embed SDK: после успешного входа поле ввода чата становится активным.
8. Отправить тестовый запрос на чтение, например "Покажи остатки товара X".
9. Проверить изменение с подтверждением, например "Создай товар X": ассистент должен показать действие и выполнить его только после подтверждения.

## Внешние endpoint-ы

| Endpoint / action | Назначение |
| --- | --- |
| `GET /external/{connected_integration_id}/ui` | Полноценный iframe UI чата. |
| `POST /external/{connected_integration_id}/embed/consume` | Принимает `embed_token` от REGOS Embed SDK и возвращает `embed_session_token`. |
| `metadata` / `info` | Возвращает информацию об интеграции, URL, SDK и доступных действиях. |
| `list_tools` / `tools` | Возвращает список REGOS-инструментов ассистента. |
| `chat` | Обрабатывает сообщение пользователя через OpenAI Responses API и REGOS tools. |
| `execute_tool` / `execute` | Выполняет конкретный REGOS-инструмент. Мутации возвращают pending confirmation. |
| `confirm_action` / `confirm` | Подтверждает или отклоняет pending confirmation. |

## Политика подтверждений

Чтение данных выполняется без подтверждения. Любое действие, которое может изменить данные REGOS, требует явного подтверждения пользователя: создание, редактирование, удаление, пометка на удаление, проведение, отмена проведения, закрытие, открытие, смена стадии или статуса, отправка сообщения.

Pending confirmation привязан к `connected_integration_id`, конкретной пользовательской embed-сессии и имеет ограниченный срок жизни. Если срок истек или пользователь открыл другую сессию, действие нужно сформировать заново.

## Техническая логика

1. UI загружает REGOS Embed SDK и вызывает авторизацию для текущего `connected_integration_id`.
2. Backend проверяет `connected_integration_id`, `origin` и обменивает `embed_token` через REGOS OAuth grant type `embed_token`.
3. Пользовательский REGOS access token хранится только на backend в короткоживущей embed-сессии.
4. UI отправляет в `chat` только локальный `embed_session_token`.
5. Backend вызывает `Sys/GetInfo`, получает `api_login` текущего аккаунта, выбирает активный тариф и резервирует usage-запись в MariaDB.
6. Backend вызывает OpenAI Responses API через серверный `CHATGPT_REGOS_OPENAI_API_KEY`.
7. Backend вызывает REGOS API от имени пользователя, выбрав релевантные tools для сообщения.
8. Для мутаций backend сначала возвращает подтверждение, а после `confirm_action` выполняет исходный REGOS API вызов.
9. После ответа OpenAI backend записывает статус, response id и токены в MariaDB.
