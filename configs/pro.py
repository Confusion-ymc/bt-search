from starlette.templating import Jinja2Templates


class Settings:
    title: str = "BT Search"
    virtual_path = ''
    description: str = "<h1>BT Search</h1>"
    # 文档地址 默认为docs
    open_api_url: str = "/openapi.json"
    docs_url: str = "/swagger"

    debug = False
    proxy = None
    templates = Jinja2Templates(directory='templates')
