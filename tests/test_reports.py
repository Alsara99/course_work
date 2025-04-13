import pytest
import pandas as pd
import os
import json

from src.reports import spending_by_weekday

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Дата операции': [
            '25.01.2019 12:00:00',
            '10.02.2019 12:00:00',
            '05.03.2019 12:00:00',
        ],
        'Сумма операции': [100, 200, 300]
    })


def test_spending_by_weekday_invalid_date_format(sample_df, monkeypatch):
    errors = []

    def mock_error(msg):
        errors.append(msg)

    monkeypatch.setattr("src.reports.logger.error", mock_error)

    result = spending_by_weekday(sample_df, "25/03/2019")
    assert result is None
    assert any("Ошибка" in msg for msg in errors)


def test_spending_by_weekday_none_input(monkeypatch):
    errors = []

    def mock_error(msg):
        errors.append(msg)

    monkeypatch.setattr("src.reports.logger.error", mock_error)

    result = spending_by_weekday(None)
    assert result is None
    assert any("Ошибка" in msg for msg in errors)