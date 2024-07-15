# Instructions

**Kubernetes Deployment:**

- Install kubectl `curl.exe -LO "https://dl.k8s.io/release/v1.30.0/bin/windows/amd64/kubectl.exe"`
- Create frontend cluster `kubectl apply -f path/to/your/backend-deployment.yaml`
- Create frontend cluster `kubectl apply -f path/to/your/frontend-deployment.yaml`
- Port Fowarding `kubectl port-forward service/backend-service 3000`

**Running Test File**

- Install Requirements: `pip install -r requirementes.txt`
- Run the python script: `python integration_test.py`
- Script has 2 methods `verification_success()` and `verification_failed()`
- `verification_success()`: Comparing backend message with the frontend message
- `verification_failed()`: Comparing backend message with random string 
