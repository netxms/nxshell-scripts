#!/usr/bin/env nxshell

#config = s.readAgentConfigurationFile(811) # read config from node 

# or hardcode it in the script

config = """LogFile = C:\\NetXMS\\log\\nxagentd.log
DebugLevel = 6

MasterServers = 172.26.18.66
ServerConnection = 172.26.18.66
"""

container = s.findObjectById(5204)
for c in container.childrenAsArray:
    print(c.objectName)
    try:
        currentConfig = s.readAgentConfigurationFile(c.objectId)
        if currentConfig != config:
            print("%s - config will be updated" % c.objectName)
            s.writeAgentConfigurationFile(c.objectId, config, True)
        else:
            print("%s skipped" % c.objectName)
    except:
        print("Error")
