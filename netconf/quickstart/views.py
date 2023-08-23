from .serializers import *
from rest_framework.views import APIView
from .tests import *
from rest_framework.response import Response
from netconf.parameters import router_config
from ncclient import manager
import xml.dom.minidom
import json
import xmltodict
import xml.etree.ElementTree as E
from django.template.loader import render_to_string, get_template

class NetconfView(APIView):

    def get(self, request):
        m = manager.connect(**router_config, look_for_keys=False)
        print('manager connection status ')
        print(m.connected)
        capab = []
        for capability in m.server_capabilities:
            print('*' * 50)
            capab.append(capability)
        data_obj = myNetconf(capab)
        serializer_class = myNetconfSerializer(data_obj)
        return Response(serializer_class.data)

class GetconfigView(APIView):

    def get(self, request):
        m = manager.connect(**router_config, look_for_keys=False)
        running_config = m.get_config('running').xml
        data_obj = xmltodict.parse(running_config)
        return Response(data_obj)

class editNetconfView(APIView):

    def post(self, request):
        post_data = request.data
        print('dataaaa got from the api')
        post_data = json.dumps(post_data)
        m = manager.connect(**router_config, look_for_keys=False)
        print('m check ')
        print(m)
        netconf_template = open('quickstart/templates/interface.xml').read()

        # netconf_payload = netconf_template.format(description=post_data['description'], name=post_data['name'], ip=post_data['ip'],netmask=post_data['netmask'])

        netconf_payload = netconf_template.format(post_data)
        response = m.edit_config(netconf_payload, target="candidate").xml
        print('response from edit config')
        print(response)
        running_config_xml = xmltodict.parse(response)["rpc-reply"]
        print(running_config_xml)
        if 'ok' in running_config_xml:
            return Response(True, 200)
        else:
            return Response(False, 201)

        # return running_config_xml
        # data_obj = myNetconf(capab)
        # serializer_class = myNetconfSerializer(data_obj)
        # return Response(running_config_xml.data)



