from kubernetes import client, config
import os
KUBE_CONFIG_PATH = "/home/ehsan/asiatech"
configuration = config.load_kube_config(config_file=os.environ.get("KUBECONFIG", KUBE_CONFIG_PATH))

v1 = client.CoreV1Api()

namespaces = [item.metadata.name for item in v1.list_namespace().items]
print(namespaces)

nodes = [item.metadata.name for item in v1.list_node().items]
print(nodes)
