---
layout: post
title: "How to Add the Tinfoil 'Port Shop' to Stream Native Game Ports on Nintendo Switch"
date: 2026-06-29 18:00:00 -0000
categories: tutorials switch
tags: [nintendo-switch, tinfoil, homebrew, ports]
---

One of the coolest aspects of the Nintendo Switch homebrew community is the dedication to decompiling, extracting, and re-compiling classic PC, Android, and retro games to run **natively** on the Switch hardware. Instead of lagging under heavy emulation, these games are optimized to run flawlessly on the console.

To make discovering these gems easier, community developers have launched a dedicated **"Port Shop"** repository right inside Tinfoil. 

Here is a guide on how to configure this custom repository and what incredible native ports are currently available to download.

---

### What Games are Available?
The Port Shop is actively under construction, meaning games are continuously added. Some of the notable titles you can expect to find include:

* **Zelda Titles:** *Zelda Ocarina of Time*, *Majora's Mask*, and *Zelda Link's Awakening DX HD* (a modified high-definition version of the original Game Boy Color game).
* **Classic RPGs & Adventures:** Android versions of *Chrono Trigger*, *Final Fantasy III 3D*, *Final Fantasy IV 3D*, and *Doctor Layton*.
* **Action & Shooters:** *Medal of Honor*, *Bully*, *Driver 2*, *Grand Theft Auto: Liberty City Stories*, and *Chinatown Wars*.
* **Platformers & Fan Projects:** *Mega Man 2.5D* (a fan-made PC game natively ported over), *Sonic 4 Episode 2* (including Episode Metal), *Celeste 64*, *Super Mario X*, and *Super Mario War*.
* **Retro Classics:** *Star Fox 64* (featuring full Portuguese text and HD UI texture updates created by Delson and YouTuber 'Eu sou o Depois') and *Mario Kart 64*.

---

### Step-by-Step Guide to Add the Port Shop

Setting up this repository takes less than a minute. Ensure your Nintendo Switch is turned on, connected to the internet, and that you have Tinfoil working.

#### Option A: Manual Setup
1. Launch **Tinfoil** from your custom firmware menu.
2. In the left-hand sidebar menu, scroll down and select **File Browser**.
3. Press **Right** on your D-pad to enter the file directory area, then press the **Minus (-)** button on your controller to create a **New** network source.
4. Fill in the network configuration form exactly as follows:
   * **Protocol:** `https`
   * **Host:** `opennx.github.io`
   * **Port:** *(Leave blank)*
   * **Path:** `/portnx`
   * **Title:** `Port NX` *(Or any identifying name you prefer)*
   * **Enabled:** `Yes`
5. Press the **X** button to save the source.

#### Option B: Via the Open NX Forwarder

If you are already utilizing the **opennx.github.io** network forwarder inside your Tinfoil source configuration profile, this index link is automatically synchronized. 
Simply refresh your network indices through the OpenNX link to populate the latest ported entries directly into your game list without managing separate server addresses.

---

### How to Browse and Install the Ports
Once saved, close and restart Tinfoil to ensure the repository initializes properly. 

* To find the titles, head over to the **New Games** section. 
* *Pro tip:* If your list is cluttered with standard titles from other active shops, you can temporarily go back to your **File Browser**, edit your other shops, and toggle them to `Enabled: No` so only the Port Shop is visible.
* Highlight a game and press the **Minus (-)** button to turn on image preview thumbnails to view game covers.
* Select your game with **A**, pick your installation target (**NAND** or **SD Card**), and Tinfoil will stream the files down and unpack them straight into your storage.

### A Note on Performance
Because these are community-driven native ports or Android translations, some titles may have minor bugs or occasional crashes. The community is constantly working on improvements, so keep your eye on the shop for updates and additional titles like *Max Payne* or *The Simpsons Hit & Run* as they get added in the near future!

***
*Credits to Delson, Derick, and the homebrew scene developers for making this repository possible. For a full visual walkthrough and gameplay previews of the shop, check out the source video by [Eu sou o Depois](http://www.youtube.com/watch?v=9OJOrL_i8YQ).*
