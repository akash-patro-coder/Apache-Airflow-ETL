from airflow.hooks.base import BaseHook
from sqlalchemy import create_engine

class CustomSqliteHook(BaseHook):

    def __init__(self, conn_id):
        self.conn_id = conn_id

    def get_conn(self):
        conn = self.get_connection(self.conn_id)
        return create_engine(f"sqlite:///{conn.host}")