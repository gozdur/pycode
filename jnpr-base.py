import xlrd


class Juniper_device:
    def __init__(self, hostname, model, ip, gateway, mgmt_junos, mac=None, software=None):
        self.hostname = hostname
        self.model = model
        self.ip = ip
        self.gateway = gateway
        self.mgmt_junos = mgmt_junos
        self.mac = mac
        self.software = software



def host_list(file):
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    hostname = []
    for i in range(1, sheet.nrows):
        hostname.append(sheet.cell_value(i, 0))
    return hostname


dev = host_list('file.xlsx')

devices = {}

for item in dev:
    devices.update({item: {}})


print(devices)