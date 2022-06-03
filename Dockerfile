FROM python:3.9
COPY ./app.py .
COPY ./test.py .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
