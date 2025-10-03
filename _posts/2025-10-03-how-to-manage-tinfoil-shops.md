---
layout: post
title: "How to Manage Shops in Tinfoil (Add, Remove, and Disable)"
date: 2025-10-03
categories: guides how-to apps
---

One of Tinfoil's most powerful features is its ability to connect to network sources, commonly known as "shops." These sources allow you to browse and download content directly to your Switch without needing a PC. But how do you control which sources Tinfoil uses?

This guide will walk you through the complete process of managing your shops: adding new ones, deleting those you no longer use, and temporarily disabling them.

**Disclaimer:** This guide is for educational purposes. You are responsible for the sources you add to Tinfoil. Ensure you only use this functionality to access legally owned content and backups.

### The Hub: Tinfoil's File Browser

Almost all shop management is done from one place: the **File Browser** tab in Tinfoil. Navigate to this tab using the 'L' and 'R' shoulder buttons on your controller. This is your command center for managing sources.

---

### How to Add (Install) a New Shop

Adding a new source is a simple process of entering its address details.

1.  Launch Tinfoil and navigate to the **File Browser** tab.
2.  Press the **`-` (minus)** button on your left Joy-Con. This will open the "Add New Location" window.
3.  You will see several fields. Use the on-screen keyboard to fill them out:
    * **Protocol:** The connection type. This is usually `https` or `http`.
    * **Host:** The main address of the source (e.g., `opennx.github.io`).
    * **Path:** The specific path to the shop's file on the server (e.g., `/folder/shop.json`). This may sometimes be left blank.
    * **Title:** A friendly nickname for the shop so you can easily recognize it (e.g., "My Awesome Shop").
4.  Once all the information is entered correctly, select **"Save"**.

Tinfoil will connect to the source. If successful, you will see your new shop listed in the File Browser, and its content will begin to populate the "New Games" and other tabs.

---

### How to Remove (Delete) a Shop

If a shop is no longer working or you simply don't want it anymore, you can permanently delete it.

1.  Navigate to the **File Browser** tab.
2.  Use the D-pad to move up and down, and highlight the shop you wish to delete.
3.  Press the **`X` button**.
4.  A confirmation dialog will appear. Confirm that you want to delete the location.

The shop will be permanently removed from your list.

---

### How to Disable and Re-enable a Shop

Sometimes you don't want to delete a shop, but you want to temporarily hide its contents or stop Tinfoil from checking it. Disabling is the perfect solution.

1.  Navigate to the **File Browser** tab.
2.  Highlight the shop you wish to disable.
3.  Press the **`Y` button**. You will notice the entry for the shop turns grey and is marked as disabled.
4.  Tinfoil will no longer pull content from this source.

To **re-enable** a disabled shop, simply highlight it again and press the **`Y` button**. It will become active again.

---

### Pro Tip: Managing Shops Manually

All of your saved shop locations are stored in a simple text file on your SD card at the following location:

`/switch/tinfoil/locations.conf`

Advanced users can back up this file or even edit it directly on a PC using a text editor to manage their list of sources.

By mastering these simple commands in the File Browser, you can take full control over your Tinfoil sources.
