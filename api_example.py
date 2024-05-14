import requests
import pandas as pd

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

# a function is much better to call the API once and store its results in the json format instead of requesting the server again and again

def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl+endpoint+ f'?page={x}')
    return r.json()

# how many functions to loop through to get to the actual something
def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    '''to change the below code line to a function instead:
    name = data['results'][0]['name']
    and not to hard code it
    '''
    character_list = []  # making a list of dictionary
    for item in response['results']:
        characters = {
            'id': item['id'],
            'name': item['name'],
            'no_ep': len(item['episode']),
                    }
        character_list.append(characters)
    #     populating a dictionary using the items obtained from the response
    return character_list

main_list = []
data = main_request(baseurl, endpoint, 2)
print(get_pages(data))
shape_of_data = len(data.keys()) # to get the idea of the type of data we are fetching and the shape of dictionary

for x in range(1, get_pages(data)+1):
    print(x)
    main_list.extend(parse_json(main_request(baseurl, endpoint, x)))

data_frame = pd.DataFrame(main_list)
data_frame.to_csv('characterlist.csv', index=False)