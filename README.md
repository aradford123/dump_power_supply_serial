# dump_power_supply_serial
This script dumps the serial numbers of all the powersupplies on switches.

## Getting stated
First (optional) step, create a vitualenv. This makes it less likely to clash with other python libraries in future.
Once the virtualenv is created, need to activate it.
```buildoutcfg
python3 -m venv env3
source env3/bin/activate
```

Next clone the code.

```buildoutcfg
git clone https://github.com/aradford123/mapsiteSSID.git
```

Then install the  requirements (after upgrading pip). 
Older versions of pip may not install the requirements correctly.
```buildoutcfg
pip install -U pip
pip install -r requirements.txt
```

Edit the dnac_vars file to add your DNAC and credential.  You can also use environment variables.

## Credentials

You can either add environment variables, or edit the  dnac_config.py file
```
import os
DNAC= os.getenv("DNAC") or "sandboxdnac.cisco.com"
DNAC_USER= os.getenv("DNAC_USER") or "devnetuser"
DNAC_PORT=os.getenv("DNAC_PORT") or 8080
DNAC_PASSWORD= os.getenv("DNAC_PASSWORD") or "Cisco123!"
```

## dump_power_supply_serial
This script will trigger a pre-check on a given device.

### Example
```
$ ./dump_power_supply_serial.py 
DeviceIP,Hostname,PS1,PS2
192.168.14.16,2960x-auckland,DCB1935607B
10.10.3.122,9k-l3,DCA2221G76U
192.168.200.232,encs-9k,ART2202F2NU,ART2202F8XJ
10.10.100.120,perth-9k,LIT22112YS7
10.10.9.4,perth-9k-edge,LIT220696DM
```
