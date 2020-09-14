FROM python:3.7.2

COPY . /app

WORKDIR /app

RUN pip install pipenv \
&& pipenv install --system --deploy --ignore-pipfile 
#use --dev flag for development environment

CMD python main.py



