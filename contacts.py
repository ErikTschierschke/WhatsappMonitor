import re
import sys
import time

select_pattern = re.compile(r'^\d+(?:\s+\d+)*$')

contact_dict = {}
selected = False


def select_contacts(browser):
    browser.set_window_position(-3000, 0)
    time.sleep(2)
    contacts = browser.find_elements_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/child::*')
    print('Indexing contacts. This may take some time.')
    amount = len(contacts)
    i = 1
    for contact in contacts:
        contact.click()
        if is_not_group(browser):
            contact_dict[len(contact_dict)] = contact
        sys.stdout.write('Indexing contacts...  [' + str(i) + '/' + str(amount) + ']\r')
        i += 1

    return get_input()


def get_input():
    global selected

    print('Found ' + str(len(contact_dict)) + ' contacts:                     \n')
    show_contacts()
    print('\nPlease select the contacts to monitor by typing their numbers separated by spaces or "a[ll]":')

    while True:
        selection = input('Contacts to monitor:\t')
        if selection.casefold() == 'a' or selection.casefold() == 'all':
            selected = True
            break
        elif re.match(select_pattern, selection):
            selected = selection.split(' ')
            input_to_high = False
            for num in selected:
                if int(num) >= len(contact_dict):
                    print('There is no contact ' + num + '. Please try again.')
                    input_to_high = True
            if not input_to_high:
                break
        else:
            print('Error reading selection. Please enter e.g. "a" or "1 3 12"')
    print()
    selection_list = list()
    if type(selected) == bool:
        selection_list = list(contact_dict.values())
    else:
        for num in selected:
            num = int(num)
            contact = contact_dict.get(num)
            if contact not in selection_list:
                selection_list.append(contact)
    return selection_list


def show_contacts():
    for i in range(len(contact_dict)):
        name = contact_dict.get(i).find_element_by_xpath('.//div/div/span/span').text
        print('\t\t[' + str(i) + ']\t' + name)


def is_not_group(browser):
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]').click()
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/span/div/ul/li[1]/div').click()

    return not bool(browser.find_elements_by_xpath(
        '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[2]/div[1]/span[2]/div'))
