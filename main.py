# Импортируем все из библиотеки TKinter
from tkinter import *
from tkinter import messagebox

# Импортируем все из библиотеки TKinter
import requests

# Создаем главный объект (по сути окно приложения)
root = Tk()

def get_weather(event=True):
    # Получаем данные от пользователя
    city = cityField.get()

    # данные о погоде берутся с сайта openweathermap.org
    # прописываем API ключ, который находится в кабинете пользователя на сайте openweathermap.org

    key = '23c3cc1d295aedfe1bf5140568f9d4f3'
    url = 'https://api.openweathermap.org/data/2.5/weather'

    # Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
    params = {'APPID':key, 'q':city, 'units': 'metric','lang':'en'}

    # Отправляем запрос по определенному URL
    response = requests.get(url,params=params)

    # Получаем JSON ответ по этому URL
    weather = response.json()
    if weather['cod'] != '400':
        print(weather['cod'])
        info['text'] = f'{weather["name"]}: {weather["main"]["temp"]}°С'
    else:
        messagebox.showinfo(title="Ошибка",message="Ошибка, невозможно получить данные о погоде"
                                                   "...")

# Настройки главного окна

# Указываем фоновый цвет
root['bg'] = '#fafafa'
# Указываем название окна
root.title('Погодное приложение')
# Указываем размеры окна
w = 300
h = 250

ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()

x = int(ws / 2 - w / 2)
y = int(wh / 2 - h / 2)

root.geometry(f'{w}x{h}+{x}+{y}')

# Делаем невозможным менять размеры окна
root.resizable(width=False,height=False)

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка

frame_top = Frame(root,bg='#ffb700',bd=5)
# Также указываем его расположение
frame_top.place(relx=0.15,rely=0.15,relwidth=0.7,relheight=0.25)

# Реализация второго фрейма
frame_bottom = Frame(root,bg='#ffb700',bd=5)
# Также указываем его расположение
frame_bottom.place(relx=0.15,rely=0.55,relwidth=0.7,relheight=0.1)

# Создаем текстовое поле для получения данных от пользователя
cityField = Entry(frame_top,bg='white',font=30)
cityField.pack()

# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top,text='Посмотреть погоду',command=get_weather)
btn.place(relx=0.2,rely=0.5)

# При нажатии на Enter будет срабатывать метод "get_weather"
root.bind('<Return>',get_weather)

# Создаем текстовую надпись, в которую будет выводиться информация о погоде
info = Label(frame_bottom,text='Погодная информация',bg='#ffb700',font=40)
info.pack()

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()