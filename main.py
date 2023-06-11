import pyttsx3
import speech_recognition as sr
import configparser
import clipboard # pip install clipboard

# ПАРАМЕТР ВВОДА ТЕКСТА: ГОЛОС ИЛИ ТЕКСТ input_voice или input_text
input_method = "input_text"

# Это голос бота с подгруженными параметрами из файла bot_params.ini
def speak_and_print(text):
    print(text)
    engine = pyttsx3.init()
    engine.setProperty("rate", bot_params["rate"])
    engine.setProperty("voice", bot_params["voice"])
    engine.say(text)
    engine.runAndWait()

# Загружаем данные из файла bot_params.ini
def load_bot_params():
    config = configparser.ConfigParser()
    config.read("bot_params.ini", encoding="utf-8")
    bot_params = {}
    bot_params["voice_engine"] = config.get("Bot Parameters", "voice_engine")
    bot_params["rate"] = config.getint("Bot Parameters", "rate")
    bot_params["voice"] = config.get("Bot Parameters", "voice")
    return bot_params

# Бот слушает мой голос
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak_and_print("Произошла ошибка при распознавании речи.")
        return ""

# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ:
def main():
    global bot_params # подгружаем глобальную переменную bot_params
    global input_method # подгружаем глобальную переменную input_method
    bot_params = load_bot_params()
    speak_and_print("Здравствуй, искатель своей силы! Я ГНОЗИСМБ БОТ рад помочь тебе раскрыть свой потенциал и преодолеть любые преграды. Вместе мы сделаем это!") # Приветствие бота
    while True:
        if input_method == "input_voice":
            print("Выберите пункт или введите текст (1 - голос/текст ввод, 2 - Вставить, 3 - Отмена, пока - Выход): ")
            user_input = listen()
        else:
            user_input = input("Выберите пункт или введите текст (1 - голос/текст ввод, 2 - Вставить, 3 - Отмена, пока - Выход): ")
        if user_input.lower() == "пока":
            speak_and_print("До встречи, бесстрашный герой! Отправляйся в новые приключения и не забывай, что в тебе есть сила, способная покорить весь мир!")
            break
        elif user_input.lower() == "1":
            if input_method == "input_voice":
                speak_and_print("Включен режим текстового ввода")
                input_method = "input_text"
            elif input_method == "input_text":
                speak_and_print("Включен режим голосового ввода")
                input_method = "input_voice"
        elif user_input.lower() == "2":
            speak_and_print("Вставляю текст из буфера обмена:")
            speak_and_print("Вы сказали: " + clipboard.paste()) # Получение текста из буфера обмена
        elif user_input.lower() == "3":
            speak_and_print("Команда в стадии разработки")
            # Добавьте здесь логику для команды "Отмена"
        elif user_input:
            speak_and_print("Вы сказали: " + user_input)

if __name__ == "__main__":
    main()
