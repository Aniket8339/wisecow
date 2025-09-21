# Wisecow Application
## Quick Start
```bash
# Local run
chmod +x wisecow.sh
./wisecow.sh

# Docker
docker build -t wisecow .
docker run -p 4499:4499 wisecow

# Kubernetes
kubectl apply -f k8s/

# Test
curl http://localhost:4499