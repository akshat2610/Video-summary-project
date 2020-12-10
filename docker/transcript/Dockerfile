FROM python:alpine3.7 
RUN apk add build-base 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 3030
ENTRYPOINT [ "python" ] 
CMD [ "transcript_processing_service.py" ] 