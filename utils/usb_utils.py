from config import SCRIPT_PATH, DISK_PATTERN

import subprocess
import os
import wmi

from utils.notif import Notice


class UsbLockerUtils(Notice):
    def __init__(self):
        super().__init__()
        self.disk_info_WMI = wmi.WMI()

    @staticmethod
    def check_disk(disk_list: list) -> bool:
        """
        CRUTCH
        """
        for disk in disk_list:
            if os.system(f'dir {disk}') != 0:
                return False
            else:
                return True

    @staticmethod
    def create_PID_VID_list(device_id: str) -> tuple[str, str]:
        PID_VID = device_id.split('\\')[1].split('&')
        VID = PID_VID[0].replace("VID_", "")
        PID = PID_VID[1].replace("PID_", "")
        return VID, PID

    def edit_core(self, disk_name: str) -> None:
        with open(SCRIPT_PATH, 'r') as f:
            old_script = f.read()

        match = DISK_PATTERN.findall(old_script)
        if not match:
            self.error_notice("Check core script(.bat). Disk not found.")
            raise Exception("Check core script. Disk not found.")

        if disk_name != match[0].replace('("', '').replace('")', ''):
            new_script = DISK_PATTERN.sub(f'("{disk_name}")', old_script)

            with open(SCRIPT_PATH, 'w') as f:
                f.write(new_script)

    @staticmethod
    def eject_usb() -> None:
        subprocess.call(SCRIPT_PATH, shell=True)
