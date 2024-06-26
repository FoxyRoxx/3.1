import requests
import json

url1 = 'https://fakestoreapi.com/products/categories'
url2 = 'https://fakestoreapi.com/products'

response = requests.get(url2).json()
Flag = False
print(f'Доступные категории: ',"\n" "electronics" "\n" "jewelery" "\n" "men's clothing" "\n" "women's clothing")
request = input('Какую категорию товаров Вы желаете посмотреть?: ')
for i in response:
    if i['category'] == request:
        print(f'ID:{i["id"]}\nTitle:{i["title"]}\nPrice:{i["price"]}\nDescription:{i["description"]}\nCategory:{i["category"]}\nImage:{i["image"]}')
        Flag = True
