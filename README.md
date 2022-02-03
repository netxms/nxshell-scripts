# Collection of scripts for nxshell

NXShell is jython-based integration tool for [NetXMS](https://netxms.org/)

Most of these scripts will require small changes to make them work in your environment (changing container IDs, etc.).

Usage:

```
$ nxshell -H 127.0.0.1 -u admin script_name.py
```

Check `nxshell -h` for detailed usage instructions.

Please note that jython supports only python 2.7, so no f-format and stuff.

## bulk_import.py

Create nodes in bulk.

## force_policy_installation.py

Iterate over all templates and force deployment of configuration policies.

## list_tunnels.py

Save list of all tunnels (both connected and unbound) to csv file.

## poll_all_nodes.py

Run configuration poll on all nodes in the system.

## poll_nodes_in_container.py

Run configuration poll for nodes in the container (can be template, cluster, etc.).

## update_agent_config.py

Remotely update and apply agent config on all nodes in the container.
