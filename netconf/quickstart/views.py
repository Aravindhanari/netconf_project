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
        post_data = dict(post_data)
        try:
            m = manager.connect(**router_config, look_for_keys=False)
            netconf_template = open('quickstart/templates/interface.xml').read()
            netconf_payload = netconf_template.format(description=post_data['description'])
            response = m.edit_config(netconf_payload, target="candidate").xml

            running_config_xml = xmltodict.parse(response)["rpc-reply"]

            if 'ok' in running_config_xml:
                data = {
                    'message': 'Config edit was successfull',
                    'data': response,
                    'status_code': 200
                }
                return Response(data)
            else:
                data = {
                    'error': 'Config edit was Failed',
                    'data': response,
                    'status_code': 201
                }
                return Response(data)
        except Exception as error:
            data = {
                'error': error,
                'message': 'Config edit was Failed',
                'data': response,
                'status_code': 500
            }
            return Response(data, 500)

class filterInterfaceView(APIView):

    def get(self, request):
        interface_name = request.query_params.get('interface_name')
        try:
            m = manager.connect(**router_config, look_for_keys=False)
            netconf_filter = """
            <filter>
                <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
                   <interface-configuration>
                          <interface-name>""" + interface_name + """
                          </interface-name>
                   </interface-configuration>
                </interface-configurations>
            </filter>
            """

            running_config = m.get_config("running", netconf_filter)
            running_config_xml = xmltodict.parse(running_config.xml)["rpc-reply"]["data"]


            data = {
                'message': 'Success',
                'data': running_config_xml['interface-configurations']["interface-configuration"],
                'status_code': 200
            }
            return Response(data)
        except Exception as error:
            data = {
                'error': error,
                'message': 'Config edit was Failed',
                # 'data': response,
                'status_code': 500
            }
            return Response(data, 500)



