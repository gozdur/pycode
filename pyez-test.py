from jnpr.junos import Device
from lxml import etree



with Device(host='192.168.1.108', user='root', passwd='Juniper') as dev:


    data = dev.rpc.get_config()

    allocated_bandwidth = 0

    for i in data.xpath(".//interface/unit[name='0']/description"):
        interco_bandiwdth = int(str(i.text).split('g')[0])

    for i in data.xpath(".//interface[name='ae0']//input/filter-name"):
        unit_bandwidth = int(str(i.text).split('g')[0])
        allocated_bandwidth += unit_bandwidth
    
    if interco_bandiwdth <= allocated_bandwidth*4.5:
        print("Pasmo sie skonczylo")
    else:
        print("Pasmo jeszcze jest")
    
    y = allocated_bandwidth*4.5
    print(y)