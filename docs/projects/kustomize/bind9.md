---
title: Bind9
description: Documentation for No Fuss Computing's Bind9 Kubernetes Kustomize Manifests
date: 2026-01-06
template: project.html
about: https://github.com/nofusscomputing/kubernetes
---

This documentation page covers deploying our [bind9](../docker/bind/index.md) docker image to kubernetes. [Bind9](https://www.isc.org/bind/) is an open source DNS server Created by the [ISC](https://www.isc.org/).


## Components

### GIT OPS

There is a component called `git-ops`. This component caters for storing you DNS config within a git repository. For this component to function correctly you must include the following secret in the namespace you have deployed to.

``` yaml

---

apiVersion: v1
kind: Secret
metadata:
  labels:
    app.kubernetes.io/component: bind9
    app.kubernetes.io/name: dns
  name: bind-config
stringData:
  SSH_PRIVATE_KEY: |
    -----BEGIN OPENSSH PRIVATE KEY-----
    
    ... key contents

    -----END OPENSSH PRIVATE KEY-----
  SSH_REPOSITORY_HOST: -dns hostname of git provider-
  SSH_REPOSITORY_OWNER: -repository owner-
  SSH_REPOSITORY_NAME: -repository name-

```

### Overlays

The following overlay is provided as part of this kustomize package:

- `production`
