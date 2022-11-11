from selenium import webdriver

path = '/Users/a/Library/Mobile Documents/com~apple~CloudDocs/Development/chromedriver'
driver = webdriver.Chrome(executable_path=path)
URL = 'https://www.python.org/'

# driver.get('https://www.amazon.com/Industrial-Standing-Footswitch-Bedroom-Minimalist/dp/B08F52QFB2/ref=sr_1_27_sspa?crid=31LQ7RES56V90&keywords=floor%2Blamp%2Bmodern&qid=1668034275&sprefix=floor%2Blamp%2Bmoden%2Caps%2C176&sr=8-27-spons&th=1')
# price_beg = driver.find_element(by='class name', value="a-price-whole")
# price_dec = driver.find_element(by='class name', value='a-price-fraction')
# price = float(f'{price_beg.text}.{price_dec.text}')
# print(price)
#
# driver.quit()


# Coding Challenge Selenium

driver.get(URL)
dates = driver.find_elements(by='xpath', value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

for event in dates:
    event_list = event.text.splitlines()


dict1 = {i: {'time': event_list[i], 'name': event_list[i + 1]} for i in range(0, len(event_list), 2)}

print(dict1)

driver.quit()