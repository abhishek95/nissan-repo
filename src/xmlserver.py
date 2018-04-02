# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 16:26:46 2018

@author: abhis
"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


def update_loc(x,y):
    print ('request recieved',x,y)
    return x+y

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),requestHandler=RequestHandler)
print (server)
server.register_function(update_loc,'update_loc')
server.register_multicall_functions()
server.serve_forever()