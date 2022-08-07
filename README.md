# USB Control System
Program for checking usb ports for registered and unregistered USB flash drives.
___
![](https://img.shields.io/badge/python-3.9-blueviolet)
![](https://img.shields.io/github/last-commit/OverPotter/RemoteImport?color=blueviolet)
![](https://img.shields.io/github/issues-pr/OverPotter/RemoteImport?color=blueviolet)
![](https://img.shields.io/github/forks/OverPotter/RemoteImport?style=social)
___
## Installation
Use the git to install remote import.
```bash
git clone https://github.com/OverPotter/usb_control.git
```
___
## Usage
То add usb flash drive to the access list, you need to add PNP, PID and VID flash drives to the database. After that, the signature of the flash drive will be found.

After that u can run main.py

If you insert an unregistered flash drive, you will see a notification

![](https://github.com/OverPotter/usb_control/blob/master/utils/img/usb_lock.PNG "USB Lock")

When you insert a registered flash drive, you will see a notification

![](https://github.com/OverPotter/usb_control/blob/master/utils/img/usb_unlock.PNG "USB Unlock")

In case of errors, you will see a notification

![](https://github.com/OverPotter/usb_control/blob/master/utils/img/error.PNG "Error")


___
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
___ 
## License
[MIT](https://choosealicense.com/licenses/mit/)