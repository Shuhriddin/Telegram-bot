import json
import requests


def weather(shahar):
	url = "https://yahoo-weather5.p.rapidapi.com/weather"

	querystring = {"location": shahar, "format": "json", "u": "f"}

	headers = {
		"X-RapidAPI-Key": "f58e77f924mshd38e85dfe987eb3p11aaf7jsnbb93ac53a54d",
		"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	data = json.loads(response.text)
	harorat = (data["current_observation"]["condition"]["temperature"] - 32) * 5 / 9
	result = f'Manzil : {data["location"]["city"]}, {data["location"]["country"]}\n' \
			 f'Quyosh chiqish vaqti : {data["current_observation"]["astronomy"]["sunrise"]}\n' \
			 f'Quyosh botish vaqti : {data["current_observation"]["astronomy"]["sunset"]}\n' \
			 f'Ob-havo: {"{:.2f}".format(harorat)}'

	return result

