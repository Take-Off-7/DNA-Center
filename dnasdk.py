from dnacentersdk import api
import json
import time
import calendar

#################### LOGIN ####################
dna = api.DNACenterAPI(base_url='https://sandboxdnac2.cisco.com', 
                       username='devnetuser', password='Cisco123!', verify=False)

#################### NETWORKS AND SITES ####################

# Print Site Topology
sites = dna.topology.get_site_topology()
for site in sites.response.sites:
    if site.parentId == '9e5f9fc2-032e-45e8-994c-4a00629648e8':
        print(site.name)
        for child_site in sites.response.sites:
            if child_site.parentId == site.id:
                print(f'  {child_site.name}')
                for more_children in sites.response.sites:
                    if more_children.parentId == child_site.id and child_site.parentId == site.id:
                        print(f'    {more_children.name}')
    print('')

# Print Vlans
vlans = dna.topology.get_vlan_details()
for vlan in vlans.response:
    print(vlan)

# Physical Topology Details
phys_top = dna.topology.get_physical_topology()
print(json.dumps(phys_top, indent=2, sort_keys=True))

#################### DEVICES ####################

# Print Device Details
devices = dna.devices.get_device_list()
for device in devices.response:
    print(device.type)
    print(device.hostname)
    print(device.managementIpAddress)
    print(device.id)
    print('')

# Get a specific device
device = dna.devices.get_device_by_id('e0ba1a00-b69b-45aa-8c13-4cdfb59afe65')
print(device)

#################### HEALTH CHECKS ####################
####################### CLIENTS #######################
# Get Client Health with Epoch Datetime
epoch_datetime = calendar.timegm(time.gmtime())

client_health = dna.clients.get_overall_client_health(timestamp=None)
print(json.dumps(client_health, indent=2, sort_keys=True))
print('')

# Get Network Health
net_health = dna.topology.get_overall_network_health(timestamp=None)
# print(net_health)
# print('')

# Get Site Health
site_health = dna.sites.get_site_health(timestamp=None)
# print(json.dumps(site_health, indent=2, sort_keys=True))
