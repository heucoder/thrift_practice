# coding: utf-8
import sys
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

sys.path.append("../idl/gen-py")
from com.test import posResp
from com.test.ttypes import *

class posRespHandler:
    def get_length(self, pos):
        return (pos.x**2 + pos.y**2)**(0.5)

if __name__ == "__main__":


    handler = posRespHandler()
    processor = posResp.Processor(handler)
    transport = TSocket.TServerSocket("localhost", 9833)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print "Starting thrift server in python..."
    server.serve()
    print "done!"