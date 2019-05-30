from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException, NoSuchElementException, ElementNotVisibleException
import random
import time


def add_links(xpath, array):
    for i in driver.find_elements_by_xpath(xpath):
        array.append(i.get_attribute('href'))
    return array


if __name__ == '__main__':
    Sections = []
    Subsections = []
    Items = []
    H3 = []
    driver = webdriver.Chrome(executable_path= '../drivers/chromedriver')
    a = True
    driver.get('https://rozetka.com.ua/')
    driver.find_element_by_link_text("Все категории").click()
    add_links('//a[@name="all-cat-i"]', Sections)
    add_links('//li[@class="all-cat-b-l-i"]/a', Subsections)
    # print(Sections)
    # print(Subsections)
    Sections.extend(Subsections)
    while a:
        driver.get(random.choice(Sections))
        try:
            driver.find_elements_by_xpath('//div[@name="price"]')
            time.sleep(2)
        except NoSuchElementException:
            try:
                add_links('//div[@class="pab-table"]/p[@class="h3 pab-h3"]/a', H3)
                print(H3)
                driver.get(random.choice(H3))
            except NoSuchElementException:
                continue
        try:
            driver.find_element_by_xpath('//div[@id="sort_price"]')
        except NoSuchElementException:
            driver.get(random.choice(Sections))
        min_price = driver.find_element_by_xpath('//div[@id="sort_price"]').find_elements_by_tag_name('input')[0]
        driver.execute_script(f"arguments[0].value = '{100}';", min_price)
        driver.find_element_by_xpath('//div[@id="sort_price"]').find_elements_by_tag_name('input')[1].send_keys('2000')
        driver.find_element_by_id('submitprice').click()
        time.sleep(1)
        try:
            driver.find_element_by_xpath(
                '//div[@param="strana-proizvoditelj-tovara-90098"]/div/a[@name="show_more_parameters"]').click()
            driver.find_element_by_css_selector('#filter_strana-proizvoditelj-tovara-90098_544338').click()
        except ElementClickInterceptedException:
            continue
        except NoSuchElementException:
            continue
        time.sleep(4)
        add_links('//div[@class="g-i-tile-i-title clearfix"]/a', Items)
        # print(Items)
        driver.get(random.choice(Items))
        # driver.find_element_by_link_text('Купить').click()
        time.sleep(6)
        try:
            driver.find_element_by_xpath(
            '//span[@class="btn-link btn-link-green detail-buy-btn"]').click()
        except NoSuchElementException:
            continue
        time.sleep(1)
        driver.find_element_by_xpath(
            '//div[@class="cart-check"]/button[@class="btn-link-green btn-link cart-check-button"]').click()
        driver.find_element_by_id('reciever_name').send_keys('Даша Житанская')
        driver.find_element_by_id('reciever_phone').send_keys('380654583212')
        driver.find_element_by_id('reciever_email').send_keys('dasha.zhitanska@ukr.net')
        time.sleep(3)
        driver.find_element_by_xpath('//span[@class="btn-link btn-link-green check-step-btn-link opaque"]/button[@class="btn-link-i"]').click()
        driver.find_element_by_xpath('//div[@class="check-method-subl-select"]/div/a[@name="pickups_drop_link"]').click()
        try:
            Places = driver.find_elements_by_xpath('//div[@class="check-method-subl-select"]/div/div[@class="pickups-select-suggest-wrap"]/div[@class="pickups-select-dropdown-wrap"]/div/ul/li[@class="pickups-select-dropdown-l-i"]/a')
            random.choice(Places).click()
        except ElementNotVisibleException:
            Places_input = driver.find_elements_by_css_selector('.check-address-l>li')
            time.sleep(2)
            random.choice(Places_input).click()
        try:
            driver.find_element_by_xpath('//input[@data-title="Фамилия"]').send_keys('Даша')
            driver.find_element_by_xpath('//input[@data-title="Имя"]').send_keys('Житанская')
        except ElementNotInteractableException:
            pass
        time.sleep(3)
        last_button = driver.find_element_by_css_selector('#make-order.btn-link-i')
        color = last_button.value_of_css_property('color')
        if color == 'rgba(255, 255, 255, 1)':
            print("Button is enabled!")
        a = False
        driver.close()



