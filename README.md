Conventusdemo rebuild
===========================

## Description
Conventusdemo - сайт для демонстрации системы CONVENTUS.

## Requirements
Для виртуально окружения можно использовать virtualenv. Разрабатывалась на python 3.4. Через pip устанавливались необходимые [пакеты (requirements.txt).](./requirements.txt)


## Install
Порядок установки:
```
sudo apt install python-virtualenv

virtualenv --no-site-packages -p python3 env/ENVNAME
source env/ENVNAME/bin/activate

pip3 install --upgrade pip
pip3 install --upgrade -r requirements.txt

deactivate
```

## Getting started
Для запуска сайта

```
source env/ENVNAME/bin/activate

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser --username USERNAME --email EMAIL@EMAIL
./manage.py runserver
```
В браузере переходим на 127.0.0.1:8000


## Todo list
Список запланированных [изменений (todo.md).](./todo.md)


## Versions
 A.B.C[.D]

* A - значительные изменения в коде и в концепции
* B - старшие ревизии, четные/нечетные - стабильные/для разработчика
* C - младшие ревизии, четные/нечетные - стабильные/для разработчика, заплатки
* D - исправление одной ошибки



