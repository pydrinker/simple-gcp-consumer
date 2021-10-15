from prettyconf import config


class Settings:
    LOG_LEVEL = config("LOG_LEVEL", default="INFO")
    SUBSCRIPTION_ID = config("SUBSCRIPTION_ID")
    PROJECT_ID = config("PROJECT_ID")
    GOOGLE_APPLICATION_CREDENTIALS = config("GOOGLE_APPLICATION_CREDENTIALS")
    SUBSCRIPTION_RETRY_TIMEOUT = config("SUBSCRIPTION_RETRY_TIMEOUT", default="300.0", cast=config.eval)
    MAX_MESSAGES_PER_PULL = config("MAX_MESSAGES_PER_PULL", default="1", cast=config.eval)
    SUBSCRIPTION_TIMEOUT = config("SUBSCRIPTION_TIMEOUT", default="None", cast=config.eval)


settings = Settings()
