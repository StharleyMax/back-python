# pylint: disable=E1101

from src.infra.config import DBConectionHandler
from src.infra.entities import Users


class UserFake:
    """A simple repository"""

    @classmethod
    def insert_use(cls):
        """Something"""

        with DBConectionHandler() as db_connection:
            try:
                new_user = Users(name="programação", password="123")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
