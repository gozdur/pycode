from junos import Junos_Configuration
import jcs

def main():
    data = Junos_Configuration
    allocated_bandwidth = 0

    for i in data.xpath(".//interface/unit[name='0']/description"):
        interco_bandiwdth = int(str(i.text).split('g')[0])
    
    for i in data.xpath(".//interface[name='ae0']//input/filter-name"):
        unit_bandwidth = int(str(i.text).split('g')[0])
        allocated_bandwidth += unit_bandwidth
    remaining_capacity = (interco_bandiwdth*4.5)-allocated_bandwidth
    if allocated_bandwidth >= interco_bandiwdth*4.5:
        jcs.syslog("2", "CAPACITY CRITICAL: VLAN Attachment Bandwidth excedded the Interconnect capacity by 450% Contract violated")
    elif allocated_bandwidth >= interco_bandiwdth*2.25:
        jcs.syslog("2", "CAPACITY CRITICAL: VLAN Attachment Bandwidth reached 250% - Plan an upgrade!")
    else:
        jcs.syslog("6", "CAPACITY NOTICE: Contractual Interconnect capacity remaining " + str(remaining_capacity) + "gbps")

if __name__ == '__main__':
    main()
