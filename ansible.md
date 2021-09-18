# Ansible Hello world by Ehsan Shirzadi

### Step1: Installation on Ubuntu:
This code works for me on Ubuntu 20.04
```
sudo apt-get install ansible
```
in case of any errors try this:
```
sudo apt-get update
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```

More information for other linux distros can be found here:
https://docs.ansible.com/ansible/2.4/intro_installation.html


### Step2: Add your host to Ansible hosts:
```
vim /etc/ansible/hosts
```
Add this to the file (I assume your client's IP is:192.168.10.20)
```
[test]
192.168.10.20
```

### Step3: Copy your server public key on your clients (I assume your client's user is ubuntu)

If you didn't generate an ssh-key before try to run this command:
```
ssh-keygen
```
and hit enter for all questions.
Then run this command to copy your public key to client:
```
ssh-copy-id ubuntu@192.168.10.20
```

### Step4: Create a playbook
```
mkdir playbooks
cd playbooks
vim hello.yml
```
Put this code into the file:
```
---
- name: This is a hello-world example
  hosts: test
  tasks:
    - name: Create a file called '/tmp/hello.txt' with the content 'hello world'.
      copy:
        content: hello world
        dest: /tmp/hello.txt
```

### Step5: Run
```
ansible-playbook hello.yml
```

### Uncomment this line in `/etc/ansible/ansible.cfg` to disable ssh host key checking
```
host_key_checking = False
```
### To use docker:
```
pip install docker-py`
```
That's it! you can now check your client for /tmp/hello.text


Web: www.ehsanshirzadi.com
