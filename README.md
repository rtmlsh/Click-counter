# Обрезка ссылок с помощью Битли
Скрипт позволяет сделать из обычной ссылки короткую битссылку и посчитать количество кликов по ней. 

## Как установить  
Python3 должен быть уже установлен. Для запуска скрипта установите виртуальное окружение: 

    >>> python3 -m venv venv
    
Затем активируйте виртуальное окружение (вариант для Windows): 

    >>> venv\Scripts\activate 
    
Используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
    
    >>> pip install -r requirements.txt

Скрипт работает с переменными окружения для взаимодействия с [API Bitly](https://dev.bitly.com/). Для успешной работы скрипта необходимо получить [токен](https://bitly.com/a/oauth_apps) (GENERIC ACCESS TOKEN — нужный тип токена) и записать его в .env файл: 


    >>> echo BITLY_TOKEN=токен > .env

Запуск скрипта осуществляеся в командной строке, ссылку или битлинк передайте аргументом:
    
    >>> python main.py https://www.youtube.com/
    Битссылка: https://bit.ly/3qPJy7w

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org/modules/). 
