FROM python:3.8-slim-buster
COPY ./app.py .
COPY ./test.py .
COPY ./requirements.txt .
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
