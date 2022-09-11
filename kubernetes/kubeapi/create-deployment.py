from kubernetes import client, config
import os

KUBE_CONFIG_PATH = "/home/ehsan/Documents/k8s_configs/afranet.yaml"
configuration = config.load_kube_config(config_file=os.environ.get("KUBECONFIG", KUBE_CONFIG_PATH))

doc = {
  "apiVersion": "apps/v1",
  "kind": "Deployment",
  "metadata": {
    "name": "nginx-deployment"
  },
  "spec": {
    "selector": {
      "matchLabels": {
        "app": "nginx"
      }
    },
    "replicas": 3,
    "template": {
      "metadata": {
        "labels": {
          "app": "nginx"
        }
      },
      "spec": {
        "containers": [
          {
            "name": "nginx",
            "image": "nginx:1.14.2",
            "ports": [
              {
                "containerPort": 80
              }
            ]
          }
        ]
      }
    }
  }
}

from kubernetes.client.rest import ApiException
import time

api_client = client.ApiClient(configuration)
v1 = client.AppsV1Api(api_client)

while True:
    try:
        response = v1.read_namespaced_deployment_status(name='nginx-deployment', namespace="default")
        if response.status.available_replicas != 3:
            print("Waiting for Deployment to become ready...")
            time.sleep(5)
        else:
            break
    except ApiException as e:
        print(f"Exception when calling AppsV1Api -> read_namespaced_deployment_status: {e}\n")
