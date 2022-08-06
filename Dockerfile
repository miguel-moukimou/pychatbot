FROM python:3.9.13-buster

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

COPY . .

RUN pip install nltk==3.7
RUN pip install numpy==1.23.1
RUN pip install tensorflow==2.9.1


RUN python training.py



USER app_user

ENTRYPOINT [ "python", "chatbot.py"]