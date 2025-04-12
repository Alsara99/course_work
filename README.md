# Домашняя работа 10.1

## Описание:

Приложение для анализа транзакций, которые находятся в Excel-файле. 
Приложение генерирует JSON-данные для веб-страниц, 
формирует Excel-отчеты,
предоставляет другие сервисы.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Использование:

Примеры использования функций:

```python
from src.views import main_view
from src.services import return_search
from src.reports import spending_by_weekday
import pandas as pd

df = pd.read_excel("../data/operations.xlsx")

# Пример использования spending_by_weekday
spending_by_weekday(df)

# Пример использования main_view
main_view("../data/operations.xlsx", "2019.5.17 0:0:0")

# Пример использования return_search
return_search(df)

```

## Тестирование

В нашем проекте используется тестирование для обеспечения надёжности и корректности работы. Был использован фреймвор pytest.
Все написанные тесты находятся в папке tests

```
File	        statements  missing  coverage
src\__init__.py	    0	        0      100%
src\reports.py	    53	        5       91%
src\services.py     22	        0      100%
src\utils.py	    103	        15      85%
src\views.py        16          16       0%
Total	           194	        36      81%