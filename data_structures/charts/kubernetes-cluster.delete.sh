kubectl delete svc financial-go-service -n financial
kubectl delete svc financial-react-service -n financial
kubectl delete svc financial-python-service -n financial
kubectl delete svc traefik -n financial

kubectl delete Deployment financial-go-server -n financial
kubectl delete Deployment financial-react-app -n financial
kubectl delete Deployment financial-python-server -n financial
kubectl delete  Deployment traefik -n financial

helm uninstall traefik --namespace financial

kubectl get svc -n financial 
kubectl get deployments -n financial 
kubectl get pods -n financial 
