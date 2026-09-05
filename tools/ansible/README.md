# No Fuss Computing Ci Ansible Tools

This directory is for CI jobs using Ansible. It has been purposely setup to mimic an Ansible Collection. That is so that any kustomize manifests directory can contain only the relevant Ansible collection directories that will be linked to this directory when that manifests directory is being worked on.

If the kustomize manifests directory contains an ansible directory. Any sub directories found should be symlinked to this directory.


## No Fuss Computing - Ansible Role `git`

Contains git related tasks.


## No Fuss Computing - Ansible Role `gitbub`

Contains Github related tasks.


## No Fuss Computing - Ansible Role `kustomize-manifest-update`

This role serves the purpose of updating templates for a defined manifest directory.

To use this role, conduct the following:

``` shell

ansible-playbook tools/ansible/playbooks/kustomize-manifest-update.yaml \
		--extra-vars "dir_manifest=manifests/<app name>" \
		-vvv;

```

To use against a specified repository
``` shell

GITHUB_REPOSITORY=<repo owner>/<repo name> \
GITHUB_REPOSITORY_OWNER=<repo owner> \
ansible-playbook tools/ansible/playbooks/kustomize-manifest-update.yaml \
		--extra-vars "dir_manifest=manifests/<app name>" \
    --extra-vars "github_token=<your github token that can create PR>" \
		-vvv;

```

Run path is the same directory as where `manifests/` resides, this would normally be the repository root directory.
