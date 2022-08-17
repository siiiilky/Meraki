import meraki
import config

dashboard = meraki.DashboardAPI(config.APIKEY)

my_orgs = dashboard.organizations.getOrganizations()
print(my_orgs)

#network_id = 'L_575897802350007824'

#response = dashboard.

#print(response)