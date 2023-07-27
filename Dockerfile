FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./app /app

RUN pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple \
&& pip config set global.trusted-host mirrors.cloud.tencent.com \
&& pip install --upgrade pip \
&& pip install --user requests
&& pip install --user json