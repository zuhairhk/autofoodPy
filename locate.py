import googlemaps
import geocoder
import pandas as pd
import time
import os

def miles_to_metres(miles):
    try:
        return miles * 1609.344
    except:
        return 0

def main(query):

    API_KEY = os.environ['API_KEY']
    map_client = googlemaps.Client(API_KEY)

    #loc = (36.133123, -115.137338)
    g = geocoder.ip('me')
    loc = (g.latlng[0], g.latlng[1])

    search_string = query # input('Enter desired cuisine: ') # 'fries'
    distance = miles_to_metres(5)
    restaruant_list = []

    response = map_client.places_nearby(
        location=loc,
        keyword=search_string,
        # name='fries shop',
        radius=distance
    )

    print(response)

    restaruant_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

    while next_page_token:
        time.sleep(2)
        response = map_client.places_nearby(
            location=loc,
            keyword=search_string,
            # name='fries shop',
            radius=distance,
            page_token=next_page_token
        )
        restaruant_list.extend(response.get('results'))
        next_page_token = response.get('next_page_token')

    df = pd.DataFrame(restaruant_list)
    df['url'] = 'https://www.google.com/maps/place/?q=place_id:' + df['place_id']

    df.to_excel('response_list.xlsx', index=False)
    print(df)

    return restaruant_list