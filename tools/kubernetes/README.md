## Tools - Kubernetes Cluster

This directory contains what is required for launching a K0s Kubernetes cluster. This cluster is for use with tests.

``` shell

docker exec -ti k0s-controller-1 k0s kubectl get po -A -o wide --watch

docker exec k0s-controller-1 k0s kubeconfig admin > ~/.kube/config

kubectl create ns openebs; \
kustomize build --enable-helm tools/kubernetes/storage | kubectl apply -f -

clear; \
kubectl create ns centurion; \
kustomize build manifests/centurion_erp/overlays/production | kubectl apply -f -

```