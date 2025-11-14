
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

SuperBoot [RUS] - Программа для работы с устройствами линейки Xiaomi Redmi. Можно выполнять fastboot, oem команды. Также есть команды Flash.

ВАЖНО!!!
СОЗДАТЕЛЬ ПРОГРАММЫ НЕ УВЕРЕН В САМОЙ ПРОГРАММЕ И РАБОЧИЙ ЛИ СКРИПТ НА 100% ПРОЦЕНТОВ. В КОМАНДЕ НЕТУ ТЕСТИРОВЩИКОВ И МОГУТ ПОЯВЛЯТЬСЯ БАГИ. ПРОГРАММА НЕ ТЕСТИРОВАЛАСЬ!!!

A powerful command-line tool for managing Xiaomi/Redmi Android devices via Fastboot and ADB.

![Superboot](https://img.shields.io/badge/version-2.4-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

## Features

- 🔓 Bootloader unlock/lock operations
- 📦 Flash partitions (boot, recovery, system, etc.)
- 🔄 Device reboot (normal, bootloader, recovery)
- 📱 Device detection (Fastboot & ADB)
- 🛠️ Direct Fastboot and ADB command execution
- 💻 Cross-platform support (Windows, Linux, macOS)

## Requirements

- Python 3.6 or higher
- [Android SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools) (Fastboot & ADB)
- USB drivers for your device (for Xiaomi: [Mi USB Driver](https://www.xiaomi.com/support/))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/superboot.git
cd superboot
```

2. Make sure Fastboot and ADB are installed and in your PATH:
```bash
fastboot --version
adb --version
```

3. Run the script:
```bash
python superboot.py
```

## Usage

### Basic Commands

```
help              - Show all available commands
exit              - Exit the program
clear/cls         - Clear the screen
ver               - Show Superboot version
```

### Superboot Commands (Fastboot-like)

```
superboot oem unlock              - Unlock bootloader
superboot oem lock                - Lock bootloader
superboot flash boot boot.img     - Flash boot partition
superboot flash recovery rec.img  - Flash recovery partition
superboot reboot                  - Reboot device
superboot reboot bootloader       - Reboot to bootloader
superboot reboot recovery         - Reboot to recovery
superboot devices                 - List connected devices (Fastboot & ADB)
superboot fastboot <cmd>          - Execute direct fastboot command
superboot adb <cmd>               - Execute direct adb command
```

### Examples

```bash
# Unlock bootloader
superboot oem unlock

# Flash boot image
superboot flash boot boot.img

# Reboot to bootloader
superboot reboot bootloader

# List all connected devices
superboot devices

# Direct fastboot command
superboot fastboot getvar all
```

## Important Notes

⚠️ **WARNING**: 
- This tool performs low-level operations on your device
- Unlocking bootloader may void warranty
- Always backup your data before flashing
- Use at your own risk
- The developer is not responsible for any damage to your device

## Supported Devices

- Xiaomi devices
- Redmi devices
- Other Android devices with Fastboot support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is provided "as is" without warranty of any kind. The developer is not responsible for any damage that may occur from using this tool. Always follow official device documentation and guidelines.

---

**Made with ❤️ for the Android modding community**

