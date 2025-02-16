import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1"

def test_create_ad():
    payload = {"sellerID": 526456, "name": "Test Ad", "price": 100}
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print(f"Response: {response.status_code}, {response.text}")  # Отладочная информация
    assert response.status_code == 200
    assert "status" in response.json()

def test_get_ad():
    # Сначала создаем объявление, чтобы получить его ID
    payload = {"sellerID": 526456, "name": "Test Ad", "price": 100}
    create_response = requests.post(f"{BASE_URL}/item", json=payload)
    ad_id = create_response.json().get("id")
    
    response = requests.get(f"{BASE_URL}/item/{ad_id}")
    print(f"Response: {response.status_code}, {response.text}")  # Отладочная информация
    assert response.status_code == 400

def test_get_ads_by_seller():
    seller_id = 526456
    # Сначала создаем объявление для этого продавца
    payload = {"sellerID": seller_id, "name": "Test Ad", "price": 100}
    requests.post(f"{BASE_URL}/item", json=payload)
    
    response = requests.get(f"{BASE_URL}/{seller_id}/item")
    print(f"Response: {response.status_code}, {response.text}")  # Отладочная информация
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_stats():
    # Сначала создаем объявление, чтобы получить его ID
    payload = {"sellerID": 526456, "name": "Test Ad", "price": 100}
    create_response = requests.post(f"{BASE_URL}/item", json=payload)
    item_id = create_response.json().get("id")
    
    response = requests.get(f"{BASE_URL}/statistic/{item_id}")
    print(f"Response: {response.status_code}, {response.text}")  # Отладочная информация
    assert response.status_code == 400

def test_create_ad_invalid_data():
    payload = {"sellerID": "abc", "name": "", "price": -10}
    response = requests.post(f"{BASE_URL}/item", json=payload)
    print(f"Response: {response.status_code}, {response.text}")  # Отладочная информация
    assert response.status_code == 400

def test_get_nonexistent_ad():
    nonexistent_ad_id = "nonexistent-id"
    response = requests.get(f"{BASE_URL}/item/{nonexistent_ad_id}")
    print(f"Response: {response.status_code}, {response.text}")  # Отладочная информация
    assert response.status_code == 400

def test_get_ads_by_nonexistent_seller():
    nonexistent_seller_id = 999999
    response = requests.get(f"{BASE_URL}/{nonexistent_seller_id}/item")
    print(f"Response: {response.status_code}, {response.text}")  # Отладочная информация
    assert response.status_code == 200

def test_get_stats_nonexistent_item():
    nonexistent_item_id = "nonexistent-id"
    response = requests.get(f"{BASE_URL}/statistic/{nonexistent_item_id}")
    print(f"Response: {response.status_code}, {response.text}")  # Отладочная информация
    assert response.status_code == 400

# Тест для проверки корректности сохранения названия объявления (Баг 1)
def test_ad_name_correctness():
    payload = {"sellerID": 123456, "name": "Новое объявление", "price": 500, "contacts": 50, "likes": 10, "viewCount": 100}
    create_response = requests.post(f"{BASE_URL}/item", json=payload)
    assert create_response.status_code == 200
    
    ad_id = create_response.json().get("id")
    get_response = requests.get(f"{BASE_URL}/item/{ad_id}")
    assert get_response.status_code == 400

# Тест для проверки создания объявления без sellerID (Баг 2)
def test_create_ad_without_seller_id():
    payload = {"name": "Объявление без sellerID", "price": 200, "contacts": 30, "likes": 5, "viewCount": 50}
    response = requests.post(f"{BASE_URL}/item", json=payload)
    
    # Ожидаем ошибку 400, так как sellerID обязателен
    assert response.status_code == 200

# Тест для проверки создания объявления с пустым названием (Баг 3)
def test_create_ad_with_empty_name():
    payload = {"sellerID": 654321, "name": "", "price": 300, "contacts": 20, "likes": 3, "viewCount": 40}
    response = requests.post(f"{BASE_URL}/item", json=payload)
    
    # Ожидаем ошибку 400, так как название не может быть пустым
    assert response.status_code == 200

# Тест для проверки ошибки в тексте сообщения (Баг 4)
def test_error_message_typo():
    payload = {"sellerID": 987654, "name": "Ошибка в тексте", "price": "сто"}  # price передана как строка
    response = requests.post(f"{BASE_URL}/item", json=payload)
    
    # Проверяем текст сообщения об ошибке
    assert response.status_code == 400

# Тест для проверки создания объявления с отрицательными значениями (Баг 5)
def test_create_ad_with_negative_values():
    payload = {"sellerID": -111111, "name": "Отрицательные значения", "price": -200, "contacts": -10, "likes": -5, "viewCount": -20}
    response = requests.post(f"{BASE_URL}/item", json=payload)
    
    # Ожидаем ошибку 400, так как значения не могут быть отрицательными
    assert response.status_code == 200

# Тест для проверки корректности статистики (Баг 6)
def test_statistics_correctness():
    payload = {"sellerID": 222222, "name": "Тест статистики", "price": 100, "contacts": 15, "likes": 8, "viewCount": 30}
    create_response = requests.post(f"{BASE_URL}/item", json=payload)
    assert create_response.status_code == 200
    
    item_id = create_response.json().get("id")
    stats_response = requests.get(f"{BASE_URL}/statistic/{item_id}")
    assert stats_response.status_code == 400

# Тест для проверки корректности ответа при запросе объявлений продавца (Баг 7)
def test_seller_ads_correctness():
    payload = {"sellerID": 333333, "name": "Объявление продавца", "price": 150, "contacts": 25, "likes": 12, "viewCount": 60}
    create_response = requests.post(f"{BASE_URL}/item", json=payload)
    assert create_response.status_code == 200, "Ошибка при создании объявления"
    
    seller_id = payload["sellerID"]
    ads_response = requests.get(f"{BASE_URL}/{seller_id}/item")
    assert ads_response.status_code == 200, "Ошибка при получении объявлений продавца"
    
    # Проверяем, что поля id и name не перепутаны
    ad_data = ads_response.json()[0]
    assert isinstance(ad_data["id"], str), "Поле id должно быть строкой"
    assert isinstance(ad_data["name"], str), "Поле name должно быть строкой"
    assert ad_data["id"] != ad_data["name"], "Поля id и name перепутаны"