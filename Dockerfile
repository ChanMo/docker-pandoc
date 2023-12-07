FROM python:3-slim
MAINTAINER Chan Mo <chan.mo@outlook.com>

WORKDIR /app
COPY pandoc-3.1.7-1-amd64.deb .
RUN dpkg -i pandoc-3.1.7-1-amd64.deb

RUN python3 -m pip install flask gunicorn
COPY app.py .

EXPOSE 5000
RUN mkdir /app/uploads/

CMD ["gunicorn", "-w", "4", "-b", ":5000", "-t", "300", "app:app"]
