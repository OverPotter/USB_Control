from time import sleep

from config import USB_DRIVE_TYPE, USB_MEDIA_TYPE, WINDOWS_MANAGER, USB_HUB, TIME_BETWEEN_CHECK
from utils.logger import Logger
from utils.usb_utils import UsbLockerUtils
from utils.crypto import Crypto
from db.db_client import DataBase

import win32com.client


class UsbLocker(UsbLockerUtils, Crypto, DataBase, Logger):
    def __init__(self):
        super().__init__()
        self.usb_diskName_list = []
        self.PNP_list = []

        self.signature_list = []
        self.signature_dict = {}

        self.db_signature = None

        self.access_list = set()

    def set_db_signature(self):
        db = DataBase()
        db.connect()
        self.db_signature = db.get_all_signature()

    def search_usb_type(self) -> bool:
        for disk in self.disk_info_WMI.Win32_LogicalDisk():
            if disk.DriveType == USB_DRIVE_TYPE:
                self.usb_diskName_list.append(disk.DeviceID)

        if not self.usb_diskName_list:
            return False
        else:
            return self.check_disk(self.usb_diskName_list)

    def create_PNPDeviceID_list(self) -> None:
        for drive in self.disk_info_WMI.Win32_DiskDrive():
            if drive.MediaType == USB_MEDIA_TYPE:
                self.PNP_list.append(drive.PNPDeviceID.split('\\')[-1])

    def create_signature_list(self) -> None:
        usb_WMI = win32com.client.GetObject(WINDOWS_MANAGER)
        for usb in usb_WMI.InstancesOf(USB_HUB):
            try:
                for PNP in self.PNP_list:
                    if usb.DeviceID.split('\\')[2] in PNP:
                        VID, PID = self.create_PID_VID_list(usb.DeviceID)
                        signature = self.get_signature(VID + PID + PNP)
                        self.signature_list.append(signature)
                        self.log(VID, PID, PNP, signature)
            except Exception:
                pass

    def create_sign_dict(self) -> None:
        self.signature_dict = dict(zip(self.signature_list, self.usb_diskName_list))
        self.usb_diskName_list = []

    def compare_signature(self) -> None:
        try:
            for usb_sign in self.db_signature:
                for sign in self.signature_dict.keys():
                    if usb_sign == str(sign):
                        if str(sign) in self.access_list:
                            continue
                        else:
                            self.unlock_notice()
                            self.access_list.add(str(sign))
                    else:
                        self.edit_core(self.signature_dict[sign])
                        self.eject_usb()
                        self.signature_dict.pop(sign)
                        self.lock_notice()
        except RuntimeError:
            pass

    def run_usb_locker(self) -> None:
        try:
            if self.search_usb_type():
                self.set_db_signature()
                self.create_PNPDeviceID_list()
                self.create_signature_list()
                self.create_sign_dict()
                self.compare_signature()
                sleep(TIME_BETWEEN_CHECK)
                self.run_usb_locker()
            else:
                sleep(TIME_BETWEEN_CHECK)
                self.run_usb_locker()
        except Exception as e:
            self.error_notice(str(e))
            raise Exception(str(e))


if __name__ == '__main__':
    u = UsbLocker()
    u.run_usb_locker()
    # u.search_usb_type()
    # u.set_db_signature()
    # u.create_PNPDeviceID_list()
    # u.create_signature_list()
    # u.create_sign_dict()
    # u.compare_signature()
