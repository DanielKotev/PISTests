import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.common.keys import Keys


class registerTestCases(unittest.TestCase):
    def test_succsesfulRegister(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(5))
        email = username + "@a.com"
        password = ''.join(random.choice(letters) for i in range(8))

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "confirm_password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

    def test_shortUsername(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = 'a'
        email = username + "@a.com"
        password = ''.join(random.choice(letters) for i in range(8))

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "confirm_password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

    def test_tooLongUsername(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(21))
        email = username + "@a.com"
        password = ''.join(random.choice(letters) for i in range(8))

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "confirm_password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

    def test_invalidEmail(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(5))
        email = username + "@.com"
        password = ''.join(random.choice(letters) for i in range(8))

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "confirm_password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

    def test_tooShortPassword(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(5))
        email = username + "@a.com"
        password = ''.join(random.choice(letters) for i in range(4))

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "confirm_password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

    def test_tooLongPassword(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(5))
        email = username + "@a.com"
        password = ''.join(random.choice(letters) for i in range(11))

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "confirm_password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

    def test_notMatchingPasswords(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(5))
        email = username + "@a.com"
        password = ''.join(random.choice(letters) for i in range(8))

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "confirm_password").send_keys("password")
        driver.find_element(By.NAME, "submit").click()

    def test_blankUsername(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(5))
        email = username + "@a.com"
        password = ''.join(random.choice(letters) for i in range(8))

        driver.find_element(By.NAME, "username").send_keys("")
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "confirm_password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

    def test_blankemail(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(5))
        email = username + "@a.com"
        password = ''.join(random.choice(letters) for i in range(8))

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "email").send_keys("")
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "confirm_password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()

    def test_blankPassword(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("http://127.0.0.1:5000/register ")
        driver.maximize_window()

        letters = string.ascii_lowercase
        username = ''.join(random.choice(letters) for i in range(5))
        email = username + "@a.com"
        password = ''.join(random.choice(letters) for i in range(8))

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys("")
        driver.find_element(By.NAME, "confirm_password").send_keys("")
        driver.find_element(By.NAME, "submit").click()


if __name__ == "__main__":
    unittest.main()
