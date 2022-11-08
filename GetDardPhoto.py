import requests
import json
import ssl
import os
from urllib.request import urlretrieve
ssl._create_default_https_context=ssl._create_unverified_context

if not os.path.exists('./dcardPhoto'):
    os.mkdir('./dcardPhoto')
    
url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=240419961'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
headers = {
    'User-Agent': userAgent
}
res = requests.get(url, headers=headers)
jsonData = json.loads(res)

for articleObject in jsonData:   
    title = articleObject['title']
    articleUrl = 'https://www.dcard.tw/f/mood/p/' + str(articleObject['id'])
    print(title)
    print(articleUrl)
    
    if not os.path.exists('./dcardPhoto/{}'.format(title)):
        os.mkdir('./dcardPhoto/{}'.format(title))
    # get image url
    for n, img in enumerate(articleObject['mediaMeta']):
        imgUrl = img['url']
        resImg = requests.get(imgUrl, headers=headers)
        resContent = resImg.content
        with open('./dcardPhoto/{}/{}.{}'.format(title, n, imgUrl.split('.')[-1]), 'wb') as f:
            f.write(resContent)
        print('\t', imgUrl)
    print('==========', )
