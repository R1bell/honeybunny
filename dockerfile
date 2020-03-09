FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt ./
RUN apk add --no-cache gcc libc-dev postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./ ./

EXPOSE 5000
ENTRYPOINT [ "python", "manage.py" ]
CMD [ "run" ]