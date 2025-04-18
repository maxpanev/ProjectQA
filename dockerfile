FROM python:3.12-alpine
ENV PYTHONBUFFERED=1
WORKDIR /python-app
COPY . .
RUN pip install pytest
CMD ["python", "project.py"]