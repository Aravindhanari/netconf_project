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

class NetconfView(APIView):

    def get(self, request):

        linkedin = 'https://www.linkedin.com/in/priyank-desai-2b89a41a3/'
        github = 'https://github.com/Priyank010'
        my_website = 'https://priyank010.github.io/#home'
        medium = 'https://priyankdesai515.medium.com/'

        m = manager.connect(**router_config, look_for_keys=False)
        print('m check ')
        print(m)
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
        print('running config')
        # print(running_config)
        o = xmltodict.parse(running_config)
        data = json.loads(o, indent = 3)  # '{"e": {"a": ["text", "text"]}}'
        # print(data)


        # import pprint
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(data)


        # tree = E.parse(running_config)
        # root = tree.getroot()
        # d = {}
        # for child in root:
        #     if child.tag not in d:
        #         d[child.tag] = []
        #     dic = {}
        #     for child2 in child:
        #         if child2.tag not in dic:
        #             dic[child2.tag] = child2.text
        #     d[child.tag].append(dic)
        # print(d)
        # from pkgutil import simplegeneric
        #
        # @simplegeneric
        # def get_items(obj):
        #     while False:  # no items, a scalar object
        #         yield None
        #
        # @get_items.register(dict)
        # def _(obj):
        #     return obj.items()  # json object. Edit: iteritems() was removed in Python 3
        #
        # @get_items.register(list)
        # def _(obj):
        #     return enumerate(obj)  # json array
        #
        # def strip_whitespace(json_data):
        #     for key, value in get_items(json_data):
        #         if hasattr(value, 'strip'):  # json string
        #             json_data[key] = value.strip()
        #         else:
        #             strip_whitespace(value)  # recursive call
        #
        # strip_whitespace(data)
        # allMovieData = json.stringify(data)
        # allMovieData = allMovieData.replace( /\\n / g, '')

        print(data)


        # with open(running_config) as xml_file:
        #     data_dict = xmltodict.parse(xml_file.read())
        # print('data dict')
        # print(data_dict)
        # data = xml.dom.minidom.parseString(running_config).toprettyxml()
        # print('data from running config')
        # data_obj = GetNetconfig(data)
        data_obj = data.replace("\\n", "")
        serializer_class = getNetconfSerializer(data_obj)

        return Response(serializer_class.data)