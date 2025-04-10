import re
import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../course_work/logs/services.log')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def return_search(lst):
    """Осуществляем поиск переводов физическим лицам"""
    result = []
    try:
        for operation in lst:
            if operation['Категория'] == 'Переводы':
                for value in operation.values():
                    search = re.findall(r'^\w+\s\D\.$', str(value))
                    if search:
                        result.append(operation)
        logger.info("Поиск осуществлён, данные переобразованы в JSON")
        return json.dumps(result)
    except Exception as e:
        logger.error(f"Ошибка: {e}")

