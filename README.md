[![Deploy GitHub Pages](https://github.com/OpenNX/opennx.github.io/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/OpenNX/opennx.github.io/actions/workflows/jekyll-gh-pages.yml)
![GitHub Repo stars](https://img.shields.io/github/stars/OpenNX/opennx.github.io)
![GitHub watchers](https://img.shields.io/github/watchers/OpenNX/opennx.github.io)


### Tinfoil shop forwarder filled with .json file link to the latest active and working tinfoil shops. 

Built with the [Tinfoil Documentation](https://blawar.github.io/tinfoil/custom_index/).

If you find this tool useful, please consider starring our repository: [Star on Github](https://github.com/OpenNX/opennx.github.io) 

To check which tinfoil shops are working now, go to [this repository](https://github.com/melogabriel/tinfoil-shops-status).

If you have any shops to add, open an [issue](https://github.com/OpenNX/opennx.github.io/issues/new/choose) or make a [pull request](https://github.com/OpenNX/opennx.github.io/pulls).

<a href="https://www.buymeacoffee.com/gabrielmelo" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

> *NOTE:*
> **Open NX** acts solely as a forwarding service and is not responsible for the quality, safety, legality, or delivery of products from third-party shops.
               
___

## Shop Links

To add shops to Tinfoil go to Tinfoil > File Browser > Press - New > Fill the fields with the information about the [shop](https://github.com/OpenNX/opennx.github.io/edit/main/README.md#open-nx). 

![image](https://github.com/user-attachments/assets/91d3fddf-74a6-46fe-8a0b-b3de94e7646a)



## [Open NX](https://github.com/OpenNX/opennx.github.io)

This repositories installs a package with the shops below. Adding this one should be enough and recommended for your game library.

```
Protocol: https
Host: opennx.github.io
Path: tinfoil.json
Title: Open NX
```

## Current Shops in Open NX:

### Ghost eShop
```
Protocol: https
Host: nx.ghostland.at
Title: Ghost eShop PUBLIC
```
### Ghost eShop RETRO
```
Protocol: https
Host: nx-retro.ghostland.at
Title: Ghost eShop RETRO
```

### Gandalf eShop
```
Protocol: https
Host: gandalfsax.com
Title: Gandalf eShop
```

### SwitchBR
```
Protocol: http
Host: switchbr.com
Title: SwitchBR
```

### World Digital
```
Protocol: https
Host: free.worldigital-brasil.com
Port: 443
Path: /
Title: world digital
```

### NX Shared Saves
This shop contains modified save files that are installable on many games.
```
Protocol: https
Host: nx-saves.ghostland.at
Title: NX Shared Saves
```

### Egg Fried Rize Shop
```
Protocol: https
Host: cyrilz87.net
Title: Egg Fried Rice Shop
```

### Ultra NX
```
Protocol: https
Host: tinfoil.ultranx.ru
Path:/tinfoil
Title: Ultra NX
```



### Backup of Shops with various Functions
```
# JITS (works with your own GDrive if you follow https://games.jits.cc/account#instructions)
Protocol: https
Host: games.jits.site
Path: shop
Title: JITS
```

### Ecchi's Firmware Archives (download all of switch firmware from Tinfoil)
```
Protocol: https
Host: e.cchi.me
Path: firmware.tfl
Title: EFA
```

### Ecchi's Archives (download save files and install them to your Switch [auto added by Tinfoil] )
```
Protocol: https
Host: e.cchi.me
Title: ESA
```

## Requirements

* Nintendo Switch running CFW ([Atmosphere](https://github.com/Atmosphere-NX/Atmosphere/releases) with [Sigpatches](https://github.com/ITotalJustice/patches/releases) recommended).

* Relies on [Tinfoil](https://tinfoil.io).

* You are recommended to DELETE the current Tinfoil locations.conf [switch/tinfoil/locations.conf] from your SD card before adding server.

* To avoid getting banned make sure you have already setup [Exosphere / DNS MITM](https://rentry.org/ExosphereDNSMITM).

#### You have to set up OAuth if you cannot download  「something」  from Tinfoil.
* Follow the Guide to set up: https://bit.ly/38HEr48.

## FAQ

Q: Why aren't the shops loaded?

> A: This usually occurs when the time of your Switch does not the same as the real-time. Please use [switch-time](https://github.com/3096/switch-time) to adjust the time of your Switch. Another circumstance might be that the shops you are trying to access could be down currently.


Q: I can't open tinfoil... :(

> A: Make sure that you install the latest [Sigpatches](https://github.com/ITotalJustice/patches/releases/latest) in your switch and are booting with fusee.bin instead of Hekate. Then try to reinstall tinfoil.


Q: Network Error 7 occurs when I try to download.

> A: It is most commonly a poor network connection. If you are using a LAN cable, try reinserting it.


### Software Developers
___

* [Blawar](https://github.com/blawar)

* [Tinfoil Official Website](https://tinfoil.io)

---

## Legal Disclaimer

> The author does not take any responsibility for your actions using this service.

> The author is NOT affiliated with the content that you can retrieve thanks to any Tinfoil shop.


## Also check out:

> [orn8/tinfoil](https://github.com/orn8/tinfoil) and [carcaschoi/tinfoil-json](https://github.com/carcaschoi/tinfoil-json) - The inspiration for this project.

> [Ghost eShop Wiki](https://wiki.ghosteshop.com/docs/category/nx--nintendo-switch) - Contains a lot of information, from how to operate Ghost eShop, to their very useful troubleshooting pages.

