import json

import aiohttp

from configs import settings


def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    else:
        return False


async def aio_request(url, method='GET', **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.request(method=method, url=url, **kwargs, proxy=settings.proxy) as response:
            return await response.text()


async def trans_to_en(search_text):
    url = 'http://front-gateway.mtime.com/mtime-search/search/unionSearch2'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "front-gateway.mtime.com",
        "Origin": "http://film.mtime.com",
        "Pragma": "no-cache",
        "Referer": "http://film.mtime.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
    }
    params = {
        "keyword": search_text,
        "pageIndex": 1,
        "pageSize": 20,
        "searchType": 0,
        "locationId": 290,
        "genreTypes": '',
        "area": '',
        "year": ''
    }
    try:
        res = json.loads(await aio_request(url=url, method='POST', headers=headers, data=params))
        en_search_text = res['data']['movies'][0]['nameEn']
        print(f'search {search_text} --->> {en_search_text}')
        return en_search_text
    except:
        return search_text


if __name__ == '__main__':
    trans_to_en('毒液2')
