from kubernetes import client, config
import os
KUBE_CONFIG_PATH = "/home/ehsan/asiatech"
configuration = config.load_kube_config(config_file=os.environ.get("KUBECONFIG", KUBE_CONFIG_PATH))

v1 = client.CoreV1Api()


def list_namespaces():
    namespaces = [item.metadata.name for item in v1.list_namespace().items]
    print(namespaces)


def list_nodes():
    nodes = [item.metadata.name for item in v1.list_node().items]
    print(nodes)


def list_pods():
    pods = [item.metadata.name for item in v1.list_pod_for_all_namespaces().items]
    print(pods)


list_pods()
