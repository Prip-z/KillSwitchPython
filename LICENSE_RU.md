# KillSwitchPython

## Описание
**KillSwitchPython** — это инструмент для быстрого завершения активных процессов на Windows. Этот скрипт создан, чтобы помочь пользователям завершать застрявшие приложения (особенно в полноэкранном режиме), которые не отвечают стандартным способам завершения.

## Возможности
- Завершает процесс, связанный с активным окном.
- Быстрая работа через глобальное горячее сочетание клавиш.
- Минимизация отвлекающих окон при запуске.

## Использование

### Запуск скрипта
Для запуска скрипта выполните:
```bash
python script.py
```

### Горячие клавиши
- Нажмите `Ctrl+Alt+P`, чтобы завершить процесс активного окна.
- Нажмите `Esc+p`, чтобы выйти из скрипта.
- При необходимости, измените горячие клавиши на свои.

### Упаковка в исполняемый файл
Чтобы создать автономный `.exe`, выполните:
```bash
pyinstaller --onefile --noconsole --strip script.py
```

## Технические детали
Скрипт использует:
- `ctypes` для взаимодействия с Windows API (получение активного окна и PID).
- `keyboard` для глобального перехвата горячих клавиш.

##Код

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

## Лицензия
Проект распространяется под лицензией MIT. 


