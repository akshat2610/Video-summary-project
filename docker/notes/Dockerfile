FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 3030
ENTRYPOINT [ "python" ] 
CMD [ "notes_service.py" ] 