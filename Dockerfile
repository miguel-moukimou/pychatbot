FROM python:3.9.13-buster

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


RUN python training.py



USER app_user

ENTRYPOINT [ "python", "chatbot.py"]