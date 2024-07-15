# qa-test

**Kubernetes Deployment:**

- Install kubectl `curl.exe -LO "https://dl.k8s.io/release/v1.30.0/bin/windows/amd64/kubectl.exe"`
- Create frontend cluster `kubectl apply -f path/to/your/backend-deployment.yaml`
- Create frontend cluster `kubectl apply -f path/to/your/frontend-deployment.yaml`
- Port Fowarding `kubectl port-forward service/backend-service 3000`
  

