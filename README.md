С помощью Api для Yatube возможно:

- Создавать пост
- Запросить все записи автора
- Подписаться на автора
- Комментировать записи автора


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

Переходим в диск, куда хотим загрузить: 
cd /c
к примеру в папку Dev, расположенную на диске С
cd Dev/

Далее:
git clone https://github.com/Iankel86/api_final_yatube.git
```

```
Cоздать и активировать виртуальное окружение (я под версию 3,7 ):
	Все действия выполняем через Git Bash (по умолчанию ставим git bash в vs code)
	Создать новый venv указав путь до нужной версии Python: 

1) C://Python37/python.exe  -m venv venv
2) В vs code через Ctrl + Shift + P -> Выбрать интерпретатор Python -> Enter interpreter path ... -> Find
Указать путь до python.exe в папке venv проекта ...venv/Scripts/python.exe
3) Закрыть текущий терминал и открыть новый Git Bash
4) пропсиать команду, чтобы узнать версию:  python -V

Виртуальное окружение должно стать активированным (venv)

```
Обновить pip-:   python -m pip install --upgrade pip 
```

Установить зависимости из файла requirements.txt:

pip install -r requirements.txt
```
Дополнительно устанавливаем 2 библиотеки
1) Djoser:
pip install djoser djangorestframework-simplejwt==4.7.2

2) Подключение бэкендов - django-filter
pip install django-filter
```

```
Теперь выполнить миграцию в 2 команды:

python manage.py makemigrations
python manage.py migrate

```

Запустить проект:

```
python3 manage.py runserver
```
