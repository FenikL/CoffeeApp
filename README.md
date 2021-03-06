# CoffeeApp

## Описание

CoffeeApp - это backend сервис учета кофейных капсул. Идея создания сервиса возникла после покупки капсюльной кофемашины
в нашем рабочем коллективе. Так как у всех разные потребности по вкусу, крепкости, цене и количеству кофе, то возникает 
сложность формирования очередного заказа партии капсул. С помощью сервиса можно:
* хранить информацию о всех видах капсулах
* формировать заказ 
* Смотреть, какие капсулы у пользователя на балансе

## Техническая часть

Проект разрабатывается в учебно-практических целях. 

Стек: FastAPI, PostgreSQL.

### Структура базы данных

![Схема базы данных](https://github.com/FenikL/CoffeeApp/blob/master/Coffee_project.png)

## Установка и запуск

1. Клонируем репозиторий

```sh
$ git clone https://github.com/FenikL/CoffeeApp.git
$ cd CoffeeApp
```

2. Устанавливаем и активируем виртуальное окружение Python

```sh
$ python3 -m venv .venv
```
MacOS или Linux: 

```sh
$ source .venv/bin/activate
```

3. Устанавливаем необходимые библиотеки

```sh
$ pip install -r requirements.txt
```

4. Запускаем сервер:

```sh
$ uvicorn app.main:app --reload
```