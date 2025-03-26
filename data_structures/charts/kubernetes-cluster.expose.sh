#  ps aux | grep "kubectl port-forward"

kubectl port-forward -n financial svc/financial-react-service 8080:80 &
kubectl port-forward -n financial svc/financial-go-service 8000:8000 &

ps aux | grep python
