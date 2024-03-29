# hw04_tests
## Описание проекта
### Покрытие следующими тестами проекта hw03_forms https://github.com/DumaDim/hw03_forms.git:
#### Тестирование Models: «Unittest в Django: тестирование моделей»
1. Протестированы модели приложения posts в Yatube.
2. Добавили в классы Post и Group метод __str__.
3. Протестировали, правильно ли отображается значение поля __str__ в объектах моделей.

#### Тестирование URLs: «Unittest в Django: тестирование URLs»
1. Проверили доступность страниц и названия шаблонов приложения Posts проекта Yatube с учетом права доступа.
2. Проверили, что запрос к несуществующей странице вернёт ошибку 404.

#### Проверка namespase:name и шаблонов: «Unittest в Django: тестирование Views»
1. Написали тесты, проверяющие, что во view-функциях используются правильные html-шаблоны.

#### Тестирование контекста: «Unittest в Django: тестирование views»
1. Проверили, соответствует ли ожиданиям словарь context, передаваемый в шаблон при вызове.

#### Дополнительная проверка при создании поста: «Unittest в Django: тестирование Views»
1. Проверили, что если при создании поста указать группу, то этот пост появляется:
    - на главной странице сайта,
    - на странице выбранной группы,
    - в профайле пользователя.
2. Проверили, что этот пост не попал в группу, для которой не был предназначен.

#### Тестирование Forms: «Unittest в Django: тестирование Forms»
1. Написали тесты проверяющие что при отправке валидной формы со страницы создания поста reverse('posts:create_post') создаётся новая запись в базе данных.
2. Написали тесты проверяющие что при отправке валидной формы со страницы редактирования поста reverse('posts:post_edit', args=('post_id',)) происходит изменение поста с post_id в базе данных.

#### Технологии
   При написании тестов использовалась библиотека Unittest, и методы setUp и setUpClass.

## Установка проекта из репозитория
### Шаг 1
Клонировать репозиторий себе на компьютер
```bash
https://github.com/DumaDim/hw04_tests.git
```

### Шаг 2
Создать и активировать виртуальное окружение
```bash
python -m venv venv
source venv/Scripts/activate
```

### Шаг 3
Установить зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```

