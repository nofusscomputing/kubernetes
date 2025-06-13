---
title: Kustomize Manifests
description: Documentation home for No Fuss Computing's Kubernetes Kustomize Manifests
date: 2025-06-12
template: project.html
about: https://github.com/nofusscomputing/kubernetes
---

<span style="text-align: center;">

![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnofusscomputing%2Fkubernetes%2Frefs%2Fheads%2Fdevelopment%2F.meta%2Fproject_status.json)

----

![GitHub forks](https://img.shields.io/github/forks/NofussComputing/kubernetes?logo=github&style=plastic&color=000000&labell=Forks) ![GitHub stars](https://img.shields.io/github/stars/NofussComputing/kubernetes?color=000000&logo=github&style=plastic) ![Github Watchers](https://img.shields.io/github/watchers/NofussComputing/kubernetes?color=000000&label=Watchers&logo=github&style=plastic)

</span>

This project exists to provide a single location for all you Kubernetes deployment puposes. Contained within the [Kustomize repository](https://github.com/nofusscomputing/kubernetes) are Kubernetes Kustomize manifests ready for deployment. You are free to use them and that includes to collaborate in the addition and maintenance of the manifests.


## Problems to Solve

As the intent of this repository is for config management, although limited to the deployment configuration minus any secrets and customizations. As much as possible **There is a requirement for CI for Quality Control.** To aid in this tooling to assist in the process will need to be created. The following list includes and is not limited to, problems to solve:

- Deploying the manifests to test they work

- Identifying if a base / component has a dependency. _i.e. other apps that must be deployed first._

- Updating manifest repo locations.

  if a manifest that is fetched via git has had an update, then being able to update this when it occurs or close to.
