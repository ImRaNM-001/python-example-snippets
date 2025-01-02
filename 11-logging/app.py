import logging
import os

log_file: str = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'app.log')

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers = [
        # logging.FileHandler('app.log'),          # needs "app.py" to be run from currrent directory, hence commented
        logging.FileHandler(log_file),
        logging.StreamHandler()                      # used to append subsequent logging information to the "app.log" file
    ]
)

# specify a module for the logger
logger = logging.getLogger('Arithmetic App Operation')

def add(a: int, b: int) -> None:
    result: int = a + b
    logger.debug(f'Adding {a} + {b} -> {result}')
    # return result

def sub(a: int, b: int) -> None:
    result: int = a - b
    logger.debug(f'Subtracting {a} - {b} -> {result}')

def mult(a: int, b: int) -> None:
    try:
        if isinstance(a, str) | isinstance(b, str):         
            logger.critical('Kya de rha hai bey tu, dtype check kar pehle....')
            raise ValueError('error >')                             # this line will re-direct to the "except" block - refer "/Python-projects/7-exception_handling/7.2-custom_exceptions.ipynb" for custom exceptions LESSON
        else:
            result: int = a * b
            logger.debug(f'Multiplying {a} * {b} -> {result}')

    except ValueError as error:
        logger.error(f'{error} samajh pehle....')

def div(a: int, b: int) -> None:
    try:
        result: float = round(a / b, 2)
        logger.debug(f'Dividing {a} / {b} -> {result}')

    except ZeroDivisionError as error:
        logger.error(f'{error} ain\'t no possible')

add(4, 15)
sub(100, 3)
mult(22, '2')
div(14, 0)







