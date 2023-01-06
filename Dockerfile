FROM python:3.7.6

WORKDIR /code/

ADD requirements.txt /code/
RUN if [ "$build_env" = "DEV" ] ; then pip config set global.index-url https://mirrors.aliyun.com/pypi/simple ; fi
RUN pip install -r requirements.txt
ADD . /code



CMD ["python3", "-u", "main.py"]

