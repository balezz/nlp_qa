# Dockerfile для сборки образа проекта распознавания речи
FROM python:3.7.13-slim

WORKDIR /root

# Установка необходимых python-библиотек
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python -m deeppavlov install bert_sentence_embedder

COPY . .
WORKDIR /root/project
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
