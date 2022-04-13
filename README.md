# Голосовой ассистент преподавателя

## Проект для оценки знаний учеников и студентов.

Для оценки знаний используются следующие технологии:
* ASR (automatic speech recognition) для перевода голоса в текст - [vosk+pykaldi](https://alphacephei.com/vosk/server)
* NLP для сравнения близости двух текстов (ответа ученика и правильного ответа) - [DeepPavlov](https://deeppavlov.ai/).


## Запуск приложения

```
docker-compose up
```

Note, correct running on 127.0.0.1:5000 , not on the docker ip.  
