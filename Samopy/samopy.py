import requests
from jinja2 import Environment, FileSystemLoader
import os

class SAMOpy(object):
    """ Documentation HERE
    
    """
    
    def __init__(self, server, user, password, port=8080):
        """ Class initialization method
        
        """
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.uri = "http://" + self.server + ":" + str(port) + "/xmlapi/invoke"
    
    def _req(self, data):
        try:
            r = requests.post(url=self.uri, data=data)
            return r.text
        except ValueError:
            raise Exception(r)
        except Exception:
            raise

    def _get(self, class_name, result_attributes, filter, children=False):
        ENV = Environment(loader=FileSystemLoader(
              os.path.join(os.path.dirname(__file__), "templates")))
        template = ENV.get_template("find.j2")
        var = dict(username=self.user, password=self.password, class_name=class_name, 
              result_attributes=result_attributes, filter=filter, children=children)
        data = template.render(config=var)
        return self._req(data)

    def get_network_interfaces(self, filter=False):
        class_name = "rtr.NetworkInterface"
        result_attributes = ["displayedName", "nodeName", "objectFullName", "olcState", "primaryIPv4Address", "primaryIPv4PrefixLength"]
        return self._get(class_name, result_attributes, filter, children=True)
