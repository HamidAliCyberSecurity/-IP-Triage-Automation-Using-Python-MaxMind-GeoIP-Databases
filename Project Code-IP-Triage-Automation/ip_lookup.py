import os
import geoip2.database
import pandas as pd
from geoip2.errors import AddressNotFoundError

# ASN Database
asndb = geoip2.database.Reader('databases/GeoLite2-ASN.mmdb')

# City Database
citydb = geoip2.database.Reader('databases/GeoLite2-City.mmdb')

# Country Database
countrydb = geoip2.database.Reader('databases/GeoLite2-Country.mmdb')

# Read IPs from file
ips = []
with open('ips.txt', 'r') as f:
    ips = [line.strip() for line in f]

# New lists to store IPs found and missing
found_ips = []
missing_ips = []

for ip in ips:
    try:
        # Try all three lookups
        asn_response = asndb.asn(ip)
        city_response = citydb.city(ip)
        country_response = countrydb.country(ip)

        found_ips.append(ip)

    except AddressNotFoundError as e:
        print(f"\n❌ {ip} NOT FOUND in one or more databases → {e}")
        missing_ips.append(ip)

# Create master list for found IPs
masterList = []
for ip in found_ips:
    # Search MMDB for IP
    asn_response = asndb.asn(ip)
    city_resp = citydb.city(ip)

    # Assign the Items
    temp_asn = asn_response.autonomous_system_organization
    temp_network = asn_response.network
    temp_asnum = asn_response.autonomous_system_number
    temp_city = city_resp.city.name
    temp_country = city_resp.country.name
    temp_zip = city_resp.postal.code
    temp_location = f"{city_resp.location.latitude}, {city_resp.location.longitude}"

    # Make a List and append it to the master list
    tempList = [ip, temp_asnum, temp_asn, temp_network, temp_city, temp_country, temp_zip, temp_location]
    masterList.append(tempList)

# Add missing IPs with NULL values for other fields
for ip in missing_ips:
    tempList = [ip, "None", "None", "None", "None", "None", "None", "None"]
    masterList.append(tempList)

# Create the dataframe and set up the column names
df = pd.DataFrame(masterList, columns=["IP Address", "ASN", "Organization", "Network", "City", "Country", "Postal Code", "Location"])

# Save the dataframe to CSV
df.to_csv('ips.csv', index=False)

print("\n📁 CSV file 'ips.csv' created successfully.")