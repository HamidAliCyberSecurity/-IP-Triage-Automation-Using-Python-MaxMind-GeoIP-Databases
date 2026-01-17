# IP Triage Automation Using Python & MaxMind GeoIP Databases

## Project Overview
This project automates IP threat intelligence triage using Python and MaxMind GeoIP databases. It allows cybersecurity professionals and SOC analysts to quickly identify IP-related information, such as geolocation, ASN, and network ownership, to support threat detection and incident response activities.

## Features
- Reads IP addresses from CSV or TXT files.  
- Retrieves geolocation, ASN, and network information using MaxMind databases.  
- Generates structured output for analysis and reporting.  
- Streamlines IP triage for faster decision-making in cybersecurity operations.

## Technologies & Tools
- **Programming:** Python  
- **Databases:** MaxMind GeoLite2 ASN, City, and Country databases  
- **Skills Applied:** Network monitoring, IP analysis, threat intelligence, Python scripting, log analysis  

## Setup Instructions
1. Clone the repository:  
   ```bash
   https://github.com/HamidAliCyberSecurity/-IP-Triage-Automation-Using-Python-MaxMind-GeoIP-Databases.git
Install required Python packages:

bash
Copy code
pip install pandas geoip2
Download the MaxMind GeoLite2 databases (ASN, City, Country) and place them in the databases/ folder.

Place your IPs in ips.txt or ips.csv.

Run the script:

bash
Copy code
python ip_lookup.py
Usage
The script outputs geolocation, ASN, and country data for each IP in a structured format.

Use the generated data to prioritize threat investigations and build reports for SOC operations.

Skills Gained
Practical experience in Python scripting for cybersecurity automation.

Hands-on IP analysis and geolocation mapping using MaxMind databases.

Threat intelligence collection, network monitoring, and log analysis.

Structured reporting for SOC operations and incident response.
License

This project is licensed under the MIT License. See the LICENSE
 file for details.
