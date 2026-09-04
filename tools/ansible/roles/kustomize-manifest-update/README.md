# No Fuss Computing - Ansible Role `kustomize-manifest-update`

This role serves the purpose of updating templates for a defined manifest directory.

To use this role, conduct the following:

``` shell

ansible-playbook tools/ansible/playbooks/kustomize-manifest-update.yaml \
		--extra-vars "dir_manifest=manifests/<app name>" \
		-vvv;

```

Run path is the same directory as where `manifests/` resides.
