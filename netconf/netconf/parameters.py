router_config = {
    # 'host': 'sandbox-iosxr-1.cisco.com',  # IP address of device
    'host': 'sbx-iosxr-mgmt.cisco.com',
    'port': 830,  # Port to connect to
    'username': 'admin',  # SSH Username
    'password': 'C1sco12345',  # SSH Password
    'hostkey_verify': False,  # Allow unknown hostkeys not in local store
    'device_params': {'name': 'iosxr'}  # Device connection parameters
}