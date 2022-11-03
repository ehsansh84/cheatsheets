from kubernetes import client, config
import os
KUBE_CONFIG_PATH = "/home/ehsan/asiatech"
configuration = config.load_kube_config(config_file=os.environ.get("KUBECONFIG", KUBE_CONFIG_PATH))

v1 = client.CoreV1Api()

nodes = [item.metadata.name for item in v1.list_node().items]
# print(nodes)

# print(v1.list_node())

# print(len(v1.list_node().items))
# print(v1.list_node().items[2])
# print(type(v1.list_node().items[2]))

for node in v1.list_node().items:
    print(node)
    print(type(node))

