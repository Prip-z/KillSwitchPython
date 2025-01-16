# KillSwitchPython

## Description
**KillSwitchPython** is a tool designed to quickly terminate active processes on Windows. This script helps users close unresponsive applications (especially in fullscreen mode) that cannot be closed using standard methods.

## Features
- Terminates the process associated with the active window.
- Quick execution via global hotkey.
- Minimizes distracting windows upon launch.

## Usage

### Running the Script
To run the script, execute:
```bash
python script.py
```

### Hotkeys
- Press `Ctrl+Alt+P` to terminate the active window's process.
- Press `Esc+P` to exit the script.
- If needed, customize the hotkeys to your preference.

### Packing into an Executable File
To create a standalone `.exe` file, run:
```bash
pyinstaller --onefile --noconsole --strip script.py
```

## Technical Details
The script uses:
- `ctypes` to interact with the Windows API (retrieve active window and PID).
- `keyboard` for global hotkey interception.

## Code

```python
import ctypes
import os
import signal
from ctypes import wintypes
import keyboard

def kill():
    user32 = ctypes.WinDLL('user32', use_last_error=True)

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
```

## License
The project is distributed under the MIT License.

