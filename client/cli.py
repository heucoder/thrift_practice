# coding: utf-8
import sys
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


sys.path.append("../idl/gen-py")
from com.test import posResp
from com.test.ttypes import *

if __name__ == "__main__":
    try:
        transport = TSocket.TSocket('localhost', 9833)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = posResp.Client(protocol)
        transport.open()
        pos = pos(x=3,y=4)

        msg = client.get_length(pos)
        print "length" + str(msg)

        transport.close()

    except Thrift.TException, ex:
        print "%s" % (ex.message)