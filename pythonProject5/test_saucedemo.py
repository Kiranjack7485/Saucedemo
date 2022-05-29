import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = None
def test_title():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverManager().install())

    driver.get(" https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@name='login-button']").click()
    time.sleep(3)

    drop = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
    drop.select_by_value("lohi")
    time.sleep(3)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(3)
    driver.find_element(By.ID, "checkout").click()
    time.sleep(3)
    driver.find_element(By.NAME, "firstName").send_keys("Tom")
    driver.find_element(By.NAME, "lastName").send_keys("Cruise")
    driver.find_element(By.NAME, "postalCode").send_keys("560040")
    time.sleep(3)
    driver.find_element(By.NAME, "continue").click()
    time.sleep(3)
    driver.find_element(By.ID, 'finish').click()
    print(driver.title)

def test_assert():
    my_str = driver.find_element(By.XPATH, "//span[@class='title']").text
    act_str = "CHECKOUT: COMPLETE!"
    assert my_str == act_str

def test_assert2():
    my_str2 = driver.find_element(By.XPATH, "//h2[@class='complete-header']").text
    act_str2 = "THANK YOU FOR YOUR ORDER"
    assert my_str2 == act_str2

def test_assert3():
    my_str3 = driver.find_element(By.XPATH, "//div[@class='complete-text']").text
    act_str3 = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    assert my_str3 == act_str3









