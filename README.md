# APIResponseTimeCheck
Checks the response time of the API and flag it if over your limit then gives you a total number count.

#Installation
I used python on my PC which had access to the customer's environment. You will have to adjust to your customer.

#Usage
This code is meant to be used in a customer environment. It will change from each user. The URL should match what the customer gives you to test. All customer API keys and token were blanked out. The API that you check can be anything since you are checking for the response time. Using notepad, you can use a text file with multiple accounts to run the API more than once. I tested out 10, 100, 500 and 1000 account numbers in the test file and it worked. Adjust the time.sleeps to your environment.

#DevNet Sandbox
All sandboxes with APIs can use this script.

#Known issues
The tokens are all differnt, you must figure it out to use this script.
In the python script, lines 23(url), 27(API Key) and 28(Access Token) is supplied by the customer or the lab that you are using.

#Getting help
Contact the owner if he is not too busy.

#Credits and references
The Cisco requests library
The book, automate the boring stuff with python.
Stack Overflow gave me some of the ideas to try.

#Best Practice
Creat the .text file local to the python script.
Run the script on 1 API to verify all paths are correct.

#Step by Step
1) Download python script based on the operating system you use to run the script.
2) PIP install the requirements.
3) Edit the file with your URL, key and token.
4) Create a text file in the same directory as your python script.
5) Edit the script to open and then print out a text file with your findings.
6) Run the script.
7) The script will pop open a notepad text file when completed.

#Example Output
This API Ended at: 2021-08-30 09:37:47.548763


No information is found for this Employee ID:  XXXXX
200
We are looking at the time below, it will be flagged if over 5 seconds

7.354588

THIS IS NOT IN SPECS

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/wags69a/APIResponseTimeCheck)
