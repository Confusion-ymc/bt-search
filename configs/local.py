from starlette.templating import Jinja2Templates


class Settings:
    title: str = "BT Search"
    virtual_path = ''
    description: str = "<h1>BT Search</h1>"
    # 文档地址 默认为docs
    open_api_url: str = "/openapi.json"
    docs_url: str = "/swagger"

    debug = False
    # proxies = {'http': '127.0.0.1:41091', 'https': '127.0.0.1:41091'}
    proxy = 'http://127.0.0.1:11801'
    templates = Jinja2Templates(directory='templates')
