import os

from datetime import datetime
from config import LOGGER_BASE_PATH


class Logger:
    def __init__(self):
        super().__init__()

    @staticmethod
    def log(*args) -> None:
        time_create = str(datetime.timestamp(datetime.now()) * 1000000)[:-1]
        log_str = f"USB CONNECT INFO:\n" \
                  f"VID: {args[0]}\n" \
                  f"PID: {args[1]}\n" \
                  f"PNP: {args[2]}\n" \
                  f"SIGN: {args[3]}\n" \
                  f"DATE: {datetime.now()}"
        if len(args) == 4:
            with open(os.path.join(LOGGER_BASE_PATH, time_create), "w") as log:
                log.writelines(log_str)
        else:
            raise Exception(f"A lot of args {args}")
