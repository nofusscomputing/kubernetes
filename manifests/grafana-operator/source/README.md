# Grafana Operator


## Updating Manifests

1. download new `cluster scoped` manifest https://github.com/grafana/grafana-operator/releases

1. remove **ALL** namespaces from manifests

    !!! tip
        VSCode:
            1. `ctrl-h` to bring up search
            1. use search string `\n\s\snamespace:.+` and set to regex search (click on `.*` button)
            1. leave the replace field empty
            1. click on replace all

1. Delete any manifest that is of kind `namespace`

1. Copy each manifest into their own file at path `base/`

    !!! tip
        If there are `ClusterRoleBinding` manifests, ensure that `kustomization.yaml` has its replacements section updated to update the service accounts namespace.

