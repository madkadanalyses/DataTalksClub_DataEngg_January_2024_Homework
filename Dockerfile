FROM python:3.9.1

#RUN pip install pandas
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
#COPY pipeline.py pipeline.py
#WORKDIR /app
#COPY ingest_data.py ingest_data.py
#COPY Homework_GreenTaxi_Injection.py Homework_GreenTaxi_Injection.py
COPY Homework_lookup_injection.py Homework_lookup_injection.py

#ENTRYPOINT [ "bash" ]
#ENTRYPOINT [ "python", "pipeline.py" ]
#ENTRYPOINT [ "python", "ingest_data.py" ]
#ENTRYPOINT [ "python", "Homework_GreenTaxi_Injection.py"]
ENTRYPOINT [ "python", "Homework_lookup_injection.py" ]
