import yaml
import ipaddress


def load_dc_data(dc_data):
    dc_data = yaml.load(open(dc_data))
    return dc_data


dc = load_dc_data('dc_data.yml')

