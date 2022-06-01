FROM python:3.9
COPY ./app.py .
COPY ./test.py .
COPY ./requirements.txt .
EXPOSE 5000
RUN pip install -r requirements.txt
CMD python app.py
