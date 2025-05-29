FROM registry.redhat.io/ubi9/python-311

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY payload.json .

COPY mcp_server.py ./

# TODO don't commit this file to built image
COPY sensetive_data.py ./

CMD ["python", "mcp_server.py"]
