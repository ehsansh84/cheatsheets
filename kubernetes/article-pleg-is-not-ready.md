# PLEG is not ready

### The problem?
Some nodes were flipping between Ready/NoyReady status. After checking `sudo systemctl status kubelet` an error seen:
```
Aug 06 07:59:04 k8s-wa-2 kubelet[1498]: E0806 07:59:04.672201    1498 fsHandler.go:114] failed to collect filesystem stats - rootDiskErr: could not stat "/var/lib/docker/overlay2/7d3bddbf3988e8e8c8faa8e77ebbdc1f6a4d5b24058ec6e99eb598a3>
Aug 06 07:59:04 k8s-wa-2 kubelet[1498]: E0806 07:59:04.839883    1498 kubelet.go:1991] "Skipping pod synchronization" err="PLEG is not healthy: pleg was last seen active 6m57.173099499s ago; threshold is 3m0s"
Aug 06 07:59:04 k8s-wa-2 kubelet[1498]: E0806 07:59:04.858245    1498 fsHandler.go:114] failed to collect filesystem stats - rootDiskErr: could not stat "/var/lib/docker/overlay2/e20e8a97923a8148e5e077b5e2c7900d3900f6baa7c08d8702acbe60>
Aug 06 07:59:04 k8s-wa-2 kubelet[1498]: E0806 07:59:04.860787    1498 fsHandler.go:114] failed to collect filesystem stats - rootDiskErr: could not stat "/var/lib/docker/overlay2/ed0ab3a78bacc200ec7f756f844a258344425a6175d372a55be9597d>
Aug 06 07:59:04 k8s-wa-2 kubelet[1498]: E0806 07:59:04.912626    1498 fsHandler.go:114] failed to collect filesystem stats - rootDiskErr: could not stat "/var/lib/docker/overlay2/473e14b76b547a9e5b89afb0993da6dd2781ef3c3dcd48587f35977c>
Aug 06 07:59:06 k8s-wa-2 kubelet[1498]: E0806 07:59:06.700289    1498 fsHandler.go:114] failed to collect filesystem stats - rootDiskErr: could not stat "/var/lib/docker/overlay2/9a9866be20a4df0d3a80e38c8ef8c42526731e33361bb63ae199d813>
Aug 06 07:59:07 k8s-wa-2 kubelet[1498]: E0806 07:59:07.541252    1498 fsHandler.go:114] failed to collect filesystem stats - rootDiskErr: could not stat "/var/lib/docker/overlay2/dd8ce0738a97a019834bf1a1c00e5f320d24fe6c7f4f08cdaf23b94c>
Aug 06 07:59:07 k8s-wa-2 kubelet[1498]: E0806 07:59:07.634097    1498 fsHandler.go:114] failed to collect filesystem stats - rootDiskErr: could not stat "/var/lib/docker/overlay2/328df7e25698f996bf7f369588e93d7a708501b038d6e22db921b240>
Aug 06 07:59:08 k8s-wa-2 kubelet[1498]: E0806 07:59:08.134452    1498 fsHandler.go:114] failed to collect filesystem stats - rootDiskErr: could not stat "/var/lib/docker/overlay2/1aad94e06e185b871f439bd6a2975d84e67165fa2abc6484f96d906e>
Aug 06 07:59:09 k8s-wa-2 kubelet[1498]: E0806 07:59:09.840553    1498 kubelet.go:1991] "Skipping pod synchronization" err="PLEG is not healthy: pleg was last seen active 7m2.173749717s ago; threshold is 3m0s"
```
Checking `sudo systemctl status docker` seems like ok:
```
Aug 06 06:11:53 k8s-wa-2 dockerd[937]: time="2022-08-06T06:11:53.646068000Z" level=info msg="ignoring event" container=3ddc709df4318d44f193a5d23a2dcd1a5c3dbff7fea3ff4e999d9d153df59471 module=libcontainerd namespace=moby topic=/tasks/de>
Aug 06 06:23:55 k8s-wa-2 dockerd[937]: time="2022-08-06T06:23:55.065632140Z" level=info msg="ignoring event" container=bf144c2022f6e09ae0a63172e16198f8ff3c7ecd52de3dc62d490e37d23f738d module=libcontainerd namespace=moby topic=/tasks/de>
Aug 06 06:23:56 k8s-wa-2 dockerd[937]: time="2022-08-06T06:23:56.019466269Z" level=info msg="ignoring event" container=5afe8d9dfe3a27e0470cf1588dd0f886f50485d83a97960af4ff091e38c6c1f7 module=libcontainerd namespace=moby topic=/tasks/de>
Aug 06 06:23:56 k8s-wa-2 dockerd[937]: time="2022-08-06T06:23:56.406082789Z" level=info msg="ignoring event" container=a273b667baa09b0937d0da7ce4d0bc761a9ad427b8cacb54fd99af7f021eaad8 module=libcontainerd namespace=moby topic=/tasks/de>
Aug 06 06:31:56 k8s-wa-2 dockerd[937]: time="2022-08-06T06:31:56.219639833Z" level=info msg="ignoring event" container=b62c264501d21515cce03b266a61856d3024bcab195685af553fd0739178cbe9 module=libcontainerd namespace=moby topic=/tasks/de>
Aug 06 06:31:57 k8s-wa-2 dockerd[937]: time="2022-08-06T06:31:57.176957780Z" level=info msg="ignoring event" container=9028c44b1fcd8847f4dac63e9072c9349686bf771e750777bb92d35a561290e2 module=libcontainerd namespace=moby topic=/tasks/de>
Aug 06 06:31:57 k8s-wa-2 dockerd[937]: time="2022-08-06T06:31:57.512771961Z" level=info msg="ignoring event" container=fa37863f3c9937d9cfb47b788477117b5ab66f0131b3089dadb7d850ebb46045 module=libcontainerd namespace=moby topic=/tasks/de>
Aug 06 06:39:56 k8s-wa-2 dockerd[937]: time="2022-08-06T06:39:56.811765789Z" level=info msg="ignoring event" container=0c45a320f7de60f2f8d3c5e4ea9982e548462ec13669142408942956e8b55b7b module=libcontainerd namespace=moby topic=/tasks/de>
Aug 06 06:39:56 k8s-wa-2 dockerd[937]: time="2022-08-06T06:39:56.869892221Z" level=error msg="exit event" container=0c45a320f7de60f2f8d3c5e4ea9982e548462ec13669142408942956e8b55b7b error="no such container" module=libcontainerd namespa>
Aug 06 06:39:56 k8s-wa-2 dockerd[937]: time="2022-08-06T06:39:56.943591097Z" level=info msg="ignoring event" container=fe2559bf369d4ad37e0cc5d45b00ad6488ade9be8fbfaeee99931ae15d965fec module=libcontainerd namespace=moby topic=/tasks/de>
```

I've tried to `cordon` and `drain` all 4 nodes having this problem. After that `ssh` into nodes and execute these commands:
```commandline
sudo systemctl restart docker
sudo systemctl restart kubelet
```
After that the problem solved, and I'm waiting to see when I will return. 
References:
- [Pod Lifecycle Event Generator: Understanding the "PLEG is not healthy" issue in Kubernetes ](https://developers.redhat.com/blog/2019/11/13/pod-lifecycle-event-generator-understanding-the-pleg-is-not-healthy-issue-in-kubernetes#)
- [Node NotReady because of PLEG is not healthy #195](https://github.com/awslabs/amazon-eks-ami/issues/195)