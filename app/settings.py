from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    
    APP_NAME: str
    YOUTUBE_URL: str
    GITHUB_URL: str
    COPYRIGHT_URL: str
    COPYRIGHT_MESSAGE: str

    SECRET_KEY: str
    SQLALCHEMY_DATABASE_URI: str

    IMAGES_PER_PAGE_COUNT: int

    ADMIN_NAME: str
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str

    CLOUDINARY_NAME: str
    CLOUDINARY_KEY: str
    CLOUDINARY_SECRET: str
    CLOUDINARY_FOLDER: str
