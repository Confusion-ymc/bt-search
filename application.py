from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from configs import settings
from configs.local import Settings
from routers.spider import router as api_router


def create_app(app_settings: Settings) -> FastAPI:
    """
    生成FatAPI对象
    :return:
    """

    fastapi_app = FastAPI(
        root_path=app_settings.virtual_path,
        debug=app_settings.debug,
        title=app_settings.title,
        description=app_settings.description,
        docs_url=app_settings.docs_url,
        openapi_url=app_settings.open_api_url
    )
    fastapi_app.state.settings = app_settings

    # 注册路由
    fastapi_app.include_router(api_router)

    # 跨域设置
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    fastapi_app.mount("/css", StaticFiles(directory="static/css"), name="static")
    fastapi_app.mount("/js", StaticFiles(directory="static/js"), name="static")
    fastapi_app.mount("/image", StaticFiles(directory="static/image"), name="static")
    return fastapi_app


app = create_app(settings)
