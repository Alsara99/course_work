from src.utils import *
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/views.log')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def main_view(date):
    """Собираем все необходимые функции для вкладки 'Главная'"""
    try:
        result = {
            "greeting": greeting(),
            "card_info": card_info("../data/operations.xlsx", date),
            "top_transactions": top_transactions("../data/operations.xlsx", date),
            "currency_rates": currency_rates(),
            "stock_prices": stock_prices()
        }
        logger.info("Данные для функции Главная в формате JSON отправлены")
        return result
    except Exception as e:
        logger.error(f"Ошибка: {e}")
