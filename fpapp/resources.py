import requests
from django.conf import settings


def get_result_for_search(lat, long, page=1):
    url = f"https://www.flickr.com/services/rest/?method=flickr.photos.search&api_key={settings.FLICKR_API_KEY}&lat={lat}&lon={long}&format=json&nojsoncallback=1&per_page=10&page={page}"
    res = requests.get(url=url)
    if res.status_code == 200:
        return res.json()
    return {}
