import traceback

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import contacts
import monitor

__version__ = 'v1.2'


def intro():
    print('WhatsappMonitor ' + __version__)
    print('Github:\thttps://github.com/ErikTschierschke/WhatsappMonitor/')
    print('\n')
    print('Warning: Running this script will have side effects on your Whatsapp account. See '
          'https://github.com/ErikTschierschke/WhatsappMonitor/blob/master/README.md#warning for more information.')
    print('Press RETURN to continue.')
    input()

    print('Please use your smartphone to scan the Whatsapp Web QR code.')


if __name__ == '__main__':
    intro()

    browser = None
    try:
        browser = webdriver.Firefox()
    except WebDriverException:
        print('An error occurred while executing the script.\n\n'
              "Most likely this is because the script didn't find either geckodriver or Firefox.\n"
              'If both are properly installed and this error continues to occur please create an issue at '
              'https://github.com/ErikTschierschke/WhatsappMonitor/issues including the following message:\n'
              + traceback.format_exc())
        quit(2)
    browser.get('https://web.whatsapp.com/')

    img_phone = '/html/body/div[1]/div/div/div[4]/div/div/div[1]'

    try:
        WebDriverWait(browser, 500).until(ec.presence_of_element_located((By.XPATH, img_phone)))
        monitor.start(contacts.select_contacts(browser), browser)
    except WebDriverException:
        print('An error occurred while executing the script.\n\n'
              'Most likely this is because you closed the browser window.\n'
              'If that\'s not the case please create an issue at '
              'https://github.com/ErikTschierschke/WhatsappMonitor/issues including the following message:\n'
              + traceback.format_exc())
        quit(1)
