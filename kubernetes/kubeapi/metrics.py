from kubernetes import client, config
import os
KUBE_CONFIG_PATH = "/home/ehsan/asiatech"
config.load_kube_config(config_file=os.environ.get("KUBECONFIG", KUBE_CONFIG_PATH))

api = client.CustomObjectsApi()


def node_metrics():
    k8s_nodes = api.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "nodes")
    total_cpu = 0
    workers_count = 0
    for stats in k8s_nodes['items']:
        if 'node-role.kubernetes.io/master' not in stats['metadata']['labels']:
            workers_count += 1
            memory = round(int(stats['usage']['memory'][:-2])/1024/1024, 2)
            cpu = round(int(stats['usage']['cpu'][:-1])/1000000000, 2)
            total_cpu += cpu
            print(f"Node Name: {stats['metadata']['name']}\tCPU: {cpu}\tMemory: {memory}GB")
            print(stats)
    average_cpu = total_cpu / workers_count
    print(f'Workers count: {workers_count}, Total CPU: {total_cpu} Average CPU: {average_cpu}')
    if average_cpu > 3:
        print('Going to scale cluster UP')


from time import sleep
while True:
    node_metrics()
    sleep(1)
