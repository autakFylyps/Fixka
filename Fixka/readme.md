#  Fixka (Solution Center)

Fixka je jednoduchá, blbuvzdorná desktopová aplikace pro OS Windows, která slouží jako "Quick Fix" nástroj pro běžné uživatele. Nabízí záchranu v situacích, kdy zamrzne obraz, spadne lišta, nejede internet nebo dochází místo na disku – to všechno na jedno kliknutí v moderním a kompaktním grafickém rozhraní.

## Co aplikace umí (Funkce)

* **Opravit obraz (Restart GPU):** Nasimuluje klávesovou zkratku `Win + Ctrl + Shift + B` a bezpečně restartuje grafické ovladače. Ideální při problémech s monitorem nebo hrami.
* **Opravit lištu (Restart Explorer):** Tvrdě ukončí a znovu spustí proces `explorer.exe`. Řeší zamrznutou hlavní lištu, nereagující plochu nebo zaseknutá okna.
* **Opravit internet (Flush DNS):** Vyčistí mezipaměť DNS (`ipconfig /flushdns`). Rychlá pomoc, když "nejede internet" nebo se nenačítají konkrétní stránky.
* **Systémové informace:** Zobrazí aktuální verzi Windows a detaily o grafickém adaptéru (včetně verze ovladače) pro snadnější diagnostiku.
* **Vyčistit dočasné soubory (Temp):** Promaže uživatelskou složku `%temp%`, čímž bezpečně uvolní místo na disku a odstraní zbytečný balast.

## Jak aplikaci spustit (Pro běžné uživatele)

1. Stáhněte si hotový soubor **Fixka.exe**.
2. Umístěte jej ideálně do složky `Dokumenty` nebo `Program Files`.
3. Klikněte na něj pravým tlačítkem a zvolte **Zobrazit více možností -> Odeslat na -> Plocha (vytvořit zástupce)**.
4. Zástupce na ploše si můžete libovolně přejmenovat (např. na "Fixka") a spouštět aplikaci přímo z něj.
5. *Aplikace nevyžaduje instalaci ani administrátorská práva (UAC).*

## Sestavení z kódu (Pro vývojáře)

Pokud si chcete aplikaci upravit a zabalit sami, budete potřebovat nainstalovaný **Python 3.x**.

**1. Instalace potřebných knihoven:**
```bash
pip install customtkinter keyboard Pillow pyinstaller
```

**2. Příprava ikon (volitelné):**
Ujistěte se, že máte ve složce s projektem obrázek `568541-200.png` a převedenou ikonu `ikona.ico`.

**3. Sestavení do .exe souboru:**
Otevřete terminál ve složce s vaším zdrojovým kódem (`main.py`) a spusťte následující příkaz:
```bash
pyinstaller --noconsole --onefile --add-data "568541-200.png;." --icon="ikona.ico" --name "Fixka" main.py
```

Výsledný spustitelný `.exe` soubor naleznete v nově vytvořené složce `dist`.

## Použité technologie

* **[Python](https://www.python.org/)** (Logika aplikace)
* **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** (Moderní grafické rozhraní)
* **Subprocess & OS** (Komunikace se systémem Windows)
* **[PyInstaller](https://pyinstaller.org/)** (Balení do spustitelného souboru)
* Vibecoding Google Gemini - nudil jsem se při večeru