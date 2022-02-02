#!/usr/bin/env nxshell

templates = [o for o in s.allObjects if isinstance(o, objects.Template)]
for t in templates:
    s.forcePolicyInstallation(t.objectId)
