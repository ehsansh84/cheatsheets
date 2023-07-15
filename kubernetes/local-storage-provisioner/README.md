To install a simple local storage provisioner for Kubernetes, you can follow these general steps:

1. Choose a local storage provisioner: There are several options available, such as `local-path-provisioner`, `hostpath`, or `rook`. You can select the provisioner that best suits your requirements. For this example, let's use `local-path-provisioner`.

2. Clone the provisioner repository: Use Git to clone the repository of the chosen local storage provisioner. In this case, you can clone the `local-path-provisioner` repository from GitHub:

   ```
   git clone https://github.com/rancher/local-path-provisioner.git
   ```

3. Create a namespace: Create a namespace where the provisioner will be installed. You can use the `kubectl` command-line tool to create the namespace:

   ```
   kubectl create namespace local-path-storage
   ```

4. Install the provisioner: Use `kubectl` to install the provisioner in the created namespace. Navigate to the cloned repository directory and apply the manifest files:

   ```
   cd local-path-provisioner
   kubectl apply -f deploy/local-path-storage.yaml
   ```

   This will deploy the provisioner as a set of Kubernetes resources.

5. Verify the installation: Wait for a few moments for the provisioner pods to be running. You can check the status of the pods using the following command:

   ```
   kubectl get pods -n local-path-storage
   ```

   Ensure that the provisioner pods are in the "Running" state.

6. Test the provisioner: Create a PersistentVolumeClaim (PVC) to test the provisioner. Here's an example PVC manifest:

   ```yaml
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: test-pvc
     namespace: default
   spec:
     accessModes:
       - ReadWriteOnce
     storageClassName: local-path
     resources:
       requests:
         storage: 1Gi
   ```

   Apply the PVC manifest using `kubectl`:

   ```
   kubectl apply -f pvc.yaml
   ```

   The provisioner should create a PersistentVolume (PV) dynamically, and the PVC should get bound to the created PV.

7. Verify the PVC and PV: Check the status of the PVC and PV using the following commands:

   ```
   kubectl get pvc
   kubectl get pv
   ```

   Ensure that the PVC is in the "Bound" state and the PV is created with the expected storage capacity.

That's it! You have successfully installed a simple local storage provisioner for Kubernetes and tested its functionality using a PersistentVolumeClaim. Remember to adjust the specific details, such as namespace, storage capacity, and storage class name, according to your requirements.