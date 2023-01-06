import traceback

from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import JSONResponse

from lib.tools import check_contain_chinese, trans_to_en
from spider import hdw
from configs import settings

router = APIRouter()


@router.get("/")
def index(request: Request):
    return settings.templates.TemplateResponse('index.html', {"request": request})


@router.get("/result/")
async def search_api(request: Request, search: str):
    if check_contain_chinese(search):
        search = await trans_to_en(search)
    try:
        data_list = await hdw.search(search)
    except Exception as e:
        traceback.print_exc()
        return JSONResponse({'data': [], 'message': str(e)})
    return JSONResponse({'data': data_list, 'message': 'success'})
