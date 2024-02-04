FROM python:3.12.0-alpine

WORKDIR /app

COPY . /app

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5555", "main:app"]
