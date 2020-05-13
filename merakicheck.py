from webexteamssdk import WebexTeamsAPI
import requests

meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
mynetwork = 'L_646829496481100388'
parentMessageId = 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYWJkYjcyNDAtOTE5ZC0xMWVhLWE3MzktN2Y2NGI0OTViZWM3'

msversion = '11-31'
mrversion = '26-6-1'
mxversion = '15-27'
mvversion = '4-0'

switch_identifier = 'MS'
AP_identifier = 'MR'
Security_appliance_identifier = 'MX'
camera_identifier = 'MV'

counts = {
    'Switch': 0,
    'AP': 0,
    'Security_appliance': 0,
    'Camera': 0,
    'Vulnerable': []
}

WebexRoomID = 'Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli'
myWebexToken = '' #you will need to put your personal token here
baseurl = 'https://dashboard.meraki.com/api/v0/networks/'

payload = {}
headers = {
            'X-Cisco-Meraki-API-Key': meraki_api_key,
            'Accept': 'application/json',
          } 

url = baseurl + f'{mynetwork}/devices'

response = requests.get(url, headers=headers, data=payload)
response.raise_for_status()

myresponse = response.json()

for device in myresponse:

    if (device['model'].startswith(switch_identifier)
            and device['firmware'].endswith(msversion)):

        counts['Switch'] += 1

    elif (device['model'].startswith(AP_identifier)
          and device['firmware'].endswith(mrversion)):

        counts['AP'] += 1

    elif (device['model'].startswith(Security_appliance_identifier)
          and device['firmware'].endswith(mxversion)):

        counts['Security_appliance'] += 1

    elif (device['model'].startswith(camera_identifier)
            and device['firmware'].endswith(mvversion)):

        counts['Camera'] += 1

    else:
        counts['Vulnerable'].append({device['serial']: device['model']})

print(f'Total switches that meet standard: {counts["Switch"]}')
print(f'Total APs that meet standard: {counts["AP"]}')
print(f'Total Security Aplliances that meet standard: {counts["Security_appliance"]}')
print(f'Total Cameras that meet standard: {counts["Camera"]}')
print('Devices that will need to be manually checked:')
for device in counts['Vulnerable']:
    for serial, model in device.items():
        print(f'Serial#: {serial}, Model#: {model}')

# api = WebexTeamsAPI(myWebexToken)
# api.messages.create(WebexRoomID, text='Report Completed')
