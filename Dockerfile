FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8


RUN mkdir -p /usr/local/app
WORKDIR /usr/local/app

COPY ./src/ .
RUN chown -R nobody:nogroup .

USER nobody
EXPOSE 8090

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090", "--proxy-headers" ]

