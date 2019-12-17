FROM python:3.7

ADD . .

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install pytest-cov pytest

CMD [ "python", "./blog_api/run.py" ]
