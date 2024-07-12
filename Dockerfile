FROM python:3.11

#Expose Port 8501 for app to be run on
EXPOSE 8501

#Set Working Directory
WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
RUN pip install -U pip setuptools.txt
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

COPY . .

CMD streamlit run app.py
