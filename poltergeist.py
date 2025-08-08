import pyautogui
import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import sys
import os
import math
from datetime import datetime
from pathlib import Path
import subprocess

class DigitalPoltergeist:
    def __init__(self):
        self.running = False
        self.threads = []
        self.intensity = "medium"
        self.safe_mode = True
        self.stop_event = threading.Event()

        # Last media tracking to avoid repeats
        self.last_played_media = None

        # Messages
        self.typing_messages = [
            "I am here...",
            "Can you see me?",
            "The machine remembers...",
            "01001000 01100101 01101100 01110000",
            "You are not alone...",
            "The dead walk among your files...",
            "I live in the circuits now...",
            "Why did you wake me?",
            "Your soul belongs to the machine..."
        ]
        self.error_messages = [
            "PRESENCE DETECTED: Unknown entity accessing system",
            "WARNING: Spectral interference in memory sectors",
            "ERROR 666: The dead walk among your files",
            "ALERT: Ectoplasmic residue found in registry",
            "GHOST.EXE has stopped responding",
            "Memory leak detected in spiritual realm",
            "HAUNTED: Your computer has been possessed",
            "WARNING: Soul trapped in hard drive",
            "ERROR: Too many spirits in the machine"
        ]
        self.protected_windows = [
            "task manager", "system configuration", "registry editor",
            "command prompt", "powershell", "system settings",
            "activity monitor", "terminal", "system preferences", "settings"
        ]

        self.root = None

        # Predefined jumpscare and audio files
        here = Path(__file__).parent
        self.jumpscare_videos = [here / f for f in ["1.mp4", "3.mp4", "4.mp4", "5.mp4", "6.mp4"] if (here / f).exists()]
        self.creepy_audios = [here / f for f in ["knock.wav", "whisper.aiff", "scream.mp3", "static.mp3"] if (here / f).exists()]

    def log(self, msg):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"[{ts}] GHOST: {msg}")

    def is_safe_window(self):
        if not self.safe_mode:
            return True
        try:
            win = pyautogui.getActiveWindow()
            if win:
                title = (win.title or "").lower()
                for protected in self.protected_windows:
                    if protected in title:
                        return False
        except Exception:
            return True
        return True

    def ghost_mouse(self):
        while self.running and not self.stop_event.is_set():
            try:
                if self.is_safe_window() and random.random() < 0.35:
                    w, h = pyautogui.size()
                    movement_type = random.choice(["random", "circle", "zigzag"])
                    if movement_type == "random":
                        x = random.randint(100, max(100, w - 100))
                        y = random.randint(100, max(100, h - 100))
                        pyautogui.moveTo(x, y, duration=random.uniform(0.5, 1.8))
                        self.log(f"Mouse moved mysteriously to ({x}, {y})")
                    elif movement_type == "circle":
                        cx, cy = w // 2, h // 2
                        radius = random.randint(80, 160)
                        for angle in range(0, 360, 12):
                            if not self.running or self.stop_event.is_set():
                                break
                            x = cx + radius * math.sin(math.radians(angle))
                            y = cy + radius * math.cos(math.radians(angle))
                            pyautogui.moveTo(int(x), int(y), duration=0.05)
                        self.log("Mouse drew a mysterious circle")
                    else:
                        sx, sy = pyautogui.position()
                        for i in range(6):
                            if not self.running or self.stop_event.is_set():
                                break
                            x = sx + ((-1) ** i) * (i * 55)
                            y = sy + i * 28
                            pyautogui.moveTo(x, y, duration=0.12)
                        self.log("Mouse moved in a zigzag pattern")
            except Exception as e:
                self.log(f"Mouse ghost error: {e}")
            time.sleep(random.uniform(0.5, 2.5))

    def ghost_scroll(self):
        """Spooky fast scroll with up/down movement."""
        while self.running and not self.stop_event.is_set():
            try:
                if self.is_safe_window() and random.random() < 0.25:  # Slightly more frequent
                    w, h = pyautogui.size()
                    # Move mouse to a random spot in the central area of the screen
                    target_x = random.randint(w // 4, 3 * w // 4)
                    target_y = random.randint(h // 4, 3 * h // 4)
                    pyautogui.moveTo(target_x, target_y, duration=0.1)

                    direction = random.choice(["up", "down"])
                    clicks = random.randint(15, 40)  # More intense scrolling
                    amount = 1 if direction == "up" else -1

                    # Very quick scrolling loop
                    for _ in range(clicks):
                        if not self.running or self.stop_event.is_set():
                            break
                        pyautogui.scroll(amount)
                        time.sleep(0.005)  # Faster than before

                    self.log(f"Scrolled {direction} very quickly ({clicks} steps)")
            except Exception as e:
                self.log(f"Scroll ghost error: {e}")
            time.sleep(random.uniform(0.5, 1.5))


    def ghost_typing(self):
        while self.running and not self.stop_event.is_set():
            try:
                if self.is_safe_window() and random.random() < 0.12:
                    message = random.choice(self.typing_messages)
                    speed = random.uniform(0.05, 0.2)
                    for ch in message:
                        if not self.running or self.stop_event.is_set():
                            break
                        pyautogui.write(ch)
                        time.sleep(speed)
                    self.log(f"Typed: '{message}'")
            except Exception as e:
                self.log(f"Typing ghost error: {e}")
            time.sleep(random.uniform(1.0, 4.0))

    def ghost_popups(self):
        while self.running and not self.stop_event.is_set():
            try:
                if random.random() < 0.10:
                    msg = random.choice(self.error_messages)
                    t = random.choice([
                        "System Ghost Alert",
                        "Paranormal Activity Detected",
                        "Supernatural Error",
                        "Ghost in the Shell",
                        "Spectral Warning"
                    ])
                    r = tk.Tk()
                    r.withdraw()
                    r.attributes("-topmost", True)
                    kind = random.choice(["error", "warning", "info"])
                    if kind == "error":
                        messagebox.showerror(t, msg, parent=r)
                    elif kind == "warning":
                        messagebox.showwarning(t, msg, parent=r)
                    else:
                        messagebox.showinfo(t, msg, parent=r)
                    r.destroy()
                    self.log(f"Popup: '{msg}'")
            except Exception as e:
                self.log(f"Popup ghost error: {e}")
            time.sleep(random.uniform(2.0, 6.0))
    def play_audio_in_background(self, file_path):
        try:
            if sys.platform == "win32":
                subprocess.Popen(["powershell", "-c", f"(New-Object Media.SoundPlayer '{file_path}').PlaySync();"], shell=True)
            elif sys.platform == "darwin":
                subprocess.Popen(["afplay", str(file_path)])
            else:
                subprocess.Popen(["mpg123", str(file_path)])
        except Exception as e:
            self.log(f"Audio play error: {e}")

    def ghost_media(self):
        last_play_time = 0
        interval = 20  # Seconds between media events (increased frequency)
        while self.running and not self.stop_event.is_set():
            try:
                now = time.time()
                if now - last_play_time >= interval:
                    available_media = []
                    media_type = random.choice(["video", "audio"])
                    if media_type == "video" and self.jumpscare_videos:
                        available_media = [m for m in self.jumpscare_videos if m != self.last_played_media]
                    elif media_type == "audio" and self.creepy_audios:
                        available_media = [m for m in self.creepy_audios if m != self.last_played_media]

                    if available_media:
                        chosen = random.choice(available_media)
                        self.last_played_media = chosen
                        if media_type == "video":
                            self.log(f"MEDIA: Playing video {chosen.name}")
                            subprocess.Popen([
                                "ffplay", "-fs", "-autoexit", "-loglevel", "quiet", str(chosen)
                            ])
                        else:
                            self.log(f"MEDIA: Playing audio {chosen.name}")
                            self.play_audio_in_background(chosen)

                    last_play_time = now
            except Exception as e:
                self.log(f"Media ghost error: {e}")
            time.sleep(2)

    def start(self):
        if self.running:
            return
        self.running = True
        self.stop_event.clear()
        self.log("Digital Poltergeist Awakening...")
        self.log("Move mouse to top-left for emergency stop (PyAutoGUI failsafe).")
        workers = [
            ("Mouse", self.ghost_mouse),
            ("Scroll", self.ghost_scroll),
            ("Typing", self.ghost_typing),
            ("Popups", self.ghost_popups),
            ("Media", self.ghost_media),
        ]
        for name, target in workers:
            t = threading.Thread(target=target, name=f"{name} Ghost", daemon=True)
            t.start()
            self.threads.append(t)
            self.log(f"{name} Ghost summoned")

    def stop(self):
        if not self.running:
            return
        self.log("Exorcising ghost...")
        self.running = False
        self.stop_event.set()
        time.sleep(0.5)
        self.log("The system is cleansed. 🕊️")

    def build_control_window(self):
        self.root = tk.Tk()
        self.root.title("Digital Poltergeist Control")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)
        frm = tk.Frame(self.root, padx=10, pady=10)
        frm.pack()
        status = tk.Label(frm, text="Status: Possession in progress...", fg="purple")
        status.pack(pady=(0, 8))

        def on_stop():
            self.stop()
            try:
                self.root.destroy()
            except Exception:
                pass

        stop_btn = tk.Button(frm, text="Stop (Exorcise)", command=on_stop, fg="white", bg="red")
        stop_btn.pack(fill="x")
        info = tk.Label(
            frm,
            text="Emergency stop: move mouse to top-left corner.\nSafe mode avoids system windows.",
            fg="gray"
        )
        info.pack(pady=(8, 0))
        self.root.protocol("WM_DELETE_WINDOW", on_stop)

    def run(self):
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.08
        self.start()
        self.build_control_window()
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()

    @staticmethod
    def show_confirm_dialog(title, message):
        r = tk.Tk()
        r.withdraw()
        r.attributes("-topmost", True)
        answer = messagebox.askyesno(title, message, parent=r)
        r.destroy()
        return answer


# Play valak.mp4 using ffplay
def play_valak_video():
    here = Path(__file__).parent
    valak_video = here / "valak.mp4"
    if not valak_video.exists():
        print("[INIT] valak.mp4 not found in program directory.")
        return
    
    try:
        subprocess.run([
            "ffplay",
            "-fs",
            "-autoexit",
            "-loglevel", "quiet",
            str(valak_video)
        ])
    except FileNotFoundError:
        print("FFmpeg not found. Install it from https://ffmpeg.org/download.html")


def main():
    app = DigitalPoltergeist()

    # Step 1: Ask first
    confirm = app.show_confirm_dialog(
        title="Digital Poltergeist",
        message="Ready for an amazing adventure?"
    )
    if not confirm:
        print("User chose No. Exiting.")
        return

    # Step 2: Play video only once after Yes
    play_valak_video()

    # Step 3: Start haunting
    try:
        app.run()
    except pyautogui.FailSafeException:
        print("Failsafe triggered. Exiting.")
        app.stop()
    except Exception as e:
        print(f"Unexpected error: {e}")
        app.stop()


if __name__ == "__main__":
    main()
