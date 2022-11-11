from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
path = '/Users/a/Library/Mobile Documents/com~apple~CloudDocs/Development/chromedriver'
driver = webdriver.Chrome(executable_path=path, options=options)
URL = 'https://orteil.dashnet.org/cookieclicker/'

driver.get(URL)
time.sleep(6)
# link = driver.find_element(by='xpath', value='//*[@id="articlecount"]/a[1]')
# link.click()

# fname = driver.find_element('name', 'fName')
# fname.send_keys('Akintoye')
#
# lname = driver.find_element('name', 'lName')
# lname.send_keys('Adesomoju')
#
# email = driver.find_element('name', 'email')
# email.send_keys('randomemail@gmail.com')
#
# submit = driver.find_element('tag name', 'button')
# submit.click()

timer_check = 15  # 15 seconds to wait
second_refresh = time.time() + timer_check
seconds = 60 * 5
wait_mins_1 = time.time() + 60 * 5  # 5 mins
wait_mins_2 = time.time() + 60 * 10  # 10 mins
wait_mins_3 = time.time() + 60 + 15  # 15 mins
start_time = time.time()

english = driver.find_element('id', 'langSelect-EN')
english.click()
time.sleep(6)
cookie_click = driver.find_element('id', 'bigCookie')
amount_of_cookies = driver.find_element('id', 'cookies').text.split('\n')
golden_cookie_count = 0

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    cookie_click.click()

    # if there is a golden cookie
    try:
        golden_cookie = driver.find_element('class name', 'shimmer')
        golden_cookie.click()
        golden_cookie_count += 1
    except:
        pass

    # main body
    if time.time() > second_refresh:

        for n in range(8, -1, -1):
            try:
                upgrades = driver.find_element('id', f'upgrade{n}')
                upgrades.click()
            except:
                pass

        for n in range(19, -1, -1):
            try:
                product = driver.find_element('id', f'product{n}')
                check_class = product.get_attribute('class')
                while check_class == 'product unlocked enabled':
                    product.click()
                    check_class = product.get_attribute('class')
            except:
                pass

        timeoout = time.time() + timer_check

    if elapsed_time > wait_mins_1:
        timer_check = 30

    if elapsed_time > wait_mins_2:
        timer_check = 60

    if elapsed_time > wait_mins_3:
        timer_check = 120

    if elapsed_time > seconds:
        cookies_per_second = int(amount_of_cookies[1].split(' ')[2])
        print(f'Cookies per second: {cookies_per_second}')
        print(f'Golden cookies clicked: {golden_cookie_count}')

        break

driver.quit()
