FROM python:3.10-slim


WORKDIR /app


COPY user_configuration_manager.py .

CMD ["python", "user_configuration_manager.py"]
