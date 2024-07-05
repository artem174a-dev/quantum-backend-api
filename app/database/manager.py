from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker, scoped_session, joinedload
from dotenv import load_dotenv
import os

from app.models import Base


class DbManager:
    _instance = None
    _Base = Base

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DbManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        load_dotenv()
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_user = os.getenv('DB_USER')
        db_pass = os.getenv('DB_PASS')
        db_name = os.getenv('DB_NAME')
        db_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
        self.engine = create_engine(db_url, pool_size=5, max_overflow=0)
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)

        self.create_tables()

    def get_base(self):
        return self._Base

    def get_session(self):
        return self.Session()

    def create_tables(self):
        self._Base.metadata.create_all(self.engine)
