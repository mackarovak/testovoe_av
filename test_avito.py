import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Конфигурация
BASE_URL = "http://tech-avito-intern.jumpingcrab.com"

# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Selenium Manager автоматически найдет драйвер
    driver.get(BASE_URL)
    yield driver
    driver.quit()

# Тест на создание объявления
def test_create_advertisement(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "create-ad-button"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "title"))).send_keys("Тестовое объявление")
    driver.find_element(By.ID, "description").send_keys("Это тестовое описание")
    driver.find_element(By.ID, "price").send_keys("1000")
    driver.find_element(By.ID, "publish-button").click()
    assert "Тестовое объявление" in driver.page_source

# Тест на редактирование объявления
def test_edit_advertisement(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Тестовое объявление')]"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "edit-button"))).click()
    title_field = wait.until(EC.presence_of_element_located((By.ID, "title")))
    title_field.clear()
    title_field.send_keys("Обновленное объявление")
    driver.find_element(By.ID, "save-button").click()
    assert "Обновленное объявление" in driver.page_source

# Тест на поиск объявлений
def test_search_advertisement(driver):
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "search-box")))
    search_box.send_keys("Обновленное объявление")
    search_box.send_keys(Keys.RETURN)
    assert "Обновленное объявление" in driver.page_source

# Тест на сортировку объявлений
def test_sort_advertisement(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "sort-by-date"))).click()
    advertisements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "advertisement-title")))
    assert len(advertisements) > 0

# Тест на просмотр карточки объявления
def test_view_advertisement(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Обновленное объявление')]"))).click()
    assert "Обновленное объявление" in driver.page_source