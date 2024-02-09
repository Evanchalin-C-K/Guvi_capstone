import requests


def fetch_data(url):
    return requests.get(url).json()


def check_status_code(url):
    return requests.get(url).status_code


def insert_data(url, data):
    return requests.post(url, data)


def update_data(url, data):
    return requests.put(url, data)


def delete_data(url):
    return requests.delete(url)
