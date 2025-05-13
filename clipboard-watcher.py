#!/usr/bin/env python3
"""
📋 Clipboard Watcher
--------------------
A Python script that monitors your system clipboard for changes.
When you manually copy any text (e.g. Ctrl+C), this script detects it,
prints the copied content, and saves it to a file.

✅ Works globally — across browser, editors, terminal, PDF viewers, etc.
✅ No root permissions required
✅ Linux, macOS, Windows compatible (with proper clipboard backend)

Author: Tuguldur Gantumur
License: MIT
"""

import pyperclip
import time
import os

# Output file where copied text will be stored
DESTINATION_FILE = "pasted_output.txt"
# Tracks the last clipboard contents to avoid duplicates
last_clipboard = ""

def ensure_output_file_exists():
    """Create the output file if it doesn't exist."""
    if not os.path.exists(DESTINATION_FILE):
        with open(DESTINATION_FILE, 'w', encoding='utf-8') as f:
            pass

def monitor_clipboard():
    """Continuously monitor the clipboard and save new content."""
    global last_clipboard
    print("📋 Clipboard watcher started.")
    print("👉 Select text anywhere and press Ctrl+C to copy it.")
    print("🔄 This script will detect new clipboard content and save it.")
    print("🔚 Press Ctrl+C in terminal to quit.\n")

    try:
        while True:
            current_clipboard = pyperclip.paste()
            if current_clipboard != last_clipboard and current_clipboard.strip():
                print(f"📋 Copied: {current_clipboard.strip()}")
                with open(DESTINATION_FILE, "a", encoding="utf-8") as f:
                    f.write(current_clipboard.strip() + "\n")
                last_clipboard = current_clipboard
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"\n👋 Exiting. All copied text saved to '{DESTINATION_FILE}'.")

if __name__ == "__main__":
    ensure_output_file_exists()
    monitor_clipboard()
