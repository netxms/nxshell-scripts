#!/usr/bin/env nxshell

CONTAINER_NAME = 'Imported Nodes'

NODES = [
        ['10.0.0.1', 'Node 1'],
        ['10.0.0.2', 'Node 2'],
        ['host.example.org', 'Node 3'],
        ['0.0.0.0', 'Node 4'], # node without IP address
        ['0.0.0.0', 'Node 5'], # node without IP address
]

container = s.findObjectByName(CONTAINER_NAME)
if container:
    containerId = container.objectId
else:
    parentId = objects.GenericObject.SERVICEROOT # Infrastructure Services root
    cd = NXCObjectCreationData(objects.GenericObject.OBJECT_CONTAINER, CONTAINER_NAME, parentId);
    containerId = session.createObject(cd)
    print '"%s" container created, id=%d' % (CONTAINER_NAME, containerId, )

flags = NXCObjectCreationData.CF_DISABLE_ICMP | \
        NXCObjectCreationData.CF_DISABLE_NXCP | \
        NXCObjectCreationData.CF_DISABLE_SNMP

for (ip, name) in NODES:
    cd = NXCObjectCreationData(objects.GenericObject.OBJECT_NODE, name, containerId);
    cd.setCreationFlags(flags);
    cd.setPrimaryName(ip) # Create node without IP address
    try:
        nodeId = session.createObject(cd)
        print '"%s" created, id=%d' % (name, nodeId)
    except NXCException:
        print 'Failed to create "%s" (%s)' % (name, ip)
