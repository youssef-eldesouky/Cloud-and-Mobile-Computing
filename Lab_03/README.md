# Lab 3 - Containerization and Cluster Orchestration

### Overview
This lab covers Docker containers, Docker image layering, Kubernetes orchestration with kind, scheduling with node labels and node selectors, and self-healing with health probes.

The lab is organized into separate parts so that each section has its own files, screenshots, and outputs.


## Folder Structure

### Lab 03
- `README.md` → main overview for the lab
- `Reflection on Lab_03.md` → answers to the reflection questions

### Part A - Containers, Namespaces, and Cgroups
This part contains the container observation screenshots from running an interactive Ubuntu container, comparing host and container process views, and testing resource limits with cgroups.

Files and evidence in this folder:
- `A1-start-container.png`
- `A1-container-observation-1.png`
- `A1-container-observation-2.png`
- `A1-container-observation-3.png`
- `A1-container-observation-4.png`
- `A1-container-observation-5.png`
- `A2-host-vs-container-pid.png`
- `A3-start-memory-limited-container.png`
- `A3-install-stress.png`
- `A3-generate-load.png`
- `A3-cgroups-stress-stats.png`

### Part B - Docker Image Layering
This part contains the Flask application files, Dockerfiles, and screenshots showing the build history of the basic image and the multi-stage image.

Files in this folder:
- `app.py`
- `requirements.txt`
- `Dockerfile.basic`
- `Dockerfile.multistage`

Screenshots in the `Screenshots` folder:
- `B1-basic-image-build-history-1.png`
- `B1-basic-image-build-history-2.png`
- `B1-basic-image-build-history-3.png`
- `B2-multistage-image-build-history-1.png`
- `B2-multistage-image-build-history-2.png`
- `B2-multistage-image-build-history-3.png`

### Part C - Kubernetes Orchestration with kind
This part contains the Kubernetes deployment and service manifests, plus screenshots showing the kind cluster, loaded images, deployed pods, and service access.

Files in this folder:
- `deployment.yaml`
- `service.yaml`

Screenshots in the `Screenshots` folder:
- `C1-kind-cluster-nodes.png`
- `C2-load-images-into-kind.png`
- `C3-deployment-service-pods.png`
- `C4-service-access.png`

### Part D - Scheduling and Placement
This part contains the deployment file updated with a node selector, along with screenshots showing node labels and pod placement.

Files in this folder:
- `deployment.yaml`

Screenshots in the `Screenshots` folder:
- `D1-node-labels.png`
- `D2-placement-with-nodeSelector.png`

### Part E - Self-Healing and Health Probes
This part contains the probe-based deployment file and screenshots showing pod deletion, automatic recovery, and probe behavior.

Files in this folder:
- `probe-deployment.yaml`

Screenshots in the `Screenshots` folder:
- `E1-pod-self-healing-1.png`
- `E1-pod-self-healing-2.png`
- `E2-probes-describe-1.png`
- `E2-probes-describe-2.png`
- `E3-kill-container-recovery-1.png`
- `E3-kill-container-recovery-2.png`
- `e3-after-kill-watch.png`


## What was implemented

### Part A
- Started an interactive Ubuntu container
- Observed hostname, process tree, network interface, mounts, and cgroup information
- Compared host PID and container PID views
- Applied CPU and memory limits
- Used `stress` to generate load and observed resource ceilings with `docker stats`

### Part B
- Built a basic Docker image for the Flask application
- Built a multi-stage Docker image
- Compared image history and layering behavior
- Observed how layer ordering affects caching and rebuild speed

### Part C
- Created a local Kubernetes cluster using kind
- Loaded Docker images into kind
- Deployed a replicated application using a Deployment
- Exposed the application using a Service
- Accessed the service using port-forward and curl

### Part D
- Added a label to the node
- Used a node selector to influence pod placement
- Verified placement using `kubectl get pods -o wide`

### Part E
- Deleted a pod and observed automatic recovery
- Added readiness and liveness probes
- Inspected probe configuration with `kubectl describe pod`
- Killed the container process and observed Kubernetes recovery behavior


## Outputs and Evidence
Each part contains its own screenshots inside the `Screenshots` folder.

If text outputs were required, they should be saved alongside the part files in the same folder structure used for that part.


## Reflection
The answers to the reflection questions are available in:
- `Reflection on Lab_03.md`


## Conclusion
This lab demonstrated the relationship between containers, Docker image design, Kubernetes orchestration, scheduling control, and self-healing behavior. It also showed how declarative infrastructure helps manage applications consistently and reliably.