import re
import requests

class Samopy(object):
    """ Documentation HERE
    
    """
    
    def __init__(self, server, user, password, port=8080):
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.uri = "http://" + self.server + ":" + str(port) + "/xmlapi/invoke"
    
    def get_network_interfaces(self):
        soap = """
<SOAP:Envelope xmlns:SOAP="http://schemas.xmlsoap.org/soap/envelope/">
 <SOAP:Header>
  <header xmlns="xmlapi_1.0">
   <security>
    <user>w45945</user>
    <password>password</password>
   </security>
   <requestID>client1:0</requestID>
  </header>  
 </SOAP:Header>
 <SOAP:Body>
  <find xmlns="xmlapi_1.0">
   <fullClassName>rtr.NetworkInterface</fullClassName>
   <resultFilter>
    <attribute>displayedName</attribute>
    <attribute>nodeName</attribute>
    <attribute>objectFullName</attribute>
    <attribute>olcState</attribute>
    <attribute>primaryIPv4Address</attribute>
    <attribute>primaryIPv4PrefixLength</attribute>
    <children/>
   </resultFilter>
  </find>
 </SOAP:Body>
</SOAP:Envelope>
        """
        try:
            r = requests.post(url=self.uri, data=soap)
            return r.text
        except ValueError:
            raise Exception(r)
        except Exception:
            raise
