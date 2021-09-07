FROM python:3.9
RUN pip install --upgrade pip
COPY . /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
EXPOSE 5000
CMD [ "python", "app.py" ]
