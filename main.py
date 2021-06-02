import requests
import datetime

# Upcoming arrival info for specific stop (Damen)
arrival_url = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx'
payload = {
    'key':'insert_key_here',
    'mapid':'40590',
    'outputType':'JSON'
    }
r = requests.get(arrival_url, params=payload)
full_response = r.json()

parsed_data = full_response['ctatt'].get('eta')

next_train = parsed_data[0]
following_train = parsed_data[1]
date_time_next = datetime.datetime.strptime(next_train['arrT'], '%Y-%m-%dT%H:%M:%S')
date_time_following = datetime.datetime.strptime(following_train['arrT'], '%Y-%m-%dT%H:%M:%S')

print('Next train: ' + next_train['stpDe'])
print('Arriving at: ', date_time_next.strftime("%I:%M %p"))
print('\n')
print('Following train: ' + following_train['stpDe'])
print('Arriving at: ', date_time_following.strftime("%I:%M %p"))