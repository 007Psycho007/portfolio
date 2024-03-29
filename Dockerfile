FROM python:3.8-slim-buster
WORKDIR /app
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
#Server will reload itself on file changes if in dev mode
ENV FLASK_ENV=production 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY /application .
EXPOSE 5000
CMD ["flask", "run"]
