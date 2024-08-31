import requests

text = ""
textfire = ""
lang = "en"

def setup(func):
    try:
        global text, textfire
        city = func
        apikey = "601cdbe6b5afae430e572e0c07bf4865"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={lang}&appid={apikey}'

        res = requests.get(url)
        info = res.json()
        weether = info["weather"][0]["id"]
        main = info["main"]
        temp = main["temp"]

            #Clouds = 801,802,803,804
            #Snow = 600,601,602,611,612,613,615,616,620,621,622
            #Rain = 500,501,502,503,504,511,520,521,522,531
            #Thunderstorm = 200,201,202,210,211,212,221,230,231,232

        index = (weether / temp)
        if weether == 800:
            text = "clear sky"
        elif weether == 801 or 802 or 803 or 804:
            text = "clouds"
        elif weether == 600 or 601 or 602 or 611 or 612 or 613 or 615 or 616 or 620 or 621 or 622:
            text = "snow"
        elif weether == 500 or 501 or 502 or 503 or 504 or 511 or 520 or 521 or 522 or 531:
            text = "moderate rain"
        elif weether == 200 or 201 or 202 or 210 or 211 or 212 or 221 or 230 or 231 or 232:
            text = "thunderstorm"


        if index <= 7 and lang == "en":
            textfire = "Fire may be 95%"
        if index <= 7 and lang == "es":
            textfire = "El fuego puede ser del 95%"
        if index <= 7 and lang == "ru":
            textfire = "Возгорание может составлять 95%"
        if index <= 7 and lang == "lv":
            textfire = "Uguns var būt 95%"

        if index <= 12 and index >= 7 and lang == "en":
            textfire = "Fire may be 75%"
        if index <= 12 and index >= 7 and lang == "es":
            textfire = "El fuego puede ser del 75%"
        if index <= 12 and index >= 7 and lang == "ru":
            textfire = "Возгорание может составлять 75%"
        if index <= 12 and index >= 7 and lang == "lv":
            textfire = "Uguns var būt 75%"
        
        if index <= 17 and index >= 12 and lang == "en":
            textfire = "Fire may be 50%"
        if index <= 17 and index >= 12 and lang == "es":
            textfire = "El fuego puede ser del 50%"
        if index <= 17 and index >= 12 and lang == "ru":
            textfire = "Возгорание может составлять 50%"
        if index <= 17 and index >= 12 and lang == "lv":
            textfire = "Uguns var būt 50%"
        
        if index <= 27 and index >= 17 and lang == "en":
            textfire = "Fire may be 25%"
        if index <= 27 and index >= 17 and lang == "es":
            textfire = "El fuego puede ser del 25%"
        if index <= 27 and index >= 17 and lang == "ru":
            textfire = "Возгорание может составлять 25%"
        if index <= 27 and index >= 17 and lang == "lv":
            textfire = "Uguns var būt 25%"
        
        if index <= 42 and index >= 27 and lang == "en":
            textfire = "Fire may be 5%"
        if index <= 42 and index >= 27 and lang == "es":
            textfire = "El fuego puede ser del 5%"
        if index <= 42 and index >= 27 and lang == "ru":
            textfire = "Возгорание может составлять 5%"
        if index <= 42 and index >= 27 and lang == "lv":
            textfire = "Uguns var būt 5%"
        
        if index >= 42 and lang == "en":
            textfire = "There will be no fire in this city"
        if index >= 42 and lang == "es":
            textfire = "No habrá fuego en esta ciudad"
        if index >= 42 and lang == "ru":
            textfire = "Пожара в этом городе не будет"
        if index >= 42 and lang == "lv":
            textfire = "Ugunsgrēka šajā pilsētā nebūs"
        
    except:
        if lang == "en":
            textfire = "An error occurred, reboot the bot and write the city correctly."
        if lang == "es":
            textfire = "Ocurrió un error, reinicie el bot y escriba la ciudad correctamente."
        if lang == "ru":
            textfire = "Произошла ошибка, перезагрузите бота и напишите город правильно."
        if lang == "lv":
            textfire = "Radās kļūda, restartējiet botu un pareizi ierakstiet pilsētu."
