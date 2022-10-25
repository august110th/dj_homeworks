FROM python:3.8

WORKDIR /usr/src/3.2-crud

COPY ./requirements.txt /usr/src/3.2-crud/stocks_products/
RUN pip install -r /usr/src/3.2-crud/stocks_products/requirements.txt

COPY . /usr/src/3.2-crud
RUN pip install django-filter

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
