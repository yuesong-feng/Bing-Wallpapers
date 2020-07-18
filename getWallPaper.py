import os
import requests
import bs4

COUNT = 1


def getWallPaper(n):
    global COUNT
    url = 'https://bing.ioliu.cn/?p=' + str(n)
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64'}
    page = requests.get(url=url, headers=header)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    lists = soup.select('.mark')

    image_lists = []
    for item in lists:
        image_lists.append(str(item)[str(item).index('/'):str(item).index('?')])

    download_urls = []
    for item in image_lists:
        download_urls.append('https://bing.ioliu.cn' + item + '?force=download')

    for download_url in download_urls:
        if os.path.exists('wallpapers/' + download_url[28:download_url.index('_')] + '.jpg'):
            print('壁纸' + str(COUNT) + '已存在')
            COUNT += 1
        if not os.path.exists('wallpapers/' + download_url[28:download_url.index('_')] + '.jpg'):
            image = requests.get(url=download_url, headers=header)
            image_file = open('wallpapers/' + download_url[28:download_url.index('_')] + '.jpg', 'wb')
            image_file.write(image.content)
            print('已下载' + str(COUNT) + '张壁纸')
            COUNT += 1


if not os.path.exists('wallpapers/'):
    os.makedirs('wallpapers/')

n = int(input('一组12张壁纸，您想下载几组：'))
for i in range(1, n + 1):
    getWallPaper(i)
