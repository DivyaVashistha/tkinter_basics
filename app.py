import tkinter as tk
from datetime import timedelta, datetime

import requests
from apply import apply
from tkcalendar import DateEntry

import calculator

window = tk.Tk()
window.title("Weather App")
height = window.winfo_screenheight()
width = window.winfo_screenwidth()
window.geometry("{}x{}".format(int(width / 2), int(height / 2)))
window.config(bg="#404643")
top_frame = tk.Frame(master=window, height=int((height / 2) * (2 / 7)),bg="#404643")
middle_frame = tk.Frame(master=window, height=int((height / 2) * (3 / 7)),bg="#404643")
bottom_frame = tk.Frame(master=window, height=int((height / 2) * (2 / 7)),bg="#404643")

variable_country = tk.StringVar(master=middle_frame)
variable_city = tk.StringVar(master=middle_frame)
country_codes = ['Country']
city_codes = ['City']
variable_city.set('City')

city = apply(tk.OptionMenu, ((middle_frame, variable_city) + tuple(city_codes)))
city.grid(row=2,column=2,padx=60, pady=20)
selected_city = 'Bangalore'
temp = 0
speed = 1


def option_changed_city(*args):
    global selected_city
    selected_city = variable_city.get()


def option_changed_country(*args):
    if variable_country.get() == "India":
        city_codes.clear()
        city_codes.append("Delhi")
        city_codes.append("Bangalore")
        city_codes.append("Maharashtra")
        city_codes.append("Uttarakhand")
        city_codes.append("Uttarpradesh")

    elif variable_country.get() == "US":
        city_codes.clear()
        city_codes.append("New York")
        city_codes.append("Chicago")
        city_codes.append("Los Angeles")
        city_codes.append("Seattle")
        city_codes.append("Boston")

    else:
        city_codes.append("Choose Country")

    variable_city.set("City")  # default value
    variable_city.trace("w", option_changed_city)
    global city
    city['menu'].delete(0, 'end')
    for choice in city_codes:
        city['menu'].add_command(label=choice, command=tk._setit(variable_city, choice))


variable_country.set("Country")  # default value
variable_country.trace("w", option_changed_country)
country_codes.append("India")
country_codes.append("US")
widget = apply(tk.OptionMenu, (middle_frame, variable_country) + tuple(country_codes))
widget.grid(row=2,column=1, padx=60, pady=20)

cal = DateEntry(middle_frame, width=12, background='#404643', foreground='#3EDBE2', borderwidth=2, year=2020)
cal.grid(row=2,column=3, padx=60, pady=20)

T = tk.Text(top_frame, height=5, width=100,bg="#404643",fg="white",padx=260, pady=20, highlightbackground="#404643")
T.pack(expand=1,fill="both")
T.config(state=tk.NORMAL)

var1 = tk.IntVar()
cb = tk.Checkbutton(middle_frame, text="save", variable=var1, onvalue=1, offvalue=0,bg="#3EDBE2")
cb.grid(row=4,column=2, padx=50, pady=20)


def calculate(*args):
    url = "https://api.weatherbit.io/v2.0/history/daily?city=" + selected_city + "&start_date=" + str(
        cal.get_date() - timedelta(1)) + "&end_date=" + str(
        cal.get_date()) + "&units=S&key=7c485deb578341818ab76cc5758903f1"
    JSONContent = requests.get(url).json()

    print(JSONContent)
    d = {'city': selected_city, 'wind': JSONContent['data'][0]['wind_spd'], 'temp': JSONContent['data'][0]['temp'],
         'humidity': JSONContent['data'][0]['rh'], 'sea': JSONContent['data'][0]['slp']}
    global temp
    global speed
    speed = d['wind']
    temp = d['temp']
    result = "City: " + str(d['city']) + "\nTemperature: " + str(d['temp']) + "K\nWind: " + str(
        d['wind']) + "m/s\nHumidity: " + str(d['humidity']) + "%\nSea Pressure: " + str(d['sea']) + "mb"

    T.delete('1.0', tk.END)
    T.insert(tk.END, result)

    if var1.get() == 1:
        file1 = open("myfile.txt", "w")
        file1.writelines(result)
        file1.close()


b = tk.Button(middle_frame, text="submit", command=calculate,bg="#E4E751")
b.grid(row=6,column=2, padx=50, pady=20)


def temp_convert(t1):
    global temp
    temp = temp - 273.15
    t1.insert(tk.END, round(temp,2))


def wind_convert(t2):
    global speed
    speed = speed * 3.6
    t2.insert(tk.END, round(speed,2))


def assist():
    assist_window = tk.Tk()
    assist_window.config(bg="#404643")
    assist_window.title("Convert Parameters")

    l = tk.Label(assist_window, text="Convert the parameters as per requirement",bg="#404643",fg="white").grid(row=1,column=0,padx=70, pady=20)

    l2 = tk.Label(assist_window, text="Convert the temperature into Celsius",bg="#404643",fg="white").grid(row=3, column=0,padx=20, pady=20)
    b1 = tk.Button(assist_window, text="Convert to Celsius", command=lambda: temp_convert(t1)).grid(row=3, column=1,padx=20, pady=20)
    t1 = tk.Text(assist_window, height=1, width=8,bg="#404643",fg="white")
    t1.grid(row=3, column=2,padx=20, pady=20)

    l3 = tk.Label(assist_window, text="\nConvert the wind speed into km/hr",bg="#404643",fg="white").grid(row=5, column=0,padx=20, pady=20)
    b2 = tk.Button(assist_window, text="Convert to km/hr", command=lambda: wind_convert(t2)).grid(row=5, column=1,padx=20, pady=20)
    t2 = tk.Text(assist_window, height=1, width=8,bg="#404643",fg="white")
    t2.grid(row=5, column=2,padx=20, pady=20)


def calculator_app():
    calculator.main()


c = tk.Button(bottom_frame, text="Calculator", command=calculator_app,bg="#E4E751")
c.pack(side="left")
a = tk.Button(bottom_frame, text="Assist", command=assist,bg="#E4E751")
a.pack(side="right")

top_frame.pack(fill=tk.BOTH)
middle_frame.pack(side="top", fill=tk.BOTH)
bottom_frame.pack(side="bottom", fill=tk.BOTH)

window.mainloop()
