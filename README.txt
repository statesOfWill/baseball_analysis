Initial Setup and Deployment
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
7. create local docker registry
    7a. > ./local-registry.sh
8. build docker image for app
    8a. > docker build -t localhost:5000/pyserver:0.1 .
9. push docker image to local docker registry
    9a. > docker push localhost:5000/pyserver:0.1 or kind load docker-image localhost:5000/pyserver:0.1  
10. create kind-ingress.yaml
11. create local kind cluster 
     11a. > kind create cluster --config kind-ingress.yaml
12. connect local kind cluster to local docker registry
    12a. > docker network connect "kind" "kind-registry"
13. deploy Nginx ingress controller
    13a. > kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml
14. create service.yaml
15. deploy service to local kind cluster
    15a. > kubectl apply -f service.yaml

Deployment cycle
1. update application code
2. build new docker image
3. disconnect kind cluster from kind registry
    3a. > docker network disconnect "kind" "kind-registry"
4. push new docker image to kind registry 
5. re-connect kind cluster to kind registry
    5a. > docker network connect "kind" "kind-registry"
6. deploy service to local kind cluster
    6a. > kubectl apply -f service.yaml