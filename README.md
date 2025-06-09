
# ML CI/CD Pipeline with Docker & Kubernetes

This project demonstrates a basic Machine Learning CI/CD pipeline using GitHub Actions, Docker, and Kubernetes. The pipeline trains a simple model, evaluates its performance, and deploys it only if it passes accuracy checks.

---

## 📌 Features

- ✅ Train a scikit-learn model (`RandomForestClassifier`) on the Iris dataset.
- ✅ Unit testing using `pytest`
- ✅ Threshold-based performance check (accuracy must be ≥ 0.80)
- ✅ CI pipeline with GitHub Actions
- ✅ Docker containerization of the training pipeline
- ✅ Push Docker image to Docker Hub
- ✅ Kubernetes deployment using `kubectl apply`

---

## 🏗️ Project Structure

```
ml-cicd-lab/
├── train.py                # Train the model
├── evaluate.py            # Evaluate model accuracy
├── check_performance.py   # Abort pipeline if accuracy < 0.80
├── requirements.txt       # Python dependencies
├── Dockerfile             # For building Docker image
├── deployment.yaml        # Kubernetes deployment manifest
├── tests/
│   └── test_training.py   # Unit test for training script
└── .github/
    └── workflows/
        └── ci.yml         # GitHub Actions CI/CD configuration
```

---

## ⚙️ CI/CD Pipeline Flow

### GitHub Actions Workflow

1. 🔍 **Lint/Test**  
   Run unit tests using `pytest`.

2. 🧠 **Train Model**  
   Run `train.py` to save model as `artifacts/model.pkl`.

3. 📈 **Performance Check**  
   Run `evaluate.py` and compare accuracy to 0.80.

4. 🐳 **Docker Deployment**  
   - Build Docker image with the trained model
   - Push to Docker Hub (e.g., `yourusername/ml-model:latest`)

5. ☸️ **Kubernetes Deployment**  
   - Load KUBECONFIG from GitHub Secrets
   - Deploy container using `deployment.yaml`

---

## 🐳 Docker Build & Push (Manual)

```bash
docker build -t yourusername/ml-model:latest .
docker push yourusername/ml-model:latest
```

> Replace `yourusername` with your Docker Hub username.

---

## ☸️ Kubernetes Deployment (Manual)

```bash
kubectl apply -f deployment.yaml
kubectl expose deployment ml-model --type=NodePort --port=80
minikube service ml-model
```

> Requires a running Kubernetes cluster (e.g., Minikube)

---

## 🔐 GitHub Secrets

To enable Docker + Kubernetes in GitHub Actions:

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `KUBECONFIG` – base64 or plaintext kubeconfig content

---

## 📊 Model Details

- Dataset: Iris
- Algorithm: RandomForestClassifier
- Metric: Accuracy (must be ≥ 0.80)

---

## 📌 Notes

- This project is for learning purposes and demonstrates a minimal ML pipeline.
- Deployment logic satisfies common production workflows by combining containerization and orchestration.

---

## 👨‍💻 Author

- Vu Nguyen
