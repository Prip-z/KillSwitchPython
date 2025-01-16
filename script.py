import ctypes
import os
import signal
from ctypes import wintypes
import keyboard

def kill():
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    # Определяем прототипы функций
    user32.GetForegroundWindow.restype = wintypes.HWND
    user32.GetWindowThreadProcessId.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
    user32.GetWindowThreadProcessId.restype = wintypes.DWORD

    def get_active_window_pid():
        hwnd = user32.GetForegroundWindow()
        if hwnd == 0:
            return None

        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        return pid.value

    active_pid = get_active_window_pid()
    os.kill(active_pid,signal.SIGTERM)

keyboard.add_hotkey('ctrl+alt+p',kill)
keyboard.wait('esc+p')