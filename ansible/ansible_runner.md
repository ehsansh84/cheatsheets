# Using ansible_runner in python

### Install ansible_runner
```commandline
pip install ansible_runner
```

### Run ansible:
```python
import ansible_runner
inventory = {"nodes": {"hosts": {
    "ubuntu@192.168.1.10": {},
    "ubuntu@192.168.1.20": {}
}}}
r = ansible_runner.run(playbook='sample.yaml', inventory=inventory)
print(r.status)
```

### References:
- []()