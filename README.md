# ddz_python


Telegram-бот для автоматической конвертации результатов тестов из Excel в 5-балльную шкалу.

---

## 🚀 Возможности

- 📥 Принимает Excel-файл (.xlsx)
- 🧠 Автоматически определяет максимальный балл из названия теста
- 🔄 Конвертирует оценки в 5-балльную систему
- ➕ Добавляет новые столбцы справа
- 🔒 Не обрабатывает повторно уже конвертированные данные
- 🤖 Работает через Telegram

---

## 📌 Формат Excel


Поддерживается любое количество вопросов

---

## 📊 Шкала оценивания

| Процент | Оценка |
|--------|--------|
| ≥ 90%  | 5 |
| ≥ 70%  | 4 |
| ≥ 50%  | 3 |
| ≥ 30%  | 2 |
| ≥ 10%  | 1 |
| < 10%  | 0 |

---


# 📁 Структура проекта

```text
ddz_python/
│── .gitignore
├── .env
├── main.py
├── requirements.txt
├── README.md
│
├── telegram_bot/
│   └── bot.py
    └── __init__.py
│
└── excel/
    └── convert.py
    └── __init__.py
```

# 📦 Установка проекта

## 1. Клонирование репозитория

```bash
git clone https://github.com/temychem/ddz_python.git
cd ddz_python
```

---

## 2. Создание виртуального окружения

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Установка зависимостей

```bash
pip3 install -r requirements.txt
```

---

# 📦 Используемые библиотеки

Проект использует:

- pandas
- openpyxl
- python-telegram-bot
- python-dotenv

---

# 🔑 Получение Telegram Bot Token

## 1. Откройте Telegram

Найдите:

```text
@BotFather
```

---

## 2. Создайте бота

Отправьте команду:

```text
/newbot
```

---

## 3. Следуйте инструкциям

BotFather выдаст токен вида:

```text
123456789:AAxxxxxxxxxxxxxxxxxxxxxxxx
```

---

# 🔐 Настройка `.env`

Откройте файл:

```text
.env
```

в корне проекта.

---

## Пример содержимого `.env`

```env
TOKEN=123456789:AAxxxxxxxxxxxxxxxxxxxxxxxx
```

---

# ⚠️ Важно

Файл `.env` должен лежать рядом с `main.py`

Правильно:

```text
project/
│
├── .env
├── main.py
```

Неправильно:

```text
project/
│
├── telegram_bot/
│   └── .env
```

---

# 🔐 Загрузка `.env`

В `bot.py` обязательно должно быть:

```python
from dotenv import load_dotenv

load_dotenv()
```

Без этого Python не загрузит переменные окружения.

---

# ▶️ Запуск бота

Из корня проекта:

```bash
python main.py
```

---

# ✅ Успешный запуск

Если всё настроено правильно, в консоли появится:

```text
Bot started...
```

---