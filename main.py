from datetime import date
import requests
import telebot
import time
from bs4 import BeautifulSoup


TOKEN = "Token bot"
bot = telebot.TeleBot(TOKEN)
id_chat = 12545889

url = " "

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


data = date.today()
pag = requests.get(url, headers=headers)
soup = BeautifulSoup(pag.content, 'html.parser')

graus_celsius = soup.find('span', id='wob_tm').get_text().strip()
chuva = soup.find('span', id='wob_pp').get_text().strip()
umidade = soup.find('span', id='wob_hm').get_text().strip()
vento = soup.find('span', id='wob_ws').get_text().strip()
cidade = soup.find('div', id='wob_loc').get_text().strip()
dia_horas = soup.find('div', id='wob_dts').get_text().strip()
tempo = soup.find('div', id='wob_dcp').get_text().strip()


while True:
    if tempo == 'Tempestades isoladas com raios e trovões':
        bot.send_chat_action(id_chat, 'typing')
        bot.send_message(id_chat, f"⚠⚠ ALERTA ⚠⚠\n\n Alerta de chuva na sua região!!")
        bot.send_chat_action(id_chat, 'typing')
        bot.send_message(id_chat, f"Cidade: {cidade} \nO tempo hoje esta: {tempo}\nTemperatura: {graus_celsius} °C|°F\nChuva: {chuva} \nUmidade: {umidade}\nVento: {vento}\nHoje é {dia_horas}\nAno de {data}")

        print("Cidade:", cidade, '\n'"Hoje esta", tempo, graus_celsius, "°C|°F ", "\nChuva:", chuva, "\nUmidade:", umidade, "\nVento:", vento, "\nHoje é",  dia_horas, "Horas", "Ano de", data)

    else:
        print("Tempo normal")

    if tempo == 'Chuvas com trovoadas':
        bot.send_chat_action(id_chat, 'typing')
        bot.send_message(id_chat, f"⚠⚠ ALERTA ⚠⚠\n\n Alerta de chuva na sua região!!")
        bot.send_chat_action(id_chat, 'typing')
        bot.send_message(id_chat, f"Cidade: {cidade} \nO tempo hoje esta: {tempo}\nTemperatura: {graus_celsius} °C|°F\nChuva: {chuva} \nUmidade: {umidade}\nVento: {vento}\nHoje é {dia_horas}\nAno de {data}")

        print("Cidade:", cidade, '\n'"Hoje esta", tempo, graus_celsius, "°C|°F ", "\nChuva:", chuva, "\nUmidade:", umidade, "\nVento:", vento, "\nHoje é", dia_horas, "Horas", "Ano de", data)

    else:
        print("Tempo normal")

    if tempo == 'Chuvas':
        bot.send_chat_action(id_chat, 'typing')
        bot.send_message(id_chat, f"⚠⚠ ALERTA ⚠⚠\n\n Alerta de chuva na sua região!!")
        bot.send_chat_action(id_chat, 'typing')
        bot.send_message(id_chat, f"Cidade: {cidade} \nO tempo hoje esta: {tempo}\nTemperatura: {graus_celsius} °C|°F\nChuva: {chuva} \nUmidade: {umidade}\nVento: {vento}\nHoje é {dia_horas}\nAno de {data}")

        print("Cidade:", cidade, '\n'"Hoje esta", tempo, graus_celsius, "°C|°F ", "\nChuva:", chuva, "\nUmidade:", umidade, "\nVento:", vento, "\nHoje é", dia_horas, "Horas", "Ano de", data)

    else:
        print("Tempo normal")



    time.sleep(6)
