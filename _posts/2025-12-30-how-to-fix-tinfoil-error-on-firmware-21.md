---
layout: post
title: "How to Fix Tinfoil Error on Firmware 21.0.0+"
date: 2025-12-30
categories: guides troubleshooting firmware
---

Nintendo Switch Firmware 21.0.0+ introduced major internal changes (ABI changes) that caused Tinfoil to crash with the error: **"The software was closed because an error occurred."**

To get Tinfoil running again, it is **highly recommended to update only the Tinfoil files** rather than your entire CFW pack. This keeps your custom settings intact and ensures a cleaner fix.

---

### Method 1: Manual Tinfoil Update (Recommended)

This is the best way to fix the error without changing your entire Atmosphere setup.

1.  **Download the Fix:** **[Tinfoil 21+ Fix (.rar)](https://www.mediafire.com/file/llifnihm03xhq0u/Tinfoil_21%252B.rar/file)**
2.  **Extract Files:** Unzip the `.rar` file on your computer.
3.  **Apply Fix:** Copy the extracted folders (usually `switch` and/or `atmosphere` components) to the **root of your SD card**. 
4.  **Overwrite:** Choose **"Yes"** to overwrite all files when prompted.
5.  **Launch:** Restart your Switch and open Tinfoil through the **Homebrew Menu** (holding 'R' while launching a game).

---

### Method 2: Update via CNX Pack (Alternative)

If you are already using the **CNX Pack** (formerly Sphaira) and prefer to update your entire system at once, the latest release now includes a working version of Tinfoil out of the box.

1.  **Download CNX Release:** **[CNX Pack v21.1.0-1](https://github.com/CostelaCNX/CNX/releases/tag/21.1.0-1)**
2.  **Install:** Extract and copy the entire pack to the root of your SD card, overwriting all existing files.
3.  **Verify:** This will update Atmosphere, Sigpatches, and Tinfoil simultaneously to match Firmware 21 compatibility.

---

### Critical: Sigpatches
Even with the Tinfoil fix, the app **will not work** without the latest Sigpatches for Firmware 21. If you use Method 1, make sure you also have the most recent patches installed manually.

### Troubleshooting
* **Checking for Updates hang:** If Tinfoil gets stuck on the loading screen, verify that your console's **Date and Time** are synchronized via the internet.
* **Applet Mode:** Never launch Tinfoil through the Album icon. Always use **Title Override** (hold 'R' while starting a game) to ensure Tinfoil has full RAM access.

---
*Disclaimer: Modifying console software carries risks. Always maintain a NAND backup and use an EmuNAND.*
