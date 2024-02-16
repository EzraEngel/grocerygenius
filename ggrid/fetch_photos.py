import requests
import shutil
from ggrid.models import Category
import time

def fetch_image(query, pk):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "client_id": "y3RuxbSYYarspf4h0Tq9VBedG7Og0qWXS_TKUEFj1-Q"
    }
    response = requests.get(url, params=params).json()
    print(response)
    image_url = response['results'][0]['urls']['regular']

    # Download and save the image
    response = requests.get(image_url, stream=True)
    with open('media/'+str(pk)+'.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


for category in Category.objects.all()[:3]:
    time.sleep(1)
    fetch_image(category.name, category.id)
