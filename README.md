# 📋 Clipboard Watcher

A simple Python script that monitors your clipboard for new copied text, prints it, and saves it to a file.

## ✨ Features

- ✅ Global clipboard monitoring (works outside the terminal or editor)
- ✅ Cross-platform support: Linux, macOS, Windows
- ✅ No root or special privileges required
- ✅ Automatically saves copied text to a file (`pasted_output.txt`)

## 🔧 Requirements

- Python 3.x
- [`pyperclip`](https://pypi.org/project/pyperclip/)

### Linux Notes

On Linux, you'll also need one of the following tools installed for clipboard support:

```bash
sudo apt install xclip   # or
sudo apt install xsel
```

### 📦 Installation
```bash
git clone https://github.com/gtrtuugii/clipboard-watcher.git
cd clipboard-watcher
pip install -r requirements.txt
```

### ▶️ Usage
Run the script:
```bash
python3 clipboard_watcher.py
```
Then simply:

    Select any text (anywhere: browser, terminal, etc.)

    Press Ctrl + C

    The script will:

        Detect the clipboard update

        Print the copied text

        Save it to pasted_output.txt

To stop the script, press Ctrl + C in the terminal.

### 📁 Output

Copied content is appended to pasted_output.txt in the current directory.

## 🧪 Setting up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```