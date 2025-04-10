import pytest
from src.utils import *
from unittest.mock import patch, mock_open


@pytest.fixture
def sample_excel_file(tmp_path):
    data = {
        'Дата операции': ['15.03.2024 14:00:00', '05.03.2024 09:00:00', '20.03.2024 21:00:00'],
        'Номер карты': ['1234', '5678', '9012'],
        'Сумма операции с округлением': [1000, 2500, 1500],
        'Кэшбэк': [10, 25, 15],
        'Сумма платежа': [990, 2480, 1490],
        'Категория': ['Еда', 'Путешествия', 'Магазин'],
        'Описание': ['Ресторан', 'Билет', 'Продукты']
    }
    df = pd.DataFrame(data)
    file_path = tmp_path / "sample_data.xlsx"
    df.to_excel(file_path, index=False)
    return str(file_path)


def test_greeting_returns_string():
    result = greeting()
    assert isinstance(result, str)
    assert result in ['Доброй ночи', 'Доброе утро', 'Добрый день', 'Добрый вечер']


def test_card_info_valid(sample_excel_file):
    result = card_info(sample_excel_file, '2024.03.31 23:59:59')
    assert isinstance(result, list)
    assert len(result) == 3
    for item in result:
        assert "last_digits" in item
        assert "total_spent" in item
        assert "cashback" in item


def test_top_transactions_valid(sample_excel_file):
    result = top_transactions(sample_excel_file, '2024.03.31 23:59:59')
    assert isinstance(result, list)
    assert len(result) <= 5
    for item in result:
        assert "date" in item
        assert "amount" in item
        assert "category" in item
        assert "description" in item


@patch("builtins.open", new_callable=mock_open, read_data='{"user_currencies": ["USD", "EUR"]}')
@patch("src.utils.requests.get")
def test_currency_rates_success(mock_get, mock_file):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "conversion_rates": {"RUB": 93.5}
    }

    result = currency_rates()

    assert isinstance(result, list)
    assert len(result) == 2
    for item in result:
        assert item["currency"] in ["USD", "EUR"]
        assert isinstance(item["rate"], float)


@patch("builtins.open", new_callable=mock_open, read_data='{"user_stocks": ["AAPL", "GOOG"]}')
@patch("src.utils.requests.get")
def test_stock_prices_success(mock_get, mock_file):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "Global Quote": {
            "01. symbol": "AAPL",
            "05. price": "172.32"
        }
    }

    result = stock_prices()

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["stock"] == "AAPL"
    assert result[0]["price"] == "172.32"
