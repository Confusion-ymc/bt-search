"""
配置文件区分生产和开发
"""
import os
from importlib import import_module

# 获取环境变量
# env = os.getenv("env", "LOCAL")
# if env == 'PRO':
#     from configs.pro import settings
# else:
#     from configs.local import Settings
#
# settings = Settings(env)
env = os.getenv("ENV", "local")

setting_module = import_module(f'configs.{env.lower()}')
settings = setting_module.Settings()
print(f'-----------{env}启动-----------')
