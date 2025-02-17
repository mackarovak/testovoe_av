# Тест-кейсы для микросервиса объявлений

## 1. Создание объявления

### Тест-кейс 1.1: Успешное создание объявления
- **Предусловие**: Нет
- **Шаги**:
  1. Отправить POST-запрос на `/item` с корректными данными (например, `{"sellerID": 526456, "name": "Test Ad", "price": 100}`).
- **Ожидаемый результат**: 
  - HTTP статус 200
  - В ответе содержится `id` созданного объявления

### Тест-кейс 1.2: Создание объявления с некорректными данными
- **Предусловие**: Нет
- **Шаги**:
  1. Отправить POST-запрос на `/item` с некорректными данными (например, `{"sellerID": "abc", "name": "", "price": -10}`).
- **Ожидаемый результат**: 
  - HTTP статус 400
  - В ответе содержится сообщение об ошибке

## 2. Получение объявления по идентификатору

### Тест-кейс 2.1: Успешное получение объявления
- **Предусловие**: Создано объявление с известным `id`
- **Шаги**:
  1. Отправить GET-запрос на `/item/{id}`.
- **Ожидаемый результат**: 
  - HTTP статус 200
  - В ответе содержится информация о запрошенном объявлении

### Тест-кейс 2.2: Получение несуществующего объявления
- **Предусловие**: Нет
- **Шаги**:
  1. Отправить GET-запрос на `/item/{несуществующий_id}`.
- **Ожидаемый результат**: 
  - HTTP статус 404
  - В ответе содержится сообщение об ошибке

## 3. Получение всех объявлений по идентификатору продавца

### Тест-кейс 3.1: Успешное получение всех объявлений продавца
- **Предусловие**: Создано несколько объявлений с одинаковым `sellerID`
- **Шаги**:
  1. Отправить GET-запрос на `/{sellerID}/item`.
- **Ожидаемый результат**: 
  - HTTP статус 200
  - В ответе содержится список всех объявлений продавца

### Тест-кейс 3.2: Получение объявлений несуществующего продавца
- **Предусловие**: Нет
- **Шаги**:
  1. Отправить GET-запрос на `/{несуществующий_sellerID}/item`.
- **Ожидаемый результат**: 
  - HTTP статус 404
  - В ответе содержится сообщение об ошибке

## 4. Получение статистики по itemID

### Тест-кейс 4.1: Успешное получение статистики
- **Предусловие**: Создано объявление с известным `itemID`
- **Шаги**:
  1. Отправить GET-запрос на `/statistic/{itemID}`.
- **Ожидаемый результат**: 
  - HTTP статус 200
  - В ответе содержится статистика по запрошенному объявлению

### Тест-кейс 4.2: Получение статистики несуществующего itemID
- **Предусловие**: Нет
- **Шаги**:
  1. Отправить GET-запрос на `/statistic/{несуществующий_itemID}`.
- **Ожидаемый результат**: 
  - HTTP статус 404
  - В ответе содержится сообщение об ошибке



# Тест-кейсы для доски объявлений

## Создание объявления
1. **Предусловие**: Пользователь находится на главной странице сайта.
2. **Шаги**:
   - Нажать кнопку "Создать объявление".
   - Заполнить все обязательные поля (например, заголовок, описание, цена).
   - Нажать кнопку "Опубликовать".
3. **Ожидаемый результат**: Объявление успешно создано, отображается на главной странице.

## Редактирование объявления
1. **Предусловие**: Пользователь находится на странице созданного объявления.
2. **Шаги**:
   - Нажать кнопку "Редактировать".
   - Изменить заголовок или описание.
   - Нажать кнопку "Сохранить".
3. **Ожидаемый результат**: Объявление успешно обновлено, изменения отображаются на странице объявления.

## Поиск объявлений
1. **Предусловие**: Пользователь находится на главной странице сайта.
2. **Шаги**:
   - Ввести ключевое слово в поле поиска.
   - Нажать кнопку "Найти".
3. **Ожидаемый результат**: Отображаются объявления, соответствующие ключевому слову.

## Сортировка объявлений
1. **Предусловие**: Пользователь находится на главной странице сайта.
2. **Шаги**:
   - Выбрать параметр сортировки (например, "По дате" или "По цене").
   - Нажать кнопку "Применить".
3. **Ожидаемый результат**: Объявления отображаются в соответствии с выбранной сортировкой.

## Просмотр карточки объявления
1. **Предусловие**: Пользователь находится на главной странице сайта.
2. **Шаги**:
   - Нажать на заголовок объявления.
3. **Ожидаемый результат**: Открывается страница с подробной информацией о выбранном объявлении.