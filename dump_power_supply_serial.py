#!/usr/bin/env python
from argparse import ArgumentParser
from dnacentersdk import api
from dnacentersdk.exceptions import ApiError
import logging
import json
from  time import sleep, time, strftime, localtime
from dnac_config import DNAC, DNAC_USER, DNAC_PASSWORD
import sys
from time import sleep, time
logger = logging.getLogger(__name__)
timeout = 10

def get_device_power_supply_serial(dnac,deviceid ,deviceip,hostname):
    pslist = dnac.devices.get_the_details_of_physical_components_of_the_given_device(deviceid,type="PowerSupply")
    serials = [ ps.serialNumber for ps in pslist.response if ps.serialNumber != '']
    print(f'{deviceip},{hostname},{",".join(serials)}')


def main(dnac):
#    PAGE=3
    PAGE=500
    device_list = []
    # need to collect all of the switches
    for start in range (1,100+1,PAGE):
        response = dnac.devices.get_device_list(family='Switches and Hubs',offset=start, limit=PAGE)
        if len(response.response) == 0:
            break
    #    print(start)
        device_list.extend(response.response)
    total= len(device_list)
    device_attrs_list = [ (device.id,device.managementIpAddress,device.hostname) for device in device_list]
    # print the headers
    print('DeviceIP,Hostname,PS1,PS2')
    batchsize = 100 
#    batchsize = 3 
    for  index, device_attrs in enumerate(device_attrs_list,1):
        get_device_power_supply_serial(dnac,*device_attrs)
        if index % batchsize == 0:
            print(f'Sleeping 5 seconds processed:{index}/{total}', file=sys.stderr) 
            sleep(5)

    #get_device_ports(dnac,*device_device_attrs[1])
    #print (device_attrs_list)
    
if __name__ == "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('-v', action='store_true',
                        help="verbose")
    parser.add_argument('--password',  type=str, required=False,
                        help='new passowrd')
    parser.add_argument('--dnac',  type=str,default=DNAC,
                        help='dnac IP')
    args = parser.parse_args()

    if args.v:
        root_logger=logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        root_logger.addHandler(ch)
        logger.debug("logging enabled")

    #logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    DNAC = args.dnac
    dnac = api.DNACenterAPI(base_url='https://{}:443'.format(DNAC),
                                #username=DNAC_USER,password=DNAC_PASSWORD,verify=False,debug=True)
                                username=DNAC_USER,password=DNAC_PASSWORD,verify=False)
    main(dnac)
