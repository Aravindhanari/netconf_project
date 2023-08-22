from ncclient import manager

router = {
    'host': 'sbx-iosxr-mgmt.cisco.com', # IP address of device
    'port': 830,  # Port to connect
    'username': 'admin',  # SSH Username
    'password': 'C1sco12345',  # SSH Password
    'hostkey_verify': False,  # Allow unknown hostkeys not in local store
    'device_params': {'name': 'iosxr'}  # Device connection parameters
}
m = manager.connect(**router, look_for_keys=False)

for capability in m.server_capabilities:
   print('*'* 50)
   print(capability)

 