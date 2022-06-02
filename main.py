"""Main"""
from os import environ
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from actions import click_save_job

CHROMIUM_PATH = 'C:/Programs/chromedriver/chromedriver'
EMAIL = environ.get('EMAIL')
PASSWORD = environ.get('LINKEDIN_PASSWORD')
URL = 'https://www.linkedin.com/'
JOBS_TO_SAVE = 10

# set up browser
wd = webdriver.Chrome(CHROMIUM_PATH)
wd.implicitly_wait(5)
wd.set_window_size(1200, 1024)

# open linkedin
wd.get(URL)

# login
WebDriverWait(wd, 10).until(
    EC.presence_of_element_located((By.ID, 'session_key')))
wd.find_element('id', 'session_key').send_keys(EMAIL)
wd.find_element('id', 'session_password').send_keys(PASSWORD)
wd.find_element(By.CSS_SELECTOR, 'button.sign-in-form__submit-button').click()

# go to jobs search filtered page (if you want other filters just select them
# and copy the url)
wd.get(URL + 'jobs/search/?f_E=2%2C3%2C4&f_JT=F%2CP%2CC%2CT&f_TPR=r604800&f\
_WT=2&geoId=106057199&keywords=product%20manager&location=Worldwide&sortBy=DD')

# loop through n jobs
counter = 1
for n in range(JOBS_TO_SAVE):
    wd.find_element(By.XPATH, f"//section[1]/div/div/ul/li[{counter}]").click()
    counter += 1
    click_save_job(wd)
