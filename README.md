# Голосовой ассистент преподавателя

## Проект для оценки знаний учеников и студентов.

Для оценки знаний используются следующие технологии:
* ASR (automatic speech recognition) для перевода голоса в текст
* NLP для сравнения близости двух текстов (ответа ученика и правильного ответа).


## Docker

Build docker
```
docker build -t nlp_qa:v1 .
```

Run docker
```
docker run -it -p 5000:5000 -v "$(pwd)":/asr nlp_qa:v1
```
Note, correct running on 127.0.0.1:5000  not docker ip.  
Download [vosk small model](https://alphacephei.com/vosk/models) and put in the project dir.

