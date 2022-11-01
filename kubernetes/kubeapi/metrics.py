from kubernetes import client, config
import os
KUBE_CONFIG_PATH = "/home/ehsan/asiatech"
config.load_kube_config(config_file=os.environ.get("KUBECONFIG", KUBE_CONFIG_PATH))

api = client.CustomObjectsApi()


def node_metrics():
    k8s_nodes = api.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "nodes")
    for stats in k8s_nodes['items']:
        print("Node Name: %s\tCPU: %s\tMemory: %s" % (stats['metadata']['name'], stats['usage']['cpu'], stats['usage']['memory']))
        print(stats)

