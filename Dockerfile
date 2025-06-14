# ---- Build Frontend ----
FROM node:18-alpine AS frontend
WORKDIR /app/frontend
COPY frontend/ ./
RUN npm install && npm run build

# ---- Build Backend ----
FROM python:3.10-slim AS backend
WORKDIR /app/backend

# Install backend dependencies
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source
COPY backend/ ./

# Copy frontend build into backend static folder
COPY --from=frontend /app/frontend/dist /app/backend/static

# ---- Final Image ----
FROM python:3.10-slim
WORKDIR /app

COPY --from=backend /app/backend /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

EXPOSE 5000
CMD ["python", "app.py"]