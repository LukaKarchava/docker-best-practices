# 1. Start with the optimized, lightweight Python engine
FROM python:3.12-slim

# 2. Set our internal active workspace folder
WORKDIR /app

# 3. Install our web framework package from the internet
RUN pip install flask psycopg2-binary

# 4. Copy our local app script from our laptop into the container
COPY app.py .

# 5. The ignition switch to start our backend service on boot
CMD ["python", "app.py"]
