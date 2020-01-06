import sys
import time
from datetime import datetime as dt

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

import data

running = False


def start(contacts, browser):
    global running
    running = True
    start_time = dt.now()
    contacts_len = len(contacts)
    try:
        while True:
            for contact in contacts:
                if not running:
                    continue
                sys.stdout.write('[' + str(time_running(start_time)) + '] Monitoring ' + str(contacts_len)
                                 + " contact(s).\t-\tPress Ctrl + C to finish.\r")
                name = contact.find_element_by_xpath('.//span[@class="_19RFN _1ovWX _F7Vk"]').text
                WebDriverWait(browser, 500).until(ec.element_to_be_clickable((By.XPATH,
                                                                              './/span[@class="_19RFN _1ovWX _F7Vk"]')))
                contact.click()
                time.sleep(2)
                if is_online(browser):
                    data.get(name).set_online()
                elif not is_online(browser):
                    data.get(name).set_offline()
    except KeyboardInterrupt:
        print('\r\n[' + str(time_running(start_time)) + '] '
                                                        'Monitoring finished.                                         ')
        data.finish(start_time)


def finish():
    global running
    running = False


def is_online(browser):
    if not browser.find_elements_by_xpath('.//span[@class="_315-i _F7Vk"]'):
        return False
    elif browser.find_element_by_xpath('.//span[@class="_315-i _F7Vk"]').text == "online":
        return True
    else:
        return False


def time_running(start_time):
    run_time = dt.now() - start_time
    hours, r = divmod(run_time.seconds, 3600)
    minutes, seconds = divmod(r, 60)
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
