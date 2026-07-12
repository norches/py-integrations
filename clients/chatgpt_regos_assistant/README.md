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
| RU | AI-чат внутри REGOS: сотрудник задает задачу обычным языком, ассистент ищет данные, готовит ответы и выполняет действия через REGOS API только после подтверждения. |
| UZ | REGOS ichidagi AI-chat: xodim oddiy tilda vazifa beradi, yordamchi ma'lumot topadi, javob tayyorlaydi va REGOS API orqali amallarni faqat tasdiqdan keyin bajaradi. |
| EN | An AI chat inside REGOS: a teammate asks in natural language, the assistant finds data, prepares answers, and runs REGOS API actions only after confirmation. |

## Полное описание

| Язык | Описание |
| --- | --- |
| RU | AI-ассистент открывается прямо внутри REGOS во встроенном окне. Пользователь входит через REGOS Embed SDK, поэтому ассистент работает от имени сотрудника, который открыл интеграцию. Он помогает искать товары, проверять остатки, работать со складскими документами, клиентами, сделками, тикетами и чатами. Чтение данных выполняется сразу, а создание, изменение, проведение, закрытие или удаление всегда требуют явного подтверждения в интерфейсе. |
| UZ | AI yordamchi REGOS ichida o'rnatilgan oynada ochiladi. Foydalanuvchi REGOS Embed SDK orqali kiradi, shuning uchun yordamchi integratsiyani ochgan xodim nomidan ishlaydi. U tovarlarni qidirish, qoldiqlarni tekshirish, ombor hujjatlari, mijozlar, bitimlar, tiketlar va chatlar bilan ishlashga yordam beradi. Ma'lumot o'qish darhol bajariladi, yaratish, o'zgartirish, o'tkazish, yopish yoki o'chirish esa interfeysda aniq tasdiqdan keyin bajariladi. |
| EN | The AI assistant opens inside REGOS as an embedded chat. The user signs in through the REGOS Embed SDK, so the assistant works on behalf of the teammate who opened the integration. It helps search items, check balances, manage warehouse documents, clients, deals, tickets, and chats. Read-only requests run immediately, while create, update, perform, close, or delete actions always require explicit confirmation in the UI. |

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
| Авторизация пользователя | UI получает `embed_token` через REGOS Embed SDK и backend обменивает его на пользовательский REGOS access token. |
| Обработка сообщения | UI отправляет текст пользователя в действие `chat`, backend вызывает OpenAI Responses API и подбирает нужные REGOS-инструменты. |
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

