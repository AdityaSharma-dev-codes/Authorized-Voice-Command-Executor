import os

def exec_command(text):
    if "browser" in text:
        os.system("librewolf")

    elif "terminal" in text:
        os.system("kitty")

    elif "close" in text:
        os.system("xdotool getwindowfocus windowkill")

    elif "shutdown" in text or "shut down" in text:
        os.system("shutdown now")

    elif "restart" in text or " reboot" in text:
        os.system("reboot")