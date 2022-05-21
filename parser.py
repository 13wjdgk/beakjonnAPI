import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
import django
django.setup()

import requests
from bs4 import BeautifulSoup as bs
from product.models import Product

def Search(num):
	print(num) 	
	url = f'https://www.acmicpc.net/problem/{num}'
	response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
	soup = bs(response.content, "html.parser")
	elements = soup.select('html>head>title')
	Product.objects.all().delete()
	for index, element in enumerate(elements, 1):
		value=(element.text).split(": ")
		try : 
			number=value[0]
			title=value[1]
		except : 
			number="없음"
			title="없음"
		Product(
			Title = title, bjNumber = number
		).save()





