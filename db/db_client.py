import sqlite3
from typing import List

from config import DATA_BASE_PATH


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=MetaSingleton):
    def __init__(self):
        super().__init__()
        self.connection = None
        self.cursor_obj = None

    def connect(self) -> None:
        if self.connection is None:
            self.connection = sqlite3.connect(DATA_BASE_PATH)
            self.cursor_obj = self.connection.cursor()

    def get_all_signature(self) -> List[bytes]:
        db_signature = []
        result = self.cursor_obj.execute("SELECT `signature` FROM `usb_data`")
        for sign in result.fetchall():
            db_signature.append(sign[0])
        return db_signature
