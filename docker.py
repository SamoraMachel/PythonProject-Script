docker_text = """
FROM python:3.8

COPY . /project

COPY ./requirements.txt /project/requirements.txt

WORKDIR /project

RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]

"""