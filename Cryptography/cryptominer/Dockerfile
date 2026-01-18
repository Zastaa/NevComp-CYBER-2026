FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    socat \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -r ctfuser && useradd -r -g ctfuser -s /bin/false ctfuser

WORKDIR /app

COPY ./app .

RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R ctfuser:ctfuser chall.py

USER ctfuser

EXPOSE 1337

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'timeout 5 python3 chall.py'"]