import requests
from jinja2 import Environment, FileSystemLoader
import os


class SAMOpy(object):
    """ Documentation HERE

    """

    def __init__(self, server, username, password, port=8080):
        """ Class initialization method

        """
        self.server = server
        self.port = port
        self.username = username
        self.password = password
        self.uri = "http://" + self.server + ":" + str(port) + "/xmlapi/invoke"
        self.management = dict(username=self.username, password=self.password)

    def _req(self, data):
        try:
            r = requests.post(url=self.uri, data=data)
            return r.text
        except ValueError:
            raise Exception(r)
        except Exception:
            raise

    def create(self):
        ENV = Environment(loader=FileSystemLoader(
                          os.path.join(os.path.dirname(__file__), "templates")))
        template = ENV.get_template("create.j2")
        data = template.render(management=self.management, config=var)
        return self._req(data)

    def read(self, var):
        ENV = Environment(loader=FileSystemLoader(
                          os.path.join(os.path.dirname(__file__), "templates")))
        template = ENV.get_template("read.j2")
        data = template.render(management=self.management, config=var)
        return self._req(data)

    def update(self):
        ENV = Environment(loader=FileSystemLoader(
                          os.path.join(os.path.dirname(__file__), "templates")))
        template = ENV.get_template("update.j2")
        data = template.render(management=self.management, config=var)
        return self._req(data)

    def delete(self):
        ENV = Environment(loader=FileSystemLoader(
                          os.path.join(os.path.dirname(__file__), "templates")))
        template = ENV.get_template("delete.j2")
        data = template.render(management=self.management, config=var)
        return self._req(data)

    def cli(self, ip_addr, command):
        ENV = Environment(loader=FileSystemLoader(
                          os.path.join(os.path.dirname(__file__), "templates")))
        template = ENV.get_template("cli.j2")
        data = template.render(ip_addr=ip_addr, command=command)
        return self._req(data)

    def filter(self, items):
        ENV = Environment(loader=FileSystemLoader(
                          os.path.join(os.path.dirname(__file__), "templates")))
        template = ENV.get_template("filter.j2")
        data = template.render(items)
        return data

    def result_filter(self, items):
        ENV = Environment(loader=FileSystemLoader(
                          os.path.join(os.path.dirname(__file__), "templates")))
        template = ENV.get_template("result_filter.j2")
        data = template.render(items)
        return data

    """
    Start of Fun
    """
    def get_network_interfaces(self, filter=False, result_filter=False):
        class_name = 'rtr.NetworkInterface'
        if filter:
            filter_xml = self.filter(filter)
        else:
            filter_xml = None

        if result_filter:
            result_attr = result_filter
        else:
            result_attr = {
                'result_attr': [
                    'displayedName',
                    'nodeName',
                    'objectFullName',
                    'olcState',
                    'primaryIPv4Address',
                    'primaryIPv4PrefixLength'
                ],
                'children': True
            }
        result_xml = self.result_filter(result_attr)

        var = {'class_name': class_name, 'result_filter': result_xml,
               'filter': filter_xml, 'children': True}
        return self.read(var)

    def cli_ping(self, src_addr, dst_addr):
        return cli(src_addr, "ping {}".format(dst_addr))
