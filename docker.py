docker_text = """
FROM python3.8

COPY . /src

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

"""