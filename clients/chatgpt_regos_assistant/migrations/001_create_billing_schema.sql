-- Billing schema for REGOS Assistant.
CREATE TABLE IF NOT EXISTS `chatgpt_regos_assistant_tariff` (
    `code` VARCHAR(64) NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `free_requests_per_day` INT UNSIGNED NOT NULL DEFAULT 0,
    `billable_request_price` DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
    `currency` CHAR(3) NOT NULL DEFAULT 'UZS',
    `is_default` TINYINT(1) NOT NULL DEFAULT 0,
    `is_active` TINYINT(1) NOT NULL DEFAULT 1,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`code`),
    KEY `idx_cra_tariff_default` (`is_default`, `is_active`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `chatgpt_regos_assistant_tariff`
    (`code`, `name`, `free_requests_per_day`, `billable_request_price`, `currency`, `is_default`, `is_active`)
VALUES
    ('default', 'REGOS Assistant Default', 20, 0.0000, 'UZS', 1, 1)
ON DUPLICATE KEY UPDATE `code` = `code`;

CREATE TABLE IF NOT EXISTS `chatgpt_regos_assistant_usage_daily` (
    `usage_date` DATE NOT NULL,
    `api_login` VARCHAR(128) NOT NULL,
    `connected_integration_id` VARCHAR(128) NOT NULL,
    `tariff_code` VARCHAR(64) NOT NULL DEFAULT 'default',
    `free_limit` INT UNSIGNED NOT NULL DEFAULT 0,
    `request_count` INT UNSIGNED NOT NULL DEFAULT 0,
    `free_request_count` INT UNSIGNED NOT NULL DEFAULT 0,
    `billable_request_count` INT UNSIGNED NOT NULL DEFAULT 0,
    `input_tokens` BIGINT UNSIGNED NOT NULL DEFAULT 0,
    `output_tokens` BIGINT UNSIGNED NOT NULL DEFAULT 0,
    `total_tokens` BIGINT UNSIGNED NOT NULL DEFAULT 0,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`usage_date`, `api_login`),
    KEY `idx_cra_usage_daily_ci` (`connected_integration_id`),
    KEY `idx_cra_usage_daily_tariff` (`tariff_code`),
    KEY `idx_cra_usage_daily_date` (`usage_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `chatgpt_regos_assistant_usage_log` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `usage_date` DATE NOT NULL,
    `api_login` VARCHAR(128) NOT NULL,
    `connected_integration_id` VARCHAR(128) NOT NULL,
    `tariff_code` VARCHAR(64) NOT NULL DEFAULT 'default',
    `model` VARCHAR(64) NOT NULL,
    `status` VARCHAR(64) NOT NULL,
    `request_number` INT UNSIGNED NOT NULL DEFAULT 0,
    `free_limit` INT UNSIGNED NOT NULL DEFAULT 0,
    `billable` TINYINT(1) NOT NULL DEFAULT 0,
    `billable_request_price` DECIMAL(18,4) NOT NULL DEFAULT 0.0000,
    `currency` CHAR(3) NOT NULL DEFAULT 'UZS',
    `response_id` VARCHAR(128) NOT NULL DEFAULT '',
    `input_tokens` BIGINT UNSIGNED NOT NULL DEFAULT 0,
    `output_tokens` BIGINT UNSIGNED NOT NULL DEFAULT 0,
    `total_tokens` BIGINT UNSIGNED NOT NULL DEFAULT 0,
    `tool_call_count` INT UNSIGNED NOT NULL DEFAULT 0,
    `error_code` VARCHAR(128) NOT NULL DEFAULT '',
    `error_description` VARCHAR(512) NOT NULL DEFAULT '',
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `completed_at` TIMESTAMP NULL DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `idx_cra_usage_log_account_date` (`api_login`, `usage_date`),
    KEY `idx_cra_usage_log_ci` (`connected_integration_id`),
    KEY `idx_cra_usage_log_tariff` (`tariff_code`),
    KEY `idx_cra_usage_log_billable` (`billable`, `usage_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
