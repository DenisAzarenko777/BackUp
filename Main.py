import datetime
import json
import time

from progress.bar import IncrementalBar

from VK import VK_response
from Yandex import Yandex

t = <"Мой токен">
TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"

if __name__ == '__main__':
    now = datetime.datetime.now()
    User = VK_response(token=TOKEN)
    User.response()
    photos = json.load(open('response.json'))['response']['items']
    test_list = []
    info_file = []
    file_dict = {}
    bar = IncrementalBar('Photo download', max=len(photos))
    for photo in photos:
        sizes = photo['sizes']
        likes = photo['likes']
        max_size = max(sizes, key=User.get_largest)['url']
        likess = max(sizes, key=User.get_largest)
        like = photo['likes']['count']
        if like in test_list:
            l = str(like) + str(now)[:-15]
        else:
            l = like
        file_dict['file_name'] = l
        file_dict['size'] = max(sizes, key=User.get_largest)['type']

        info_file.append(file_dict)
        User.download_photo(max_size, l)
        test_list.append(like)
        bar.next()
        time.sleep(1)
    with open('data.json', 'w') as f:
        json.dump(info_file, f, indent=2)
    Yan = Yandex(token=t)
    Yan.load()
    bar.finish()
    print(info_file)
