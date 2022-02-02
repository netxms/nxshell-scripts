#!/usr/bin/env nxshell

import threading
import org.netxms.client.TextOutputListener
from Queue import Queue
from threading import Thread

class ProgressCallback(org.netxms.client.TextOutputListener):
    def messageReceived(self, text):
        print(self.tag + ": " + text.strip())
        pass

    def onError(self):
        print(self.tag + ": onError")
        pass

    def setStreamId(self, streamId):
        pass

def worker():
    while True:
        print("###: qsize %s ###" % q.qsize());
        node = q.get()
        cb = ProgressCallback()
        cb.tag = node.objectName
        s.pollNode(node.objectId, NodePollType.CONFIGURATION_NORMAL, cb)
        #s.pollNode(node.objectId, NodePollType.CONFIGURATION_FULL, cb)
        q.task_done()

q = Queue()
for i in range(25):
    t = Thread(target=worker, name="Thread %d" % i)
    t.daemon = True
    t.start()

nodes = [o for o in s.allObjects if isinstance(o, objects.Node)]
for node in nodes:
    q.put(node)

q.join()

print("######## ALL DONE")
