from plyer import notification

from config import UNLOCK_ICO_BASE_PATH, LOCK_ICO_BASE_PATH, NOTICE_TIME, ERROR_ICO_BASE_PATH


class Notice:
    def __init__(self):
        super().__init__()

    @staticmethod
    def unlock_notice() -> None:
        notification.notify(
            title="USB Locker",
            message="Access permitted",
            app_icon=UNLOCK_ICO_BASE_PATH,
            timeout=NOTICE_TIME
        )

    @staticmethod
    def lock_notice() -> None:
        notification.notify(
            title="USB Locker",
            message="Permission to connect denied",
            app_icon=LOCK_ICO_BASE_PATH,
            timeout=NOTICE_TIME
        )

    @staticmethod
    def error_notice(data: str) -> None:
        notification.notify(
            title="Error",
            message=data,
            app_icon=ERROR_ICO_BASE_PATH,
            timeout=NOTICE_TIME
        )