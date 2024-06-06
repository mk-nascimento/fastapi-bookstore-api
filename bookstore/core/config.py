from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_ignore_empty=True, env_file='.env')

    PGPASSWORD: str
    PGUSER: str
    PGDB: str
    PGHOST: str
    PGPORT: str

    @property
    def DATABASE_URI(self) -> 'str':
        return MultiHostUrl.build(
            scheme='postgresql+psycopg2',
            username=self.PGUSER,
            password=self.PGPASSWORD,
            host=self.PGHOST,
            port=int(self.PGPORT),
            path=self.PGDB,
        ).unicode_string()
