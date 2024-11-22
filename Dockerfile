FROM python:3.10

RUN pip install typing-extensions
RUN pip install dict2xml
RUN pip install dicttoxml
RUN pip install connexion[flask] connexion[swagger-ui] connexion[uvicorn]
RUN pip install flask-restplus
RUN pip install Flask

COPY ./Src /Src
COPY ./Docs /Docs
COPY ./Requests /Requests
COPY ./Datasets /Datasets
COPY ./main.py .
COPY ./swagger.yaml .

CMD ["python", "main.py"]