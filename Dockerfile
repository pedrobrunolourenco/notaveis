FROM python:3.10-slim

WORKDIR /app

COPY requerimentos.txt .

RUN pip install --no-cache-dir -r requerimentos.txt

COPY . .

EXPOSE 8181


CMD ["flask", "run", "--host=0.0.0.0","--port=8181"]


#docker build -t api-notaveis .
#docker run -d -p 8181:8181 api-notaveis
#funciona com a porta 8080, 8181, 5000 tentar outras (nao funcionou com a 6000 por exemplo, considera insegura)
