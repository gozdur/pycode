from junos import Junos_Configuration
import jcs

def main():
    data = Junos_Configuration
    y = 0
    for elem in data.xpath(".//interface[name='ae0']//input/filter-name"):
        x = int(str(elem.text).split('g')[0])
        y += x
    
    if y == 15:
        jcs.syslog("172", "Works")

if __name__ == '__main__':
    main()
