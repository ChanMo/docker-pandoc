FROM python:3-slim
MAINTAINER Chan Mo <chan.mo@outlook.com>

WORKDIR /app
RUN mkdir /app/uploads/
RUN apt-get update -y
RUN apt-get install pandoc -y

RUN python3 -m pip install flask gunicorn
COPY app.py .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", ":5000", "app:app"]
