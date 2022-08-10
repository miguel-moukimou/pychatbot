FROM python:3.9.13-buster

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

COPY . .

RUN pip install nltk==3.7
RUN pip install numpy==1.23.1
RUN pip install tensorflow==2.9.1
RUN pip install flask
RUN pip install gunicorn

RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu


RUN python training.py



USER app_user

EXPOSE 5000

#CMD []

#ENTRYPOINT [ "python", "chatbot.py"]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["sh","-c","python3 -m flask run --host 0.0.0.0 --port ${PORT}"]