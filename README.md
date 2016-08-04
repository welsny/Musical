## *Musical* 

Identify musical chords on guitar, ukulele, and more:

###### Guitar
```bash
python musical.py x21202

> B dom7
```

-

###### Uke

```bash
python musical.py x333

> C min
```

-

###### "More"
```bash
python musical.py CEGB

> C Maj7
```

---

#### Install

Clone this repositiory and run:
```
pip install -r requirements.txt
```

-

I highly recommend using a [terminal alias](http://www.techradar.com/us/how-to/computing/apple/terminal-101-creating-aliases-for-commands-1305638) to improve usability:

```bash
chord xx5777

> G Maj7
```

---

#### Notes


* This project also includes a sample GUI interface implemented with [TkInter](https://wiki.python.org/moin/TkInter). 
  * To open, enter `python sample_gui_app.py` into your terminal. 
  * Fonts are optimized for Ubuntu, and currently do *not* look good on Mac OS X. 
  * TODO: Switch to [React Native Desktop](https://github.com/ptmt/react-native-desktop)

* The chord-identifying algorithm supports many commonly-used chord qualities, but not *all* of them - in particular the more obscure/uncommon ones. 
  * Support for more exotic chord qualities will be added *Soon™*

---

#### Tests

```
./tests.py
```

-

Pull requests are welcome. Thank you for reading!

:smile::violin::notes::notes:
