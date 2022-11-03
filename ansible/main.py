import ansible_runner
inventory = {"nodes": {"hosts": {
    "ubuntu@85.208.253.141": {},
    "ubuntu@85.208.253.223": {},
    "ubuntu@123.208.253.222": {}
}}}
import os

print(os.getcwd())
r = ansible_runner.run(private_data_dir=os.getcwd(), playbook='sample.yaml', inventory=inventory)
# print(r.stats['failures'])
# print(r.status)


message = {}
for host in r.stats['failures']:
    for e in r.host_events(host):
        try:
            if "fail" in e["event"]:
                message[str(host)] = e['event_data']['res']['stderr']
        except Exception as s :
            pass
# data['tags'] = tmp
print('======================')
print(r.status)
print(message)
print(r.stats)
print(r.stats['changed'])

