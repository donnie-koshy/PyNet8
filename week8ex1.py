from jnpr.junos import Device
from pprint import pprint
from getpass import getpass

#Create Device object
router=Device(host="srx2.lasthop.io",user="pyclass",password=getpass())
#Open NETCONF session
router.open()
details=router.facts
pprint(details)

print("\n Host name is "+details['hostname'])
