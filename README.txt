Initial Setup
1. > wsl --install -d [distributionName]
    1a. update kernel if necessary
2. > wsl --set-default-version 2
3. install chocolatey package manager
    3a. > https://chocolatey.org/install 
4. install docker desktop
5. choco install kubernetes-cli
    5a. > https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/
6. choco install kind
    6a. > https://kind.sigs.k8s.io/docs/user/quick-start/

> kind create cluster --config kind-ingress.yaml

> kubectl delete pod pyserver --now

> docker build -t localhost:5000/pyserver:0.1 .

> kind load docker-image localhost:5000/pyserver:0.1 

> kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml

> kubectl apply -f service.yaml

> kubectl port-forward service/pyserver 8080:8080