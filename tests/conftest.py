import pytest
import json
from unittest.mock import MagicMock


@pytest.fixture
def mock_transactions_df():
    mock_df = MagicMock()
    mock_df.fillna.return_value = mock_df
    mock_df.sort_values.return_value = mock_df
    mock_df.__getitem__.return_value = ["01.02.2022", "02.02.2022"]
    mock_df.to_dict.return_value = [
        {
            "Дата операции": "01.02.2022",
            "Сумма платежа": 1000,
            "Категория": "Продукты",
            "Описание": "Пятёрочка"
        },
        {
            "Дата операции": "02.02.2022",
            "Сумма платежа": 2000,
            "Категория": "Техника",
            "Описание": "DNS"
        },
    ]
    return mock_df


@pytest.fixture
def mock_currency_file():
    data = {"user_currencies": ["USD", "EUR"]}
    return json.dumps(data)


@pytest.fixture
def mock_stock_file():
    data = {"user_stocks": ["AAPL", "GOOG"]}
    return json.dumps(data)


@pytest.fixture
def mock_currency_response():
    return {
        "conversion_rates": {"RUB": 89.73}
    }


@pytest.fixture
def mock_stock_response():
    return {
        "Global Quote": {
            "01. symbol": "AAPL",
            "05. price": "165.32"
        }
    }