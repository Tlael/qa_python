import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    return collector
