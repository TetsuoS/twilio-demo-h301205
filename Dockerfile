FROM python:3.6

RUN mkdir /twilio
WORKDIR /twilio

COPY say.py .
COPY call.py .

RUN pip install twilio --target .
RUN pip install Flask --target .

EXPOSE 5000
