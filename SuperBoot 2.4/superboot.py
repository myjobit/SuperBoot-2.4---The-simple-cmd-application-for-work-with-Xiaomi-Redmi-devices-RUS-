import os
import sys
import subprocess
import time
import threading
import queue
import re
import shutil
import tempfile
import logging
import json
import hashlib
import base64
import struct


print("""

  █████████                                          ███████████                     █████   
 ███░░░░░███                                        ░░███░░░░░███                   ░░███    
░███    ░░░  █████ ████ ████████   ██████  ████████  ░███    ░███  ██████   ██████  ███████  
░░█████████ ░░███ ░███ ░░███░░███ ███░░███░░███░░███ ░██████████  ███░░███ ███░░███░░░███░   
 ░░░░░░░░███ ░███ ░███  ░███ ░███░███████  ░███ ░░░  ░███░░░░░███░███ ░███░███ ░███  ░███    
 ███    ░███ ░███ ░███  ░███ ░███░███░░░   ░███      ░███    ░███░███ ░███░███ ░███  ░███ ███
░░█████████  ░░████████ ░███████ ░░██████  █████     ███████████ ░░██████ ░░██████   ░░█████ 
 ░░░░░░░░░    ░░░░░░░░  ░███░░░   ░░░░░░  ░░░░░     ░░░░░░░░░░░   ░░░░░░   ░░░░░░     ░░░░░  
                        ░███                                                                 
                        █████                                                                
                       ░░░░░                                                                 2.4
""")

commands = {
    "help": "Show all commands",
    "exit": "Exit the program",
    "clear": "Clear the screen",
    "cls": "Clear the screen",
    "ver": "Version of Superboot",
    "oem": "OEM commands (unlock, lock, etc.)",
    "flash": "Flash partition/image",
    "reboot": "Reboot device (bootloader, recovery, fastboot)",
    "devices": "List connected devices",
    "fastboot": "Execute fastboot command",
    "adb": "Execute adb command"
}
Superboot_version = "2.4"

