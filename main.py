import sys
from datetime import datetime, timedelta
from random import randint

sys.path.append('/Users/alan/')
from secret import *
import logging
import requests
from urllib.parse import urlencode

logging.basicConfig(level=logging.INFO, filename="app.log")

def create_graph(id: str):

    endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs"

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    params = {
        "id": id,
        "name": "lbot graph 0",
        "unit": "number",
        "type": "int",
        "color": "shibafu",
        "timezone": "Africa/Johannesburg"
    }

def get_the_graph(id: str):

    endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{id}"

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    response = requests.get(url=endpoint)
    print(response.text)

def update_the_graph(id: str, date: str, value: str):
    endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/{id}"

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    params = {
        "date": date,
        "quantity": value
    }

    response = requests.post(url=endpoint, json=params, headers=headers)
    print(response.json())

def main():
    #update_the_graph("l00", date="20200907", value="1")

    start_date = datetime(2020,4,1)
    end_date = datetime(2021,5,31)

    while start_date <= end_date:
        date = start_date.strftime("%Y%m%d")
        px_value = str(randint(0,7))
        update_the_graph("l00", date=date, value=px_value)
        start_date += timedelta(days=1)


if __name__ == '__main__':
    main()

# logging.debug(stuff)
