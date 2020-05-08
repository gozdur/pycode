import xlrd
import json


class NetworkDevice:

    def __init__(self, hostname, model, ip, mac, soft):
        self.hostname = hostname
        self.model = model
        self.ip = ip
        self.mac = mac
        self.soft = soft
        if self.model != None:
            if 'mx' in self.model:
                self.mgmt_junos = True
                self.mgmt_int = 'fxp0'
            elif 'ex' in self.model:
                self.mgmt_junos = False
                self.mgmt_int = 'me0'
            elif 'qfx' in self.model:
                self.mgmt_junos = True
                self.mgmt_int = 'em0'
            else:
                pass

    @classmethod
    def initialize_by_row(cls, file, row=1 ):
        wb = xlrd.open_workbook(file)
        sheet = wb.sheet_by_index(0)
        hostname = sheet.cell_value(row, 0)
        model = sheet.cell_value(row, 1)
        ip = sheet.cell_value(row, 3)
        mac = sheet.cell_value(row, 5)
        soft = sheet.cell_value(row, 6)
        return cls(hostname, model, ip, mac, soft)

    @staticmethod
    def get_device_list(file):
        wb = xlrd.open_workbook(file)
        sheet = wb.sheet_by_index(0)
        host_list = []
        for i in range(1, sheet.nrows):
            host_list.append(sheet.cell_value(i, 0))
        return host_list



def main():
    hosts = NetworkDevice.get_device_list('file.xlsx')
    object_list = []
    row = 0
    for device in range(0, len(hosts)):
        row += 1
        object_list.append(NetworkDevice.initialize_by_row('file.xlsx', row))
    for i in object_list:
        print(json.dumps((i.__dict__)))


if __name__ == "__main__":
    main()





