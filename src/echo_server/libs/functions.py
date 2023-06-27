import os
import requests

def get_env():
    try:
        return  os.environ['SYS_ENV']
    except KeyError:
        return 'SYS_ENV environment variable not set'

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/147.229.2.90/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data