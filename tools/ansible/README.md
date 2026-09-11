# No Fuss Computing Ci Ansible Tools

This directory is for CI jobs using Ansible. It has been purposely setup to mimic an Ansible Collection. That is so that any kustomize manifests directory can contain only the relevant Ansible collection directories that will be linked to this directory when that manifests directory is being worked on.

If the kustomize manifests directory contains an ansible directory. Any sub directories found should be symlinked to this directory.


## No Fuss Computing - Ansible Role `app-versions`

This role updates the version details (`vars/versions.yaml`) for applications specified in `vars/applications.yaml`.

To update all applications, do the following:

``` shell

ansible-playbook tools/ansible/playbooks/application-update.yaml \
		-vvv;

```

To update a specific application, do the following:

``` shell

ansible-playbook tools/ansible/playbooks/application-update.yaml \
		--extra-vars "directory_application=<application name>" \
		-vvv;

```

To supply PR details (if not run from GH actions), do the following:

``` shell

GITHUB_REPOSITORY=<repo owner>/<repo name> \
GITHUB_REPOSITORY_OWNER=<repo owner> \
ansible-playbook tools/ansible/playbooks/application-update.yaml \
		--extra-vars "directory_application=<application name>" \
    --extra-vars "github_token=<your github token that can create PR>" \
		-vvv;

```


## No Fuss Computing - Ansible Role `git`

Contains git related tasks.


## No Fuss Computing - Ansible Role `gitbub`

Contains Github related tasks.


## No Fuss Computing - Ansible Role `kustomize-manifest-update`

This role serves the purpose of updating templates for a defined manifest directory.

To use this role, conduct the following:

``` shell

ansible-playbook tools/ansible/playbooks/kustomize-manifest-update.yaml \
		--extra-vars "directory_manifest=manifests" \
		-vvv;

```

To use against a specified repository
``` shell

GITHUB_REPOSITORY=<repo owner>/<repo name> \
GITHUB_REPOSITORY_OWNER=<repo owner> \
ansible-playbook tools/ansible/playbooks/kustomize-manifest-update.yaml \
		--extra-vars "directory_manifest=manifests" \
    --extra-vars "github_token=<your github token that can create PR>" \
		-vvv;

```

Run path is the same directory as where `manifests/` resides, this would normally be the repository root directory.
