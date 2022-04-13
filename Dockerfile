# Dockerfile для сборки образа проекта распознавания речи
FROM python:3.7.13-slim

# Установка необходимых python-библиотек
RUN pip install --upgrade pip
RUN pip install jinja2==3.0.0
RUN pip install itsdangerous==2.0.1
RUN pip install flask
RUN pip install deeppavlov transformers
RUN python -m deeppavlov install bert_sentence_embedder

EXPOSE 5000
WORKDIR /root/project
ENTRYPOINT ["python"]
CMD ["app.py"]
