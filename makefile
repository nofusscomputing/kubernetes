.ONESHELL:

.SILENT:

START_PWD     := ${PWD}
MANIFEST      := ${MANIFEST}

.PHONY: update


update:
	ansible-playbook tools/ansible/playbooks/kustomize-manifest-update.yaml \
		--extra-vars "dir_manifest=${MANIFEST}" \
		-vvv;
