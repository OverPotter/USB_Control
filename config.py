import re
import os
from pathlib import Path

SCRIPT_NAME = "eject.bat"

DATA_BASE_NAME = "usb.db"

UNLOCK_ICO = "usb_unlock.ico"
LOCK_ICO = "usb_lock.ico"
ERROR_ICO = "error.ico"

CORE_DIR = os.path.join(Path(__file__).resolve().parent, "core")
SCRIPT_PATH = os.path.join(CORE_DIR, SCRIPT_NAME)

DATA_BASE_DIR = os.path.join(Path(__file__).resolve().parent, "db")
DATA_BASE_PATH = os.path.join(DATA_BASE_DIR, DATA_BASE_NAME)

LOGGER_PATH = os.path.join("utils", "logging")
LOGGER_BASE_PATH = os.path.join(Path(__file__).resolve().parent, LOGGER_PATH)

ICO_PATH = os.path.join("utils", "icon")
ICO_BASE_DIR = os.path.join(Path(__file__).resolve().parent, ICO_PATH)
UNLOCK_ICO_BASE_PATH = os.path.join(ICO_BASE_DIR, UNLOCK_ICO)
LOCK_ICO_BASE_PATH = os.path.join(ICO_BASE_DIR, LOCK_ICO)
ERROR_ICO_BASE_PATH = os.path.join(ICO_BASE_DIR, ERROR_ICO)

USB_DRIVE_TYPE = 2
USB_MEDIA_TYPE = "Removable Media"

WINDOWS_MANAGER = "WinMgmts:"
USB_HUB = "Win32_USBHub"

DISK_PATTERN = re.compile(r"\(\"[A-Z]:\"\)")

TIME_BETWEEN_CHECK = 5
NOTICE_TIME = 5
