import os

from dotenv import load_dotenv

load_dotenv()

CHAT_ID = "@yandex_b_notifications"
ME_CHAT_ID = 727312887

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE = os.getenv("DATABASE")

female_names = {'Валентина', 'Алена', 'Елена', 'Ксения', 'Анастасия', 'Татьяна', 'Милана', 'Олеся', 'Виктория', 'Надежда', 'Юлия', 'Ярослава', 'София', 'Мария',
                'Софья', 'Дарья', 'Алина', 'Валерия', 'Ирина', 'Арина'}

messages = [
    [
        ("-1", [
            "*{name}* начал работать над задачей *{task}*, но понял, что не может найти подходящее решение.",
            "Стоило подумать, а не сразу отсылать свой код. У *{name}* первый штраф по задаче *{task}*",
            "Ой, *{name}* решил отправить код без компиляции. Первый штраф за *{task}* уже в кармане.",
            "*{name}*, взялся за задачу *{task}*, но осознал, что не стоило писать код в блокноте.",
            "*{name}*, приступил к задаче *{task}*, но застрял в раздумьях.",
            "Не спеши, *{name}*, подумай еще раз перед отправкой кода. Штраф за неверную посылку по задаче *{task}* уже прилетел.",
            "Казалось бы, простая задача... Но видимо не для всех. *{name}* получил свой первый штраф за задачу *{task}*"
        ]),
        ("\+", [
            "*{name}* уничтожил задачу *{task}* с первой попытки!",
            "*{name}* сдал задачу *{task}* с первой попытки. Наверное, ему просто повезло...",
            "*{name}* мастерски справился с задачей *{task}* с первого раза."
        ]),
        ("\+[0-9]+", [
            "*{name}* сдал задачу *{task}* после {tries} неверных посылок.",
            "Ученик *{name}*, изворачиваясь как кот, смог поймать задачу *{task}* с {tries} попытками, будто это нить из клубка.",
            "Задача *{task}* не могла пройти мимо ученика *{name}*, так что он ее решил после {tries} попыток, словно с чашкой кофе в руках.",
            "Ученик *{name}* решил задачу *{task}* с {tries} попытками, и его успех был таким громким, что можно было услышать аплодисменты по всему кружку.",
            "Задача *{task}* пыталась противостоять ученику *{name}*, но он с {tries} попытками доказал ей, кто здесь настоящий босс.",
            "Ученик *{name}*, с {tries} попытками на счету, без проблем разгадал задачу *{task}*, и даже сервера восторженно аплодировали.",
            "Ученик *{name}*, с {tries} попытками в запасе, покорил задачу *{task}*, словно владелец клавиатуры-танка.",
            "Задача *{task}* пыталась сбежать от ученика *{name}*, но после {tries} попыток он ее настиг и решил с легкостью.",
            "Ученик *{name}*, с {tries} попытками, справился с задачей *{task}* так легко, словно это была задачка для младших классов."
        ]),
        ("-[1-9]0", [
            "Бесконечность не предел! У *{name}* уже {tries} неверных посылок по задаче *{task}*.",
            "У *{name}* только что стало {tries} неверных посылок по задаче *{task}*. Может ему стоило выбрать географию, а не программирование?",
            "*{name}* получает {tries} штраф по задаче *{task}*. Кажется, пора забрать у него ноутбук."
        ]),
    ],
    [
        ("-1", [
            "*{name}* начала работать над задачей *{task}*, но поняла, что не может найти подходящее решение.",
            "Стоило подумать, а не сразу отсылать свой код. У *{name}* первый штраф по задаче *{task}*",
            "Ой, *{name}* решила отправить код без компиляции. Первый штраф за *{task}* уже в кармане.",
            "*{name}*, взялась за задачу *{task}*, но осознала, что не стоило писать код в блокноте.",
            "*{name}*, приступила к задаче *{task}*, но застряла в раздумьях.",
            "Не спеши, *{name}*, подумай еще раз перед отправкой кода. Штраф за неверную посылку по задаче *{task}* уже прилетел.",
            "Казалось бы, простая задача... Но видимо не для всех. *{name}* получила свой первый штраф за задачу *{task}*"
        ]),
        ("\+", [
            "*{name}* уничтожила задачу *{task}* с первой попытки!",
            "*{name}* сдала задачу *{task}* с первой попытки. Наверное, ей просто повезло...",
            "*{name}* мастерски справилась с задачей *{task}* с первого раза."
        ]),
        ("\+[0-9]+", [
            "*{name}* сдала задачу *{task}* после {tries} неверных посылок.",
            "Ученица *{name}*, изворачиваясь как кошка, смогла поймать задачу *{task}* с {tries} попытками, будто это нить из клубка.",
            "Задача *{task}* не могла пройти мимо ученицы *{name}*, так что она ее решила после {tries} попыток, словно с чашкой кофе в руках.",
            "Ученица *{name}* решила задачу *{task}* с {tries} попытками, и ее успех был таким громким, что можно было услышать аплодисменты по всему кружку.",
            "Задача *{task}* пыталась противостоять ученице *{name}*, но она с {tries} попытками доказала ей, кто здесь настоящий босс.",
            "Ученица *{name}*, с {tries} попытками на счету, без проблем разгадала задачу *{task}*, и даже сервера восторженно аплодировали.",
            "Ученица *{name}*, с {tries} попытками в запасе, покорила задачу *{task}*, словно владелец клавиатуры-танка.",
            "Задача *{task}* пыталась сбежать от ученицы *{name}*, но после {tries} попыток она ее настигла и решила с легкостью.",
            "Ученица *{name}*, с {tries} попытками, справилась с задачей *{task}* так легко, словно это была задачка для младших классов."
        ]),
        ("-[1-9]0", [
            "Бесконечность не предел! У *{name}* уже {tries} неверных посылок по задаче *{task}*.",
            "У *{name}* только что стало {tries} неверных посылок по задаче *{task}*. Может ей стоило выбрать географию, а не программирование?",
            "*{name}* получает {tries} штраф по задаче *{task}*. Кажется, пора забрать у нее ноутбук."
        ]),
    ]
]

title_replacements = {
    'Динамическое программирование 2': 'ДП 2',
    'Дерево отрезков 2': 'ДО 2',
    'Дерево отрезков 1': 'ДО 1',
    'Динамическое программирование 1': 'ДП 1',
    'Графы 2': 'Графы 2',
    'Задачи с двойным запуском': 'Двойной запуск',
    'Бинарный и тернарный поиск. Интерактивные задачи': 'Поиски+Интерактивки',
    'Теория чисел': 'ТЧ',
    'C++, стресс-тестирование и дебаг': 'Дебаг',
    'Строки 2': 'Строки 2',
    'Строки 1': 'Строки 1',
    'Графы 1': 'Графы 1'
}

first_solve_message = "⚡ *{name}* стал первым, кто решил задачу *{task}*!"
