import traceback

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import contacts
import monitor

__version__ = 'v1.0'


def intro():
    print('WhatsappMonitor ' + __version__)
    print('Github:\thttps://github.com/ErikTschierschke/WhatsappMonitor/')
    print('\n')
    print('Warning: Running this script will have side effects on your Whatsapp account. See '
          'https://github.com/ErikTschierschke/WhatsappMonitor/README.md#warning! for more informstion.')
    print('Press RETURN to continue.')
    input()

    print('Please use your smartphone to scan the Whatsapp Web QR code.')


if __name__ == '__main__':
    intro()

    browser = None
    try:
        browser = webdriver.Firefox()
    except WebDriverException:
        print('geckodriver was not found. Please install it manually or run the install-gecko script.')
        quit(2)
    browser.get('https://web.whatsapp.com/')

    img_phone = '//div[@class="HGVhc"]'
    WebDriverWait(browser, 500).until(ec.presence_of_element_located((By.XPATH, img_phone)))
    try:
        monitor.start(contacts.select_contacts(browser), browser)
    except WebDriverException:
        print('An error occurred while executing the script.\n\n'
              'Most likely this is because you closed the browser window.\n'
              'If that\'s not the case please create an issue at '
              'https://github.com/ErikTschierschke/WhatsappMonitor/issues including the following message:\n'
              + traceback.format_exc())
        quit(1)
