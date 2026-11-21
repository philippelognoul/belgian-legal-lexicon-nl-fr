FROM python:3.12-slim
WORKDIR /app
COPY data /app/data
COPY mcp /app/mcp
RUN pip install --no-cache-dir /app/mcp
ENV LEXICON_PATH=/app/data/lexicon.jsonl
CMD ["belgian-legal-lexicon-mcp"]
