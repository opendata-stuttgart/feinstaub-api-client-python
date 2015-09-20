import requests
from config import API_TOKEN


def get_data():
    header = {'Authorization': 'Token ' + API_TOKEN}
    session = requests.Session()
    url = "https://api.dusti.xyz/v1/node/"
    r = session.get(url, headers=header)
    for node in r.json():
        for sensor in node.get('sensors'):
            print("sensor_id: {}".format(sensor.get('id')))


if __name__ == '__main__':
    get_data()
