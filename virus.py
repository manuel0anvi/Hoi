import tkinter as tk
import os
import ctypes
import keyboard  # pip install keyboard
import time
from datetime import datetime

# Get user32 and kernel32 for hiding console
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

class VirusPrank:
    def __init__(self):
        # Hide Console Window FIRST
        try:
            user32.ShowWindow(kernel32.GetConsoleWindow(), 0)
        except:
            pass

        self.root = tk.Tk()
        self.root.title("System Error")
        
        # Block Windows Keys and shortcuts using keyboard library
        keyboard.block_key('left windows')
        keyboard.block_key('right windows')
        keyboard.block_key('alt')
        keyboard.block_key('f4')
        keyboard.block_key('esc')
        keyboard.block_key('tab')
        
        # Configure full screen and aggressive behaviors
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True) 
        self.root.configure(bg='black')
        self.root.config(cursor="none")

        self.secret_code = "unlock"
        self.input_buffer = ""
        
        # Setup logging
        self.log_file = os.path.join(os.path.dirname(__file__), 'keylog.txt')
        self.log(f"=== Script started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")

        self.setup_ui()
        
        # Listen with tkinter only (no keyboard library)
        self.root.bind('<KeyPress>', self.on_key)
        self.root.bind('<FocusOut>', self.on_focus_out)
        self.root.protocol("WM_DELETE_WINDOW", self.disable_event)
        
        self.keep_topmost()
        
        # Auto-close after 60 seconds (1 minute) as safety feature
        self.root.after(60000, self.auto_close)

    def log(self, message):
        """Write to log file"""
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"{message}\n")
        except:
            pass

    def setup_ui(self):
        frame = tk.Frame(self.root, bg='black')
        frame.place(relx=0.5, rely=0.5, anchor='center')

        try:
            image_path = os.path.join(os.path.dirname(__file__), 'assets', 'hacked_bg.png')
            if os.path.exists(image_path):
                self.bg_image = tk.PhotoImage(file=image_path)
                bg_label = tk.Label(frame, image=self.bg_image, bg='black')
                bg_label.pack(pady=20)
        except Exception:
            pass

        tk.Label(frame, text="CRITICAL ERROR", font=("Courier", 72, "bold"), fg="red", bg="black").pack()
        tk.Label(frame, text="SYSTEM COMPROMISED", font=("Courier", 36), fg="red", bg="black").pack()
        
        term_text = "> DELETING FILES...\n> UPLOADING DATA TO SERVER...\n> OVERRIDING SECURITY PROTOCOLS..."
        tk.Label(frame, text=term_text, font=("Courier", 18), fg="#0f0", bg="black", justify="left").pack(pady=30)

    def disable_event(self):
        pass

    def on_focus_out(self, event):
        self.root.lift()
        self.root.focus_force()

    def on_key(self, event):
        # Only process single character keys
        if event.char and len(event.char) == 1 and event.char.isprintable():
            self.input_buffer += event.char.lower()
            # Keep only the last 20 characters (sliding window)
            self.input_buffer = self.input_buffer[-20:]
            
            # Log what was typed
            self.log(f"Key pressed: '{event.char}' | Buffer: {self.input_buffer}")
            
            # Check if unlock code is in buffer
            if self.secret_code in self.input_buffer:
                self.log("UNLOCK CODE DETECTED! Exiting...")
                self.cleanup_and_exit()

    def keep_topmost(self):
        try:
            self.root.lift()
            self.root.focus_force()
            self.root.attributes('-topmost', True)
        except:
            pass
        self.root.after(50, self.keep_topmost)

    def auto_close(self):
        """Auto-close after 1 minute as safety feature"""
        self.log("Auto-closing after 1 minute timeout")
        self.cleanup_and_exit()

    def cleanup_and_exit(self):
        self.log(f"=== Script ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        # Unblock all keys before exiting
        try:
            keyboard.unhook_all()
            keyboard.unblock_key('left windows')
            keyboard.unblock_key('right windows')
            keyboard.unblock_key('alt')
            keyboard.unblock_key('f4')
            keyboard.unblock_key('esc')
            keyboard.unblock_key('tab')
        except:
            pass
        self.root.destroy()

if __name__ == "__main__":
    app = VirusPrank()
    app.root.mainloop()
