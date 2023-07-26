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


def push_bottom():
    try:
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        api_key = 'f039fbd75b1dc47f381248ddae467482'
        city = ui.lineEdit.text()
        res_pore = requests.get(base_url + 'appid=' + api_key + '&q=' + city).json()
        temp = str(round(res_pore['main']['temp'] - 273.15))
        ui.label.setText(temp + '°С')
        weather = 'Weather:' + res_pore['weather'][0]['main']
        ui.label_2.setText(weather)
        wind = 'Wind:' + str(res_pore['wind']['speed']) + 'km/h'
        ui.label_3.setText(wind)
        visibility = res_pore['visibility'] / 1000
        ui.label_4.setText('Visibility:' + str(visibility) + 'km')
        country = res_pore['sys']['country']
        ui.label_5.setText('Country:' + country)
    except KeyError:
        ui.lineEdit.setText('Invalid location :/')


ui.pushButton.clicked.connect(push_bottom)
sys.exit(app.exec_())
