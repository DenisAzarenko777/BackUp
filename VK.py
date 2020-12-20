import json

import requests


class VK_response():
    def __init__(self, token: str) -> None:
        self.token = token

    def response(self):
        VK_response = requests.get('https://api.vk.com/method/photos.get',
                                   params={
                                       "access_token": self.token,
                                       "count": '1000',
                                       "album_id": "profile",
                                       "photo_sizes": 1,
                                       "v": 5.122,
                                       "extended": 1,
                                   }).json()
        with open('response.json', 'w') as file:
            json.dump(VK_response, file, indent=2, ensure_ascii=False)

    def get_largest(self, size_dict):
        if size_dict['width'] >= size_dict['height']:
            return size_dict['width']
        else:
            return size_dict['height']

    def download_photo(self, url, j):
        p = requests.get(url)
        out = open(f"Dir/{j}.jpg", "bw")
        out.write(p.content)
        out.close()
