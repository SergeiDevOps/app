📜 Flask + Redis app with Docker, CI/CD and Kubernetes

Description
A small web application built with Flask that tracks visits using Redis.  
This pet project was created to practice and demonstrate DevOps engineering skills, including containerization, CI/CD setup, and Kubernetes deployment.

🛠 Tech Stack
- Flask — Python framework for building REST APIs
- Redis — key-value store for tracking visits
- Docker, Docker Compose** — containerization and local development environment
- nginx — reverse proxy server
- Gunicorn — production-grade WSGI HTTP server
- GitHub Actions — CI/CD: linting, building, and deploying the app
- Kubernetes — application deployment in a minimal k8s cluster
- Helm — Kubernetes package manager for manifest templating
- Secrets & .env — environment variables management

✨ Features
- Flask application with Redis as a visit counter
- Dockerized environment with Docker Compose
- CI/CD pipeline configured with GitHub Actions
- Production-ready build with nginx + Gunicorn
- Makefile and bash scripts for easy local development
- Basic Helm chart for Kubernetes deployment (without Ingress or ConfigMaps for simplicity)

🚀 Future Improvements
- Enhanced Helm chart configurations via `values.yaml`
- Add Ingress controller and ConfigMap usage
- Monitoring setup with Prometheus + Grafana
- Centralized logging with ELK stack or Loki
- Expand app logic (authentication, database integration, Celery tasks)

📦 How to Run Locally
```bash
git clone https://github.com/SergeiDevOps/app.git
cd app
docker-compose up --build
![image](https://github.com/user-attachments/assets/df9d56bb-3711-4c10-8d95-536a66a708b2)

