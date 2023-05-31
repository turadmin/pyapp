# Используйте официальный образ Python в качестве базового образа
FROM python:3.9

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование файлов проекта в рабочую директорию контейнера
COPY . .

# Указываем порт, на котором будет работать приложение
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app.py"]
