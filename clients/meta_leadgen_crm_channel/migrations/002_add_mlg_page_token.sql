-- Keep Meta Page authorization durable for webhook processing when service settings
-- are temporarily unavailable through ConnectedIntegrationSetting/Get.
ALTER TABLE `mlg_page_map`
    ADD COLUMN IF NOT EXISTS `page_access_token` TEXT NULL AFTER `page_name`,
    ADD COLUMN IF NOT EXISTS `access_token_expires_at` BIGINT NULL AFTER `page_access_token`;
