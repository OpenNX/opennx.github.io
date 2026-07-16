---
layout: post
title: "Network Installations via DBI: Configuring Your Repositories"
date: 2026-07-16 12:00:00 +0100
categories: guides tutorial dbi
---

While many users treat DBI primarily as an offline USB/MTP file responder, it actually contains a powerful, lightweight network layer capable of streaming and installing files straight from secure online indices. 

If you are looking for an alternative application environment to handle network streaming over your local Wi-Fi, configuring external directories within DBI offers a clean, stable, and highly efficient solution. Currently, two of the premier remote ecosystems utilizing this method are **[Pixel Goblin](https://pixelgoblin.link/r/awarelocale28)** and **notUltraNX**.

> **Crucial Requirement:** Use a recent, modern DBI build — older legacy versions cannot parse remote index scripts or HTTP network repositories correctly.

---

### Repository 1: [Pixel Goblin](https://pixelgoblin.link/r/awarelocale28)

Connecting Pixel Goblin directly into your console environment takes less than a minute and can be done completely on your Switch without touching a computer:

1. Open **DBI** on your Switch.
2. Open the remote-install / HTTP source option and choose to add a source.
3. Use this URL: `https://pixelgoblin.link/api/shop`
4. When prompted, enter the Username and Password from your private [Pixel Goblin Dashboard](https://pixelgoblin.link/r/awarelocale28) fields.
5. Save. Your titles load straight from the index.

---

### Repository 2: notUltraNX

The specialized notUltraNX index utilizes pre-configured setup layout tables to mount its directory trees smoothly onto DBI's interface:

1. Download the pre-configured [dbi.config](https://files.ultranx.ru/shared/dbi/dbi.config) and [dbi.locations](https://files.ultranx.ru/shared/dbi/dbi.locations) files and put them into your `/switch/DBI` directory on your SD card.
2. Create a **notUltraNX** account.
3. Launch **DBI** and select **Просмотр HTTP/FTP/Github сервера...**
4. Enter `https://dbi.ultranx.ru/link/login/password` (replace *login* and *password* with your credentials) and press **+**.
5. If everything is done correctly, you will see a relevant success message. Now you can download games directly from the notUltraNX repository.

***

*Disclaimer: This tutorial is intended purely for educational and homebrew asset optimization purposes. Always ensure you are utilizing your legally obtained backup libraries.*
