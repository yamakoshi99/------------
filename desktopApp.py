import datetime
import os
import tkinter as tk
from tkinter import filedialog

DATA_TIME = "時間表示"


class DesktopApp:
    def __init__(self, root, title):
        self.root = root
        self.root.title("デスクトップアプリ")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.time_button = tk.Button(self.frame, text=title)
        self.time_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.listbox = tk.Listbox(self.frame)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.update_time()

    def open_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.listbox.delete(0, tk.END)
            for file_name in os.listdir(folder_path):
                self.listbox.insert(tk.END, file_name)

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_button.config(text=current_time)
        self.root.after(1000, self.update_time)


if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopApp(root, DATA_TIME)
    root.mainloop()
