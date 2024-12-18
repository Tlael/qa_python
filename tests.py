import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    )
    # проверка установки жанра для книги
    def test_set_book_genre(self, collector, genre):
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)
        assert collector.books_genre['Гордость и предубеждение и зомби'] == genre

    @pytest.mark.parametrize(
        'genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    )
    # получение жанра книги по ее имени
    def test_get_book_genre_name(self, collector, genre):
        collector.add_new_book('Тестовая книга')
        collector.set_book_genre('Тестовая книга', genre)
        assert collector.get_book_genre('Тестовая книга') == genre

    @pytest.mark.parametrize(
        'genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    )
    # вывод списка книг с определенным жанром
    def test_get_books_with_specific_genre(self, collector, genre):
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)
        assert collector.get_books_with_specific_genre(genre) == ['Гордость и предубеждение и зомби']

    @pytest.mark.parametrize(
        'genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    )
    # получение словаря books_genre
    def test_get_books_genre_dict(self, collector, genre):
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', genre)
        expected_result = {
            'Гордость и предубеждение и зомби': genre,
            'Что делать, если ваш кот хочет вас убить': genre
        }
        assert collector.get_books_genre() == expected_result

    @pytest.mark.parametrize(
        'genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    )
    # получение книг, которые подходят для детей
    def test_books_for_children(self, collector, genre):
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', genre)
        collector.books_for_children = collector.get_books_for_children()
        assert 'Ужасы' and 'Детективы' not in collector.books_for_children

    # добавление книг в избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.favorites == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    # добавление отсутствующей книги в избранное
    def test_add_book_in_favorites_not_name_book(self, collector):
        collector.add_book_in_favorites('Тестовая книга')
        assert collector.favorites == []

    # удаление книги из избранного
    def test_delete_book_from_favorites_true(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить']

    # удаление отсутствующей книги из избранного
    def test_delete_book_from_favorites_false(self, collector):
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == []

    # получение списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        expected_result = [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        ]
        assert collector.get_list_of_favorites_books() == expected_result
