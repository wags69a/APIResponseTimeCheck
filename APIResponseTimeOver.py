import requests
import time
import sys
from datetime import datetime
import subprocess

fd = open(r'C:\python\APITimes12.txt', 'w')
old_stdout = sys.stdout
sys.stdout = fd
print('This is the start of the response time testing')
print()
start_time = datetime.now()
print('The report started at: ' + (str(start_time)))
print()
print('This query will provide the time for each request using different employee IDs so no caching')
print()
print('=============================================================================================')
print()
howManyX = 0
howManyY = 0
myfile = open("API.txt", "r")
for line in myfile:
  url = "https://<BASEURL>?employeeNumber="+format(line).strip()

  payload={}
  headers = {
    'us-customer-api-key': '<APIKEY>',
    'Authorization': 'Basic <CUSTOMERTOKEN>'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  if len(response.text) == 2:
     print('No information is found for this Employee ID:  '+format(line).strip())
     print(response.status_code)
     print('We are looking at the time below, it will be flagged if over 5 seconds')
     print()
     print(response.elapsed.total_seconds())
     print()
     if (response.elapsed.total_seconds()) > 1:
         y = 'THIS IS NOT IN SPECS'
         print(y)
         print()
         howManyY =+ 1
     print('This API Ended at: ' + (str(datetime.now())))
     print()
     print()
  else:
    print(response.text[3:120])
    print(response.status_code)
    print('We are looking at the time below in seconds, it will be flagged if over 5 seconds')
    print(response.elapsed.total_seconds())
    print()
    if (response.elapsed.total_seconds()) > 1:
        x = 'THIS IS OUT OF SPECS'
        print(x)
        print()
        howManyX =+ 1
        print()
    print('This API Ended at: ' + (str(datetime.now())))
    time.sleep(3)
    print()
    print()

print()
print()
end_time = datetime.now()
print('==========================================')
print('This report ended at :' + (str(end_time)))
print()
print('There were this many failures with an ID:')
print(howManyX)
print()
print('There were this many failures with no ID:')
print(howManyY)
print()
total = howManyX + howManyY
print('We found this many issues:')
print(total)
print()
total_time = end_time - start_time
print('Total time to run this report was ' + (str(total_time)))
print()

fd.close()
subprocess.Popen(['C:\\Windows\\System32\\notepad.exe', 'C:\\python\\APITimes12.txt'])

