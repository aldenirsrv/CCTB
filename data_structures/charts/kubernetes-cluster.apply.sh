kubectl apply -f ms-go/ -n financial
kubectl apply -f python-ms/ -n financial
kubectl apply -f frontend/ -n financial

sleep 2
kubectl get pods -n financial
kubectl top pods -n financial
sleep 2
kubectl apply -f ingress.yaml -n financial

helm repo add traefik https://traefik.github.io/charts
helm repo update
sleep 1
helm install traefik traefik/traefik -n financial
sleep 2
kubectl apply -f traefik-ingressroute.yaml -n financial
sleep 2
kubectl apply -f traefik-loadbalancer.yaml

