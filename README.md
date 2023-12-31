# My1bot_voice_menu20230611
ШАБЛОН бота, который озвучивает свои действия и действия пользователя. Принимает текст и команды от пользователя в текстовом и голосовом режиме. Имеет шаблон миню команд, которые можно изменить под свои задачи. Некоторые настройки в отдельном файле.

## Установка и запуск:
1. Устанавливаем виртуальное окружение для программы через Командную строку

`python3 –m venv venv`

2. Запускаем виртуальное окружение

`source venv/bin/activate`

3. Импортируем библиотеки 

 `pip install -r requirements.txt`

4. Запускаем программу

`python main.py`

## Ручная установка зависимостей (если понадобиться):
`pip install pyttsx3` 
`pip install SpeechRecognition` 
`pip install pyaudio` 
`pip install clipboard` 

## Подробное описание программы в main.py:
Данный код выполняет функции голосового помощника, который обрабатывает ввод пользователя и предоставляет соответствующие ответы и команды.

Первым делом, код импортирует несколько библиотек: `pyttsx3` для синтеза речи, `speech_recognition` для распознавания речи, `configparser` для работы с конфигурационными файлами, и `clipboard` для доступа к буферу обмена.

Затем, устанавливается параметр ввода текста (`input_method`), который может быть установлен на "input_voice" или "input_text". Этот параметр определяет способ ввода текста пользователем.

Далее, определены несколько функций:

1. `speak_and_print(text)`: Эта функция выводит текст на экран и произносит его с помощью библиотеки `pyttsx3`. Здесь создается объект `engine` с параметрами голоса, заданными в файле `bot_params.ini`, и произносится переданный текст.

2. `load_bot_params()`: Эта функция загружает параметры бота из файла `bot_params.ini` и возвращает их в виде словаря. В файле `bot_params.ini` содержатся параметры, такие как движок голоса, скорость речи и выбранный голос.

3. `listen()`: Эта функция отвечает за распознавание речи пользователя. Она использует библиотеку `speech_recognition` для записи аудио с микрофона и распознавания речи с помощью сервиса Google. Распознанный текст возвращается из функции.

Затем, основная часть программы (`main()`) начинается с загрузки параметров бота с помощью функции `load_bot_params()` и приветствия пользователя с помощью функции `speak_and_print()`.

Далее, программа переходит в бесконечный цикл, в котором ожидает ввода пользователя. Если параметр `input_method` равен "input_voice", программа слушает речь пользователя с помощью функции `listen()`. В противном случае, программа ожидает ввод текста от пользователя с помощью функции `input()`.

В зависимости от ввода пользователя, выполняются следующие действия:

- Если пользователь вводит "пока", программа прощается с пользователем и завершается.
- Если пользователь вводит "1", программа переключает режим ввода между голосовым и текстовым.
- Если пользователь вводит "2", программа выводит текст из буфера обмена.
- Если пользователь вводит "3", программа сообщает, что команда находится в разработке.
- Если пользователь

 вводит непустую строку, программа выводит эту строку.

Таким образом, код представляет собой простого голосового помощника, который обрабатывает ввод пользователя, распознает речь и предоставляет соответствующие ответы и команды.

## Подробное описание bot_params.ini:
Файл `bot_params.ini` является конфигурационным файлом, используемым для хранения параметров бота. Он содержит различные настройки, которые определяют поведение и характеристики голосового помощника.

Файл `bot_params.ini` имеет следующую структуру:

```
; Параметр rate - это скорость озвучивания текста бота (от 100 до 200, 150 - обычная скорость)
; Но я ставил 400 и скорость становилась еще быстрее!!!
; voice_engine - голосовой движок, и это voice туда же
; Эта настройка бота bot_params.ini
[Bot Parameters]
voice_engine = pyttsx3
rate = 400
voice = russian_voice
```

Внутри квадратных скобок `[Bot Parameters]` указывается секция, которая содержит параметры бота. Каждый параметр задается в формате `ключ = значение`.

В данном случае, в секции `[Bot Parameters]` определены следующие параметры:

1. `voice_engine`: Этот параметр определяет голосовой движок, который используется для синтеза речи. Значение `pyttsx3` указывает на использование библиотеки pyttsx3.

2. `rate`: Этот параметр определяет скорость озвучивания текста бота. Значение должно быть целым числом в диапазоне от 100 до 200. Заметка в комментариях указывает, что при значении 150 скорость является обычной, но значение 400 было использовано и приводит к еще более быстрой скорости озвучивания.

3. `voice`: Этот параметр определяет выбранный голос для синтеза речи. Значение `russian_voice` указывает на использование русскоязычного голоса.

Файл `bot_params.ini` позволяет легко настраивать различные параметры голосового помощника, такие как голосовой движок, скорость озвучивания и выбранный голос, без необходимости изменения исходного кода программы.
