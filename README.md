# Голосовой ассистент преподавателя

## Проект для оценки знаний учеников и студентов.

Для оценки знаний используются следующие технологии:
* ASR (automatic speech recognition) для перевода голоса в текст - [vosk+pykaldi](https://alphacephei.com/vosk/server)
* NLP для сравнения близости двух текстов (ответа ученика и правильного ответа) - [DeepPavlov](https://deeppavlov.ai/).


## Запуск приложения
Скачайте и скопируйте содержимое архива с моделью [rubert](http://files.deeppavlov.ai/deeppavlov_data/bert/rubert_cased_L-12_H-768_A-12_pt.tar.gz) в папку ```project/rubert```   

Из папки проекта ```nlp_qa``` запустите приложение командой:  

```
docker-compose up
```

Откройте браузер по ссылке [localhost:5000](127.0.0.1:5000) .
