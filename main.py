import datetime
import requests
import asyncio
import os
import sys
import PyQt5
from sampel import Ui_Form
from PyQt5 import QtWidgets
from PyQt5 import uic

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


def pushbotton():
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    api_key = 'f039fbd75b1dc47f381248ddae467482'
    city = ui.lineEdit.text()
    url = base_url + 'appid=' + api_key + '&q=' + city
    respore = requests.get(url).json()
    temp_kelvin = respore['main']
    temp_kelvin1 = temp_kelvin['temp']
    temp_kelvin2 = round(temp_kelvin1 - 273.15)
    temp_kelvin3 = str(temp_kelvin2)
    ui.label.setText(temp_kelvin3 + '°С')
    weather = respore['weather']
    weather1 = weather[0]
    weather2 = weather1['main']
    weather3 = 'Weather:' + weather2
    ui.label_2.setText(weather3)
    wind = respore['wind']
    wind1 = wind['speed']
    wind2 = 'Wind:' + str(wind1) + 'km/h'
    ui.label_3.setText(wind2)
    visibily = respore['visibility']
    visibily1 = visibily / 1000
    ui.label_4.setText('Visibility:' + str(visibily1) + 'km')
    country = respore['sys']
    country1 = country['country']
    ui.label_5.setText('Country:' + country1)


ui.pushButton.clicked.connect(pushbotton)

sys.exit(app.exec_())
