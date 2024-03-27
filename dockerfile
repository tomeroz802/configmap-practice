
FROM python
WORKDIR /app
COPY requirements.txt /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 81
CMD [ "python", "main.py" ]