import re
from urllib import parse
from lib.tools import aio_request


async def search(search_text):
    search_text = parse.quote(search_text)
    url = f"https://thepiratebay0.org/search/{search_text}/1/99/200"
    headers = {
        'referer': url,
        'sec-ch-ua': 'Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78"
    }
    res = await aio_request(url, headers=headers)
    magnet_list = re.findall('''title="Details for (.*?)"[\w\W]*?<a href="(magnet:.*?)"''', res)
    return magnet_list
