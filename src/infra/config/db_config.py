from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConectionHandler:
    """sqlalchemy database connection"""

    def __init__(self):
        self.__conection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """
        return connection Engine
        :param - none
        :return - engine connection to database

        """
        engine = create_engine(self.__conection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__conection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