def execute_fastboot_command(args, silent=False):
    """
    Выполняет fastboot команду
    """
    try:
        cmd = ['fastboot'] + args
        if not silent:
            print(f"[ * ] Выполняется: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=False, text=True, timeout=300)
        if result.returncode != 0 and not silent:
            print(f"[ ! ] Ошибка выполнения команды (код: {result.returncode})")
        return result.returncode == 0
    except FileNotFoundError:
        print("[ ! ] Fastboot не найден в PATH")
        print("[ ! ] Установите Android SDK Platform Tools")
        return False
    except subprocess.TimeoutExpired:
        print("[ ! ] Таймаут выполнения команды")
        return False
    except Exception as e:
        print(f"[ ! ] Ошибка: {e}")
        return False

def execute_adb_command(args, silent=False):
    """
    Выполняет adb команду
    """
    try:
        cmd = ['adb'] + args
        if not silent:
            print(f"[ * ] Выполняется: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=False, text=True, timeout=300)
        if result.returncode != 0 and not silent:
            print(f"[ ! ] Ошибка выполнения команды (код: {result.returncode})")
        return result.returncode == 0
    except FileNotFoundError:
        print("[ ! ] ADB не найден в PATH")
        print("[ ! ] Установите Android SDK Platform Tools")
        return False
    except subprocess.TimeoutExpired:
        print("[ ! ] Таймаут выполнения команды")
        return False
    except Exception as e:
        print(f"[ ! ] Ошибка: {e}")
        return False

def process_superboot_command(cmd_parts):
    """
    Обрабатывает команды superboot (аналог fastboot)
    """
    if len(cmd_parts) == 0:
        print("[ ! ] Недостаточно аргументов")
        return
    
    main_cmd = cmd_parts[0].lower()
    
    if main_cmd == "oem":
        if len(cmd_parts) < 2:
            print("[ ! ] Использование: superboot oem <command>")
            print("     Пример: superboot oem unlock")
            return
        oem_cmd = cmd_parts[1:]
        if execute_fastboot_command(['oem'] + oem_cmd):
            if 'unlock' in oem_cmd:
                print("[ + ] Bootloader разблокирован успешно!")
            elif 'lock' in oem_cmd:
                print("[ + ] Bootloader заблокирован успешно!")
    
    elif main_cmd == "flash":
        if len(cmd_parts) < 3:
            print("[ ! ] Использование: superboot flash <partition> <image>")
            print("     Пример: superboot flash boot boot.img")
            return
        partition = cmd_parts[1]
        image = cmd_parts[2]
        if execute_fastboot_command(['flash', partition, image]):
            print(f"[ + ] Раздел {partition} успешно прошит!")
    
    elif main_cmd == "reboot":
        reboot_target = cmd_parts[1] if len(cmd_parts) > 1 else ""
        if reboot_target:
            execute_fastboot_command(['reboot', reboot_target])
        else:
            execute_fastboot_command(['reboot'])
    
    elif main_cmd == "devices":
        print("[ * ] Поиск подключенных устройств...\n")
        print("[ * ] Fastboot устройства:")
        execute_fastboot_command(['devices', '-l'], silent=True)
        print("\n[ * ] ADB устройства:")
        execute_adb_command(['devices', '-l'], silent=True)
    
    elif main_cmd == "fastboot":
        if len(cmd_parts) < 2:
            print("[ ! ] Использование: superboot fastboot <command> [args...]")
            return
        execute_fastboot_command(cmd_parts[1:])
    
    elif main_cmd == "adb":

        if len(cmd_parts) < 2:
            print("[ ! ] Использование: superboot adb <command> [args...]")
            return
        execute_adb_command(cmd_parts[1:])
    
    else:
        print(f"[ ! ] Неизвестная команда: {main_cmd}")
        print("[ * ] Введите 'help' для списка команд")

def process_command(cmd):
    """
    Обрабатывает команду пользователя
    """
    cmd = cmd.strip()
    
    if not cmd:

        return True
    
    cmd_lower = cmd.lower()
    
    if cmd_lower == "help":
        print("\n[ * ] Доступные команды:")
        for cmd_name, desc in commands.items():
            print(f"     {cmd_name:15} - {desc}")
        print("\n[ * ] Команды Superboot (аналог fastboot):")
        print("     superboot oem unlock          - Разблокировать bootloader")
        print("     superboot oem lock            - Заблокировать bootloader")
        print("     superboot flash boot <img>    - Прошить boot раздел")
        print("     superboot flash recovery <img>- Прошить recovery раздел")
        print("     superboot reboot              - Перезагрузить устройство")
        print("     superboot reboot bootloader   - Перезагрузить в bootloader")
        print("     superboot reboot recovery     - Перезагрузить в recovery")
        print("     superboot devices             - Список подключенных устройств")
        print("     superboot fastboot <cmd>      - Прямой вызов fastboot команды")
        print("     superboot adb <cmd>           - Прямой вызов adb команды")
        print()
    
    elif cmd_lower == "exit":
        print("[ + ] Выход из программы...")
        return False
    
    elif cmd_lower in ["clear", "cls"]:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    elif cmd_lower == "ver":
        print(f"\n[ * ] Superboot версия: {Superboot_version}\n")
    
    elif cmd_lower.startswith("superboot "):

        cmd_parts = cmd.split()[1:]
        process_superboot_command(cmd_parts)
        print()
    
    else:
        print(f"[ ! ] Неизвестная команда: {cmd}")
        print("[ * ] Введите 'help' для списка команд")
        print("[ * ] Используйте 'superboot <command>' для работы с устройствами\n")
    
    return True

while True:
    try:
        superboot_input = input("[ + ]$superboot > ")
        if not process_command(superboot_input):
            break
    except KeyboardInterrupt:
        print("\n\n[ + ] Выход из программы...")
        break
    except EOFError:
        print("\n\n[ + ] Выход из программы...")
        break

