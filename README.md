# MAZ practice


Инструкция для запуска проекта:

##Установка Docker и Docker Compose:
    Убедитесь, что Docker и Docker Compose установлены на вашем компьютере. Инструкции по установке можно найти на официальных сайтах:
        [Docker](https://www.docker.com/)
        [Docker Compose](https://docs.docker.com/compose/gettingstarted/)

##Распаковка архива:
    Распакуйте полученный архив maz-master.zip в удобное место на вашем компьютере.


##Запуск Docker Compose:
    Перейдите в директорию, куда вы разархивировали полученный архив, где находится файл docker-compose.yml, и с помощью консоли(PowerShell) выполните команды для запуска Docker Compose.
    ```
    docker-compose up --build
    ```
    Эта команда создаст и запустит все необходимые контейнеры (база данных, backend, frontend).

##Проверка работы:
    Откройте веб-браузер и перейдите по следующим URL:
        Backend (Django): [http://localhost:8000](http://localhost:8000)
        Frontend (React): [http://localhost:3000](http://localhost:3000)
