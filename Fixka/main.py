import platform
import customtkinter as ctk
import keyboard
import subprocess
import threading
import time
import tkinter as tk
import os
import shutil
import sys

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
# UI
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class SolutionCenterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # UI x,y
        self.title("Fixka")
        self.geometry("350x420")
        self.resizable(False, False)

        # Ikona
        cesta_k_ikone = resource_path("568541-200.png")
        ikona = tk.PhotoImage(file=cesta_k_ikone)
        self.iconbitmap("")
        self.iconphoto(True, ikona)

        # Nadpis
        self.label = ctk.CTkLabel(self, text="Fixka", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=(20, 20))

        # Tlačítko 1: Restart Grafiky
        self.btn_gpu = ctk.CTkButton(self, text="Opravit obraz (Restart GPU)", command=self.restart_gpu, height=40)
        self.btn_gpu.pack(pady=10, padx=40, fill="x")

        # Tlačítko 2: Restart Průzkumníka
        self.btn_explorer = ctk.CTkButton(self, text="Opravit lištu (Restart Explorer)", command=self.restart_explorer, height=40)
        self.btn_explorer.pack(pady=10, padx=40, fill="x")

        # Tlačítko 3: Vyčistit DNS
        self.btn_dns = ctk.CTkButton(self, text="Opravit internet (Flush DNS)", command=self.flush_dns, height=40)
        self.btn_dns.pack(pady=10, padx=40, fill="x")

         # Tlačítko 4: Temp soubory
        self.btn_temp = ctk.CTkButton(self, text="Vyčistit dočasné soubory (Temp)", command=self.smazat_temp, height=40, fg_color="#d97706", hover_color="#b45309")
        self.btn_temp.pack(pady=10, padx=40, fill="x")

        # Tlačítko 5: Výpis verzí
        self.btn_info = ctk.CTkButton(self, text="Systémové informace", command=self.ukaz_info, height=40,
                                      fg_color="#444444", hover_color="#666666")
        self.btn_info.pack(pady=10, padx=40, fill="x")
        # (Status bar)
        self.status_label = ctk.CTkLabel(self, text="Připraveno", font=ctk.CTkFont(size=12, slant="italic"),
                                         text_color="gray")
        self.status_label.pack(side="bottom", pady=15)

    def update_status(self, message):
        self.status_label.configure(text=message)
        self.after(3000, self.clear_status)

    def clear_status(self):
        self.status_label.configure(text="Připraveno")

    # --- JEDNOTLIVÉ OPRAVNÉ FUNKCE ---

    def restart_gpu(self):
        keyboard.send('windows+ctrl+shift+b')
        self.update_status("Grafický ovladač byl restartován!")

    def restart_explorer(self):
        # Shodí a znovu nahodí proces explorer.exe přes příkazový řádek
        subprocess.run("taskkill /f /im explorer.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run("start explorer.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.update_status("Průzkumník byl restartován!")

    def flush_dns(self):
        # Vyčistí mezipaměť DNS
        subprocess.run("ipconfig /flushdns", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.update_status("DNS mezipaměť byla vyčištěna!")

    def ukaz_info(self):
        self.update_status("Načítám informace...")

        # Win vers.
        os_verze = f"Windows {platform.release()} (Sestavení: {platform.version()})"

        # GPU vers.
        try:
            cmd = 'powershell -Command "Get-CimInstance Win32_VideoController | Select-Object Name, DriverVersion | Format-List"'
            gpu_data = subprocess.check_output(cmd, shell=True, text=True, encoding='cp852').strip()
        except Exception:
            gpu_data = "Nepodařilo se načíst informace o grafice."

        vypis = f"--- OPERAČNÍ SYSTÉM ---\n{os_verze}\n\n--- GRAFICKÝ ADAPTÉR ---\n{gpu_data}"

        # Vytvoření nového vyskakovacího okna nad aplikací
        info_okno = ctk.CTkToplevel(self)
        info_okno.title("Systémové informace")
        info_okno.geometry("400x300")
        info_okno.attributes("-topmost", True)
        info_okno.grab_set()

        # Textové pole pro výpis
        textbox = ctk.CTkTextbox(info_okno, width=380, height=280)
        textbox.pack(padx=10, pady=10)
        textbox.insert("0.0", vypis)
        textbox.configure(state="disabled")

        self.update_status("Informace načteny!")

    def smazat_temp(self):
        self.update_status("Mažu dočasné soubory...")
        temp_dir = os.environ.get('TEMP')

        if temp_dir:
            for polozka in os.listdir(temp_dir):
                cesta = os.path.join(temp_dir, polozka)
                try:
                    if os.path.isfile(cesta) or os.path.islink(cesta):
                        os.remove(cesta)
                    elif os.path.isdir(cesta):
                        shutil.rmtree(cesta)
                except Exception:
                    pass 

        self.update_status("Temp složka byla vyčištěna!")


# Spuštění aplikace
if __name__ == "__main__":
    app = SolutionCenterApp()
    app.mainloop()