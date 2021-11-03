import sys
import platform
import os

if platform.system() == "Windows":
    from win32com.client import Dispatch
import getpass


def become_persistent(filename):
    if platform.system() == "Windows":
        USER_NAME = getpass.getuser()
        path = (
            r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
            % USER_NAME
        )
        path = os.path.join(path, "ItemStockTracker.lnk")
        wDir = os.path.dirname(sys.executable)
        target = wDir + "\\ItemStockTracker.exe"
        icon = target
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()


def remove_startup():
    USER_NAME = getpass.getuser()
    path = (
        r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
        % USER_NAME
    )
    path = os.path.join(path, "ItemStockTracker.lnk")
    if os.path.exists(path):
        os.remove(path)
