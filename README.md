# Algocode Notifier

Бот с уведомлениями о посылках в Яндекс Кружке

## beta-algocode-parser

Эта директория содержит первоначальную версию бота, использующую парсинг таблички. Возможно, кому-то может пригодиться

## archive

Архив данных за все дни (естестенно, в которые бот работал). Будет постепенно дополняться

## Основной проект

```bash
git clone https://github.com/aVitness/algocode-notifier.git
cd algocode-notifier
pip install -r ./requirements.txt
python main.py
```

* Перед запуском:
1. Необходимо указать переменную окружения `TELEGRAM_TOKEN` содержащую токен вашего бота (либо указать его в `config.py`)
2. Изменить переменные `CHAT_ID` (ссылка на основной канал для отправки уведомлений), `STANDINGS_PAGE` (ссылка на данные с алгокода - не на табличку, а на json данные), `title_replacements` (краткие заголовки для контестов - нужны для избежания слишком длинных нечитабельных текстов + превышения лимита длины кнопок в телеграме) в файле `config.py`
