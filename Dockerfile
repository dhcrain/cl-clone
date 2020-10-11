FROM python:3.5

RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN mkdir /code/static
RUN mkdir /code/media

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 80
