# CloudnativePG Operator Kustomize


## Upgrading manifests

1. Fetch new release manifest

    - Navigate to repository https://github.com/cloudnative-pg/cloudnative-pg

    - Go To `releases` directory

    - Change the branch to the desired tag _Tag sgould match the desired release_

    - click on the file that matches the release version

    - copy the permalink raw URL

        Keep a copy of this url so it can be added to the commit message. Doing this will allow validity checking if required.

1. split the manifest

    From the apps dir `manifests/<app name>` run:

    ``` bash

    docker run -ti \
      -e "KUBECTL_SLICE_INPUT_FILE=<Raw URL of manifest>" \
      -e "KUBECTL_SLICE_OUTPUT_DIR=base/" \
      -v manifests/cloudnativepg-operator:/workdir \
      --rm \
      nofusscomputing/kubernetes-manifest-tools:latest

    ```

1. update the Base kustomization

    From the apps dir `manifests/<app name>` run:

    ``` bash

    ansible-playbook ../../../../other/kubernetes-manifest-tools/collection/playbooks/update-kustomize.yaml \
      --extra-vars "namespace=operators" \
      --extra-vars "manifest_dir=${PWD}/base"

    ```
