"""Automated actions on linkedin"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException as Stale
from selenium.common.exceptions import NoSuchElementException as NoSuch
from selenium.webdriver.common.by import By


def click_job(counter: int, webd: webdriver):
    try:
        WebDriverWait(webd, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//section[1]/div/div/ul/li[{counter}]')))

        webd.find_element(By.XPATH,
                          f'//section[1]/div/div/ul/li[{counter}]').click()

    except (Stale, NoSuch):
        webd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(webd, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//section[1]/div/div/ul/li[{counter}]')))

        webd.find_element(By.XPATH,
                          f'//section[1]/div/div/ul/li[{counter}]').click()


def click_save_job(webd: webdriver):
    """Click to save the job for future use
    and dismiss the popup"""
    try:
        WebDriverWait(webd, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class=\
"jobs-unified-top-card__content--two-pane"]//button/span[text()="Save"]')))

        webd.find_element(
            By.XPATH, '//div[@class="jobs-unified-top-card__content--two-pane"]//\
button/span[text()="Save"]').click()

    except (Stale, NoSuch):
        WebDriverWait(webd, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class=\
"jobs-unified-top-card__content--two-pane"]//button/span[text()="Save"]')))

        webd.find_element(
            By.XPATH, '//div[@class="jobs-unified-top-card__content--two-pane"]//\
button/span[text()="Save"]').click()

    finally:
        webd.find_element(By.XPATH,
                          '//div[@class="artdeco-toast-item artdeco-toast-item--visible \
ember-view"]/*/li-icon[@type="cancel-icon"]').click()
