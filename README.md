# MAZ practice


Инструкция для запуска проекта:

## Установка Docker и Docker Compose:
Убедитесь, что Docker и Docker Compose установлены на вашем компьютере. Инструкцию по установке можно найти на официальном сайте:
    [Docker](https://www.docker.com/products/docker-desktop/)

## Распаковка архива:
Распакуйте полученный архив `maz-master-main.zip` в удобное место на вашем компьютере.


## Запуск Docker Compose:
Перейдите в директорию, куда вы разархивировали полученный архив, где находится файл docker-compose.yml, и с помощью консоли (PowerShell) выполните команды для запуска Docker Compose (убедитесь, что у вас уже запущен Docker Engine).

```
docker-compose up --build
```

Эта команда создаст и запустит все необходимые контейнеры (база данных, backend, frontend).

## Проверка работы:
Откройте веб-браузер и перейдите по следующим URL:
    Backend (Django): [http://localhost:8000](http://localhost:8000)
    Frontend (React): [http://localhost:3000](http://localhost:3000)

При входе на http://localhost:3000 возможно возникновение ошибки с библиотекой axios. Для перезапуска билдинга проекта на docker-compose нажмите Ctrl+C для выключения запущенного проекта и пропишите заново:

```
docker-compose up --build
```
