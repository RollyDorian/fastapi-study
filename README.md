# FastAPI Study

Учебный API для работы с записями о ML-моделях.

## Развёртывание

Требование — Docker. Команды выполняются по одной из каталога с `Dockerfile`.

### Первый запуск

```bash
docker build -t my_fastapy_app .
docker run -d --name my_fastapi_container -p 8000:8000 my_fastapy_app
```

Swagger UI доступен по адресу `http://<адрес-сервера>:8000/docs`.

### Обновление

**Сборка образа после обновления файлов**

```bash
docker build -t my_fastapy_app .
```

**Пересоздание контейнера после успешной сборки**

```bash
docker stop my_fastapi_container
docker rm my_fastapi_container
docker run -d --name my_fastapi_container -p 8000:8000 my_fastapy_app
```

Записи, добавленные через API, хранятся в памяти и сбрасываются при перезапуске.


**Просмотр логов приложения**

```bash
docker logs -f my_fastapi_container

```