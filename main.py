import requests
import datetime
import time

def get_train_info():
    # Upcoming arrival info for specific stop (Damen)
    arrival_url = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx'
    payload = {
        'key':'',
        'mapid':'40590',
        'outputType':'JSON'
        }
    r = requests.get(arrival_url, params=payload)
    full_response = r.json()

    parsed_data = full_response['ctatt'].get('eta')
    ohare_trains = []
    forest_park_trains = []
    now = datetime.datetime.now() - datetime.timedelta(hours=1)

    for item in parsed_data:
        if 'O\'Hare' in item.get('stpDe'):
            arrival_time = datetime.datetime.strptime(item.get('arrT'), '%Y-%m-%dT%H:%M:%S')
            difference = arrival_time - now
            ohare_trains.append(difference.seconds // 60)
        if 'Forest' in item.get('stpDe'):
            arrival_time = datetime.datetime.strptime(item.get('arrT'), '%Y-%m-%dT%H:%M:%S')
            difference = arrival_time - now
            forest_park_trains.append(difference.seconds // 60)

    #print in BART format
    print('O\'Hare', end=' ')
    print(','.join(map(str, ohare_trains)), end = ' ')
    print('MIN')
    print('Forest Park', end=' ')
    print(','.join(map(str, forest_park_trains)), end = ' ')
    print('MIN')

if __name__ == '__main__':
    start_time = time.time()
    while True:
        get_train_info()
        time.sleep(60.0 - ((time.time() - start_time) % 60.0))
        