from flickrapi import FlickrAPI
from datetime import datetime
import SQL

API_KEY = 'XXXXX'
API_SECRET = 'XXXXX'

flickr = FlickrAPI(api_key=API_KEY, secret=API_SECRET, format='parsed-json', cache=False)

# method 1
def scrape(keyword, size):
    data = flickr.photos.search(api_key=API_KEY, text=keyword, per_page=size)

    list_of_id = []
    for photo in data['photos']['photo']: # Get the id for each photo
        list_of_id.append(photo['id'])

    Urls = []
    Scrape_times = []

    for photo_id in list_of_id:
        url = flickr.photos.getInfo(api_key=API_KEY, photo_id=photo_id)

        Current_time = datetime.now()
        Current_time = Current_time.strftime("%Y-%m-%d %H:%M:%S")
        Scrape_times.append(Current_time)

        # get the url for each photo
        Urls.append(url['photo']['urls']['url'][0]['_content'])

    # Call 'create_data_base' function from SQL file
    SQL.create_data_base(Urls, Scrape_times, keyword)


scrape('food', 20) # For test
