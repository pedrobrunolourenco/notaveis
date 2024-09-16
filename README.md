# Componente - Api-Notaveis
 MicroService para Cruid de notáveis

## 1. Objetivo
Post, Put, Gets e Delete de Notáveis

## 3. Referência Técnica
- Esta API foi desenvolvida em **Phyton** faz uso do seu próprio **Dockerfile** e de seu próprio Repositório em **SQLLite**, ORM **Sqlalchemy**, o banco com sua respectiva tabela será gerado automaticamente;

## 4. Subindo o componente Api-Notaveis
### 4.1
- Abrir um novo terminal na pasta do projeto (onde se encontra o arquivo Dockerfile).
### 4.3 - Executar os comandos abaixo
   ```sh
   docker build -t api-notaveis .
   docker run -d -p 8181:8181 api-notaveis
   ```
- Feito isso a documentação do componente **Api-Notaveis** é disponibilizada em `localhost:8181`.
