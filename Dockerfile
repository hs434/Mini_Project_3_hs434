FROM python:3.7

ADD . .

RUN pip install --upgrade pip
RUN pip install pipenv

CMD [ "python", "./blog_api/run.py" ]
