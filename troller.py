#!/usr/bin/env python

import argparse
from urllib.parse import urlparse
import requests
from time import sleep
from random import randint
from faker import Faker

def delay_type(d):
	d = int(d)
	if d < 0:
		raise argparse.ArgumentTypeError("Minimum delay is 0")
	return d

def url_type(u):
	parsed_url = urlparse(u)
	if not(bool(parsed_url.scheme)):
		raise argparse.ArgumentTypeError("URL invalida")
	return u

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True, action='store', help="URL DONDE METER LOS DATOS FAKE JAJA", type=url_type)
parser.add_argument('-fu', '--form-user', required=True, action='store', help="INPUT DEL FORMULARIO PARA EL USERNAME O EMAIL", type=str)
parser.add_argument('-fp', '--form-password', required=True, action='store', help="INPUT DEL FORMULARIO PARA EL PASSWORD", type=str)
parser.add_argument('-d', '--delay', required=False, action='store', help="Delay entre inyecciones en milisegundos", type=delay_type)
args = parser.parse_args()

url = args.url
form_user = args.form_user
form_password = args.form_password
delay = args.delay

faker = Faker()

print("Comenzando metodo POST ;)")
print()

try:
	while True:
		payload = {
			form_user: faker.email(),
			form_password: faker.password(length = randint(8, 12))
		}

		response = requests.request("POST", url, headers = [], data = payload, files = [])

		print(str(response.status_code) + ': ' + payload[form_user] + ' | ' + payload[form_password])

		if delay != None and delay > 0:
			sleep(delay / 100)

except KeyboardInterrupt:
	print()
	print("adioooooo")
