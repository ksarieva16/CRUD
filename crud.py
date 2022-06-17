
import requests
import json
from settings import settings


class CRUD():
    

    def list_records(self):
       
        print('Listing records...')
        req = requests.get(settings.get_url + settings.LIST_RECORDS_URL, headers=settings.AUTH_TOKEN_HEADER)
        return req.json()

    def retrieve_record(self, id_):
     
        print('Retrieving record...')
        req = requests.get(settings.get_url + f'/{id_}', headers=settings.AUTH_TOKEN_HEADER)
        return req.json()

    def create_record(self):
    
        print('Creating record...')
        data = {
            'fields': {
                'brand': input('Введите название автомобиля: '), 
                'model': input('Введите модель автомобиля: '), 
                'year_of_vypusk': int(input('Введите год выпуска автомобиля: ')), 
                'obem': float(input('Введите объем двигателя автомобиля: ')), 
                'color': input('Введите цвет автомобиля: '), 
                'probeg':  int(input('Введите пробег автомобиля: ')), 
                'price': int(input('Введите цену автомобиля: ')), }}

        req = requests.post(settings.get_url, headers=settings.AUTH_TOKEN_HEADER, data=json.dumps(data))
        return req.json()

    def update_record(self, id_ ):
        
        print('Updating record...')
       
        data =  {'records': [{'id': id_, 'fields': {
                'brand': input('Введите название автомобиля: '),
                'model': input('Введите модель автомобиля: '),
                'year_of_vypusk': int(input('Введите год выпуска автомобиля: ')),
                'obem': float(input('Введите объем двигателя автомобиля: ')), 
                'color': input('Введите цвет автомобиля: '),
                'probeg':  int(input('Введите пробег автомобиля: ')), 
                'price': float(input('Введите цену автомобиля: '))}}]}

        req = requests.patch(settings.get_url, headers=settings.AUTH_TOKEN_HEADER, data=json.dumps(data))
        return req.json()


    def delete_record(self, id_):
     
        print('Deleting record...')
        req = requests.delete(settings.get_url + f'/{id_}', headers=settings.AUTH_TOKEN_HEADER)
        return req.json()


