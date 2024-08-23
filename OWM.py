import requests

text = ""
textfire = ""

def setup(func):
    try:
        global text, textfire
        city = func
        apikey = "APIKEY"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=en&appid={apikey}'

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
        if index >= 7:
            textfire = "Fire may be 95%"
        if index >= 12 and index <= 7:
            textfire = "Fire may be 75%"
        if index >= 17 and index <= 12:
            textfire = "Fire may be 50%"
        if index >= 27 and index <= 17:
            textfire = "Fire may be 25%"
        if index >= 42 and index <= 27:
            textfire = "Fire may be 5%"
        if index >= 42:
            textfire = "There will be no fire in this city"
    except:
        textfire = "An error occurred, reboot the bot and write the city correctly."
