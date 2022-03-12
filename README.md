# Голосовой ассистент преподавателя

## Проект для оценки знаний учеников и студентов.

Для оценки знаний используются следующие технологии:
* ASR (automatic speech recognition) для перевода голоса в текст - [vosk+pykaldi](https://alphacephei.com/vosk/)
* NLP для сравнения близости двух текстов (ответа ученика и правильного ответа) - [DeepPavlov](https://deeppavlov.ai/).


## Docker

Build docker
```
docker build -t nlp_qa:v1 .
```

Run docker flask app
```
docker run -it -p 5000:5000 -v "$(pwd)":/asr nlp_qa:v1
```
Note, correct running on 127.0.0.1:5000 , not on the docker ip.  


Download [vosk small model](https://alphacephei.com/vosk/models) and put it in the project dir.    

Run docker CLI  
```
docker run --rm -it --entrypoint bash  -v "$(pwd)":/asr nlp_qa:v1
```