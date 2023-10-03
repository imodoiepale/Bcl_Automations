import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, scrolledtext
from subprocess import run
import sys

# Get the path to the icon file
icon_path = os.path.join(sys._MEIPASS, "pass.ico")


class DarkThemeMixin:
    def set_dark_theme(self):
        self.configure(fg_color="#282C34", bg_color="#282C34", border_color="#1E2228", text_color="#FFFFFF")

class HomePage(ctk.CTk, DarkThemeMixin):
    def __init__(self):
        super().__init__()

        self.set_dark_theme()
        self.title("Home Page")
        self.geometry("400x300")

        kra_button = ctk.CTkButton(self, text="KRA", command=self.open_kra_page)
        ecitizen_button = ctk.CTkButton(self, text="eCitizen", command=self.open_ecitizen_page)
        nhif_button = ctk.CTkButton(self, text="NHIF", command=self.open_nhif_page)
        nssf_button = ctk.CTkButton(self, text="NSSF", command=self.open_nssf_page)

        kra_button.grid(row=0, column=0, padx=20, pady=20)
        ecitizen_button.grid(row=0, column=1, padx=20, pady=20)
        nhif_button.grid(row=1, column=0, padx=20, pady=20)
        nssf_button.grid(row=1, column=1, padx=20, pady=20)

    def open_kra_page(self):
        self.destroy()
        kra_page = KRAPage()
        kra_page.mainloop()

    def open_ecitizen_page(self):
        self.destroy()
        ecitizen_page = ECitizenPage()
        ecitizen_page.mainloop()

    def open_nhif_page(self):
        self.destroy()
        nhif_page = NHIFPage()
        nhif_page.mainloop()

    def open_nssf_page(self):
        self.destroy()
        nssf_page = NSSFPage()
        nssf_page.mainloop()

class BasePage(ctk.CTk, DarkThemeMixin):
    def __init__(self, title, back_command):
        super().__init__()

        self.set_dark_theme()
        self.title(title)
        self.geometry("500x600")

        self.output_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=40, height=10)
        self.output_text.grid(row=0, column=0, padx=20, pady=20)

        check_passwords_button = ctk.CTkButton(self, text="Check Passwords", command=self.check_passwords)
        check_passwords_button.grid(row=1, column=0, padx=20, pady=20)

        back_button = ctk.CTkButton(self, text="Back", command=back_command)
        back_button.grid(row=2, column=0, padx=20, pady=260)  # Align the button to the bottom

    def go_back_home(self):
        self.destroy()
        home_page = HomePage()
        home_page.mainloop()

    def check_passwords(self, script_name):
        script_path = f"{script_name}.py"
        result = run(["python", script_path], capture_output=True, text=True)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result.stdout + result.stderr)

class KRAPage(BasePage):
    def __init__(self):
        super().__init__("KRA Page", self.go_back_home)
        
    def check_passwords(self):
        script_path = "kra_passwords.py"
        result = run(["python", script_path], capture_output=True, text=True)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result.stdout + result.stderr)

    def go_back_home(self):
        self.destroy()
        home_page = HomePage()
        home_page.mainloop()

class ECitizenPage(BasePage):
    def __init__(self):
        super().__init__("eCitizen Page", self.go_back_home)

    def check_passwords(self):
        script_path = "ecitizen_pass.py"
        result = run(["python", script_path], capture_output=True, text=True)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result.stdout + result.stderr)

    def go_back_home(self):
        self.destroy()
        home_page = HomePage()
        home_page.mainloop()

class NHIFPage(BasePage):
    def __init__(self):
        super().__init__("NHIF Page", self.go_back_home)

    def check_passwords(self):
        script_path = "nhif_passwords.py"
        result = run(["python", script_path], capture_output=True, text=True)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result.stdout + result.stderr)

    def go_back_home(self):
        self.destroy()
        home_page = HomePage()
        home_page.mainloop()

class NSSFPage(BasePage):
    def __init__(self):
        super().__init__("NSSF Page", self.go_back_home)

    def check_passwords(self):
        script_path = "nssf_passwords.py"
        result = run(["python", script_path], capture_output=True, text=True)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result.stdout + result.stderr)

    def go_back_home(self):
        self.destroy()
        home_page = HomePage()
        home_page.mainloop()

if __name__ == "__main__":
    home_page = HomePage()
    home_page.mainloop()