| Ключ | Обяз. | Тип данных | Наименование (RU / UZ / EN) | Описание (RU / UZ / EN) | Placeholder (RU / UZ / EN) |
| --- | --- | --- | --- | --- | --- |
| `chatgpt_connect_url` | Да для UI-входа | String | Вход через ChatGPT / ChatGPT orqali kirish / ChatGPT sign-in | URL внешнего сценария входа через ChatGPT. UI открывает его по кнопке "Войти через ChatGPT" и передает `connected_integration_id` и `return_url`; сценарий должен подключить модель для этой интеграции. / ChatGPT orqali kirish tashqi URL manzili. / External ChatGPT sign-in URL opened by the UI. | `https://.../chatgpt/connect` |
| `chatgpt_openai_api_key` | Да | String | OpenAI API ключ / OpenAI API kaliti / OpenAI API key | Ключ используется backend-сервисом для вызова OpenAI Responses API. Значение не отправляется в браузер. / Kalit OpenAI Responses API chaqiruvi uchun backend servisda ishlatiladi. Brauzerga yuborilmaydi. / Used by the backend service to call the OpenAI Responses API. The value is never sent to the browser. | `sk-...` |
| `chatgpt_openai_model` | Нет | String | Модель OpenAI / OpenAI modeli / OpenAI model | Модель для ответов ассистента. По умолчанию используется `gpt-4.1-mini`. / Yordamchi javoblari uchun model. Standart qiymat `gpt-4.1-mini`. / Model used for assistant responses. Default is `gpt-4.1-mini`. | `gpt-4.1-mini` |
| `chatgpt_assistant_prompt` | Нет | Text | Инструкция ассистента / Yordamchi yo'riqnomasi / Assistant instructions | Дополнительные правила поведения ассистента: тон, ограничения, внутренние регламенты и приоритеты. / Yordamchi xatti-harakati uchun qo'shimcha qoidalar: ohang, cheklovlar, ichki reglamentlar va ustuvorliklar. / Additional behavior rules for the assistant: tone, limits, internal policies, and priorities. | `Отвечай кратко и уточняй данные перед изменениями` |
| `chatgpt_temperature` | Нет | Number | Температура / Harorat / Temperature | Управляет вариативностью ответов. Допустимый диапазон: `0`-`2`, значение по умолчанию `0.2`. / Javoblar o'zgaruvchanligini boshqaradi. Ruxsat etilgan oraliq: `0`-`2`, standart qiymat `0.2`. / Controls response variability. Allowed range: `0`-`2`, default is `0.2`. | `0.2` |
| `chatgpt_max_tool_rounds` | Нет | Integer | Лимит циклов инструментов / Instrument sikllari limiti / Tool round limit | Максимальное количество последовательных обращений ассистента к REGOS API в одном сообщении. Диапазон: `1`-`10`, по умолчанию `5`. / Bitta xabarda REGOS API ga ketma-ket murojaatlar soni. Oraliq: `1`-`10`, standart `5`. / Maximum number of sequential REGOS API tool calls in one assistant turn. Range: `1`-`10`, default is `5`. | `5` |
| `chatgpt_max_output_tokens` | Нет | Integer | Лимит ответа / Javob limiti / Output limit | Максимальный размер финального ответа модели. Диапазон: `256`-`8000`, по умолчанию `1200`. / Model yakuniy javobi hajmi. Oraliq: `256`-`8000`, standart `1200`. / Maximum size of the model's final answer. Range: `256`-`8000`, default is `1200`. | `1200` |
| `chatgpt_confirmation_ttl_sec` | Нет | Integer | Время подтверждения / Tasdiqlash muddati / Confirmation TTL | Сколько секунд pending confirmation остается доступным. Диапазон: `60`-`3600`, по умолчанию `900`. / Pending confirmation necha soniya faol turadi. Oraliq: `60`-`3600`, standart `900`. / How long a pending confirmation remains available. Range: `60`-`3600`, default is `900`. | `900` |
| `chatgpt_regos_parent_origin` | Нет | String | Origin REGOS / REGOS origin / REGOS origin | Origin родительского окна REGOS для Embed SDK. По умолчанию `https://regos.online`. / Embed SDK uchun REGOS ota oynasi origin qiymati. Standart `https://regos.online`. / Parent REGOS window origin for the Embed SDK. Default is `https://regos.online`. | `https://regos.online` |

## Глобальные настройки сервиса

Эти параметры задаются на уровне backend-сервиса и нужны для обмена `embed_token` на пользовательский REGOS access token.

| Ключ | Обяз. | Описание |
| --- | --- | --- |
| `oauth_endpoint` | Да | Базовый URL REGOS OAuth. Backend вызывает `{oauth_endpoint}/oauth/token`. |
| `oauth_client_id` | Да | OAuth client id приложения, зарегистрированного для работы с REGOS embed token. |
| `oauth_secret` | Да | OAuth secret приложения. |
| `integration_url` | Да | Публичный HTTPS URL сервиса интеграций, с которого открывается iframe UI. Используется для построения `/external/{connected_integration_id}/...`; `proxy_integration_url` не должен подменять origin для Embed OAuth. |

## Порядок настройки

1. Зарегистрировать OAuth-приложение для REGOS embed token и заполнить `oauth_endpoint`, `oauth_client_id`, `oauth_secret`.
2. Убедиться, что backend интеграций доступен по публичному HTTPS URL и он указан в `integration_url`; этот origin должен совпадать с адресом, с которого REGOS открывает iframe.
3. Создать подключение интеграции `chatgpt_regos_assistant` в REGOS.
4. Указать `chatgpt_connect_url`, чтобы пользователь мог нажать "Войти через ChatGPT" прямо в UI. После успешного входа внешний сценарий должен заполнить `chatgpt_openai_api_key`; при необходимости также указать модель, prompt и лимиты.
5. Открыть `/external/{connected_integration_id}/ui` во фрейме REGOS.
6. Проверить вход пользователя через REGOS Embed SDK: после успешного входа поле ввода чата становится активным.
7. Отправить тестовый запрос на чтение, например "Покажи остатки товара X".
8. Проверить изменение с подтверждением, например "Создай товар X": ассистент должен показать действие и выполнить его только после подтверждения.

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
5. Backend вызывает REGOS API от имени пользователя, выбрав релевантные tools для сообщения.
6. Для мутаций backend сначала возвращает подтверждение, а после `confirm_action` выполняет исходный REGOS API вызов.
