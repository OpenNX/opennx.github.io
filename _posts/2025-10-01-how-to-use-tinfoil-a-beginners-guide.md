---
layout: post
title: "How to Use Tinfoil: A Beginner's Guide"
date: 2025-10-01
categories: guides apps how-to
---

You've successfully set up Custom Firmware on your Nintendo Switch, and now you're ready to explore the world of homebrew applications. One of the most powerful and popular apps you'll encounter is Tinfoil. At its core, Tinfoil is an advanced game installer, but it can do much more.

This guide will walk you through installing Tinfoil and using its most important features.

**Disclaimer:** This guide is for educational purposes only. Tinfoil is a powerful tool that should be used for managing your legally owned game backups and homebrew software. Downloading and installing copyrighted content you do not own is illegal. Always operate on an EmuNAND and take precautions to avoid connecting to Nintendo's servers to reduce the risk of a console ban.

### Prerequisites

Before you begin, ensure you have the following:
* A Nintendo Switch running a modern, up-to-date version of **Atmosphère Custom Firmware**.
* Access to the Homebrew Menu (usually by holding 'R' while launching a game).

### Step 1: Installing Tinfoil

Installing Tinfoil is a straightforward process.

1.  **Download:** Get the latest version of Tinfoil from a trusted source. It usually comes as a `.zip` file containing a file named `tinfoil.nro`.
2.  **Copy to SD Card:** Extract the `.zip` file. On your Switch's SD card, navigate to the `/switch/` folder. Place the `tinfoil.nro` file inside this folder.
3.  **Launch:** Insert the SD card back into your Switch and boot into Atmosphère. Open the Homebrew Menu, and you should see the Tinfoil icon. Select it to launch the application for the first time.

Tinfoil may take a moment to set itself up on the first launch, creating necessary folders on your SD card.

### Step 2: The Main Features - How to Install Games

Tinfoil offers several ways to install content onto your Switch. Here are the most common methods.

#### Method 1: Installing from the SD Card

This is the most basic method.
1.  Place your game files (in `.nsp`, `.nsz`, or `.xci` format) anywhere on your SD card. A folder named `install` or `games` on the root of the card is a good practice.
2.  In Tinfoil, navigate to the **"File Browser"** tab.
3.  Browse to the location of your game files on the SD card.
4.  Select the file you wish to install and follow the on-screen prompts. Choose to install to either the SD card or the internal system memory (NAND).

#### Method 2: Installing Over USB from a PC

This method is very useful as it saves you from having to copy large game files to your SD card first.

1.  **Download a PC-side tool.** You will need an application for your computer like **NS-USBloader**.
2.  **Connect your Switch.** On your Switch, open Tinfoil and navigate to the **"Options"** tab. Scroll down and enable "Install Unsigned Code".
3.  Connect your Switch to your PC using a USB-C cable.
4.  **Send the file from your PC.** Open NS-USBloader on your computer, select the game `.nsp` file, and send it to the Switch. The installation will begin automatically in Tinfoil.

#### Method 3: Adding a Network Location ("Shop")

This is Tinfoil's most famous feature. It allows you to add network locations, often called "shops," to browse and download content directly to your Switch.

1.  In Tinfoil, go to the **"File Browser"** tab.
2.  Press the `-` (minus) or `+` (plus) button on your controller to bring up the location entry menu.
3.  Enter the details for the network location you wish to add. You will need to provide information like the **Protocol** (e.g., `https`), **Host** (e.g., `opennx.github.io`), and an optional **Title**.
4.  Once added, the new location will appear in your File Browser, and its content may also populate the "New Games" and other tabs.

### Best Practices for Safe Usage

* **Always Use an EmuNAND:** Perform all Tinfoil-related activities on your EmuNAND to keep your primary system memory (SysNAND) clean and safe for online play with your purchased games.
* **Stay Offline:** Use DNS blockers like 90DNS or Atmosphère's `exosphere.ini` to block communication with Nintendo's servers while using Tinfoil to prevent console bans.
* **Be Wary of Sources:** Only install files from sources you trust to avoid malicious software that could damage your console.

Tinfoil is an incredibly versatile tool that serves as the central hub for managing content on a modded Switch. By understanding its features and following safe practices, you can make the most of this essential homebrew application.
