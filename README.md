### Discontinuation note

> As of Whatsapp Web version 2.2114 this script is **broken**. For details see [#3](https://github.com/ErikTschierschke/WhatsappMonitor/issues/3#issuecomment-826085792).

<br><br>

[![Python 3.8](https://img.shields.io/badge/Python-3.8-blue.svg?style=flat-square)](http://www.python.org/download/)

# WhatsappMonitor

## About
 WhatsappMonitor monitors the online times of selected contacts and displays them as a graph.
It's original purpose was to show how even tiny pieces of personal information like whether you're using Whatsapp just now can become scarily powerful if it's collected and evaluated.
Running this script for an extended period of time can give sensitive knowledge about personal behavior of the monitored contacts like sleep routines, work times and correspondence with others.

## Installation
#### Install WhatsappMonitor
    git clone https://github.com/ErikTschierschke/WhatsappMonitor.git
    cd WhatsappMonitor
    pip install -r requirements.txt
#### Install geckodriver
> On Linux you can run `sudo gecko-install.sh` to automatically install geckodriver.

Download [geckodriver](https://github.com/mozilla/geckodriver/releases) for your operating system and extract it to a PATH directory (e.g. linux: /usr/bin, win: C:\Windows\)
#### Run WhatsappMonitor

    python3 whatsappmonitor.py

## Warning!
- Running this script without informing the monitored contacts is ethically questionable. You should only use it for scientific purposes on privy contacts.

- The script **violates** Whatsapp's [**Terms of Service**](https://www.whatsapp.com/legal/#terms-of-service). Running it may result in the account being disabled. Never run it on your primarily used account.

- The script causes some side effects to the used Whatsapp account:
  - The used account will be **online** itself the whole time.
  - **Messages received** by monitored contacts will be marked as "**read**" for them (blue ticks) and may not generate "new message" notifications on your phone.

### Disclaimer
Running this script is at own risk and **without any liability**.

