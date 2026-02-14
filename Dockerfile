FROM python:3.12-alpine3.21

WORKDIR /bot

COPY . .

RUN pip install --no-cache-dir -r bot/requirements.txt

EXPOSE 8000

ENTRYPOINT [ "sh", "bot/entrypoint.sh" ]