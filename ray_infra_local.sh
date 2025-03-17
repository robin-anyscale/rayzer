#!/bin/bash
# quick-launch.sh

# Function to clean up background processes on script exit
cleanup() {
    echo "Cleaning up..."
    kill $PORT_FORWARD_PID 2>/dev/null
    kubectl delete -f ray-cluster-autoscaler.yaml
}

# Set up cleanup trap
trap cleanup EXIT


# echo "Installing Prometheus stack..."
# /Users/robin/source/anyscale/kuberay/install/prometheus/install.sh

sleep 5

# Apply Ray cluster configuration
echo "Applying Ray cluster configuration..."
kubectl apply -f ray-cluster-autoscaler.yaml

# sleep 1

# Wait for the pod to be ready
echo "Waiting for Ray head pod to be ready..."
kubectl wait --for=condition=ready pod -l ray.io/node-type=head --timeout=120s

echo "Starting port forwarding for Ray dashboard..."
export HEAD_POD=$(kubectl get pods --selector=ray.io/node-type=head -o custom-columns=POD:metadata.name --no-headers)
kubectl port-forward $HEAD_POD -n default 8265:8265&
RAY_PORT_FORWARD_PID=$!

# sleep 1

# Start port forwarding in the background
echo "Starting port forwarding for code server..."
kubectl port-forward svc/coder-service 9999:9999 &
CODE_PORT_FORWARD_PID=$!

echo "Starting port forwarding for grafana dashboard..."
kubectl port-forward ${HEAD_POD} 8080:8080 &
GRAFANA_PORT_FORWARD_PID=$!

# sleep 1



# sleep 1


echo "Starting port forwarding for prometheus dashboard..."
kubectl port-forward prometheus-prometheus-kube-prometheus-prometheus-0 -n prometheus-system 9090:9090 &
PROMETHEUS_PORT_FORWARD_PID=$!

# sleep 1

echo "Starting port forwarding for prometheus-grafana dashboard..."
kubectl port-forward deployment/prometheus-grafana -n prometheus-system 3000:3000 &
PROMETHEUS_GRAFANA_PORT_FORWARD_PID=$!

open "http://localhost:9999/?folder=/home/ray"
sleep 1
open "http://localhost:8265/#/cluster"

echo "Ray cluster is ready!"
echo "Code server is available at http://localhost:9999"
echo "Press Ctrl+C to clean up and exit"

# Keep script running until interrupted
wait $CODE_PORT_FORWARD_PID
wait $RAY_PORT_FORWARD_PID
wait $PROMETHEUS_PORT_FORWARD_PID
wait $PROMETHEUS_GRAFANA_PORT_FORWARD_PID

