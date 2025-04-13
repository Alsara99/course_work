import json
from src.services import return_search
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_return_search_valid_match(monkeypatch):
    sample_data = [
        {
            'Категория': 'Переводы',
            'Описание': 'Ivan I.',
            'Сумма': 1000
        },
        {
            'Категория': 'Оплата',
            'Описание': 'Magazin'
        },
        {
            'Категория': 'Переводы',
            'Описание': 'Anna B.'
        }
    ]

    monkeypatch.setattr("services.logger.info", lambda msg: None)

    result = return_search(sample_data)
    parsed_result = json.loads(result)

    assert isinstance(result, str)
    assert len(parsed_result) == 2
    assert parsed_result[0]['Описание'] == 'Ivan I.'
    assert parsed_result[1]['Описание'] == 'Anna B.'


def test_return_search_no_match(monkeypatch):
    sample_data = [
        {'Категория': 'Оплата', 'Описание': 'Market'},
        {'Категория': 'Переводы', 'Описание': 'NoMatch123'}
    ]

    monkeypatch.setattr("services.logger.info", lambda msg: None)

    result = return_search(sample_data)
    parsed_result = json.loads(result)
    assert parsed_result == []


def test_return_search_with_exception(monkeypatch):
    sample_data = None

    errors = []

    def mock_error(msg):
        errors.append(msg)

    monkeypatch.setattr("src.services.logger.error", mock_error)

    result = return_search(sample_data)

    assert result is None
    assert any("Ошибка" in msg for msg in errors)