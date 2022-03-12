# Dockerfile для сборки образа проекта распознавания речи
FROM pykaldi/pykaldi

# Настройка окружения
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/kaldi/src/featbin:/kaldi/src/ivectorbin:/kaldi/src/online2bin:/kaldi/src/rnnlmbin:/kaldi/src/fstbin:$PATH
ENV LC_ALL C.UTF-8
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install -y llvm-8 ffmpeg
RUN LLVM_CONFIG=/usr/bin/llvm-config-8 pip3 install enum34 llvmlite numba

# Установка необходимых python-библиотек
RUN pip install --upgrade pip \
	tqdm \
	pandas \
	matplotlib \
	seaborn \
	librosa \
	sox \
	pysubs2 \
	flask \
	soundfile

RUN pip install vosk
RUN pip install deeppavlov transformers
RUN python -m deeppavlov install bert_sentence_embedder

EXPOSE 5000
WORKDIR /asr/project
ENTRYPOINT ["python"]
CMD ["app.py"]
