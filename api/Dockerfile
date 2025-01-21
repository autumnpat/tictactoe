FROM python:3.9-slim
#TODO: Before production let's move this to alpine so we're not stuck with python's choices

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]