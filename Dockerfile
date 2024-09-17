FROM python:3.10-slim

WORKDIR /app

COPY requerimentos.txt .

RUN pip install --no-cache-dir -r requerimentos.txt

COPY . .

EXPOSE 8181

VOLUME ["/app/database"]

CMD ["flask", "run", "--host=0.0.0.0","--port=8181"]


#docker build -t api-notaveis .
#docker run -d -v notaveis_volume:/app/database -p 8181:8181 api-notaveis
