
class juniper_device:
    def __init__(self, model, hostname, ip, gateway, mgmt_junos, mac=None, software=None):
        self.model = model
        self.hostname = hostname
        self.ip = ip
        self.gateway = gateway
        self.mgmt_junos = mgmt_junos
        self.mac = mac
        self.software = software
    def load(data):
        with exce
        



sw1 = juniper_device('qfx', 'vir-cp00-csw000', '192.168.1.1/24', '192.168.1.254', True, 'aa:bb:cc:dd:ee', '19.1R4')


sw2 = juniper_device.load_devce_properties()

print(sw2)