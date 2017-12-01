import requests
from LowBid import findwinner

projectid = input()
access = input()
#for test purposes only
#projectid = 15339034
#access = "6rpFBq8OYfmkd5s9siF8ZZExBnQgZe"
bidid = findwinner(projectid) #replace this with input or other thing 
action = 'award'
#UPDATE change the url
url ='https://www.freelancer-sandbox.com/api/projects/0.1/bids/' + str(bidid) + '/?action=' + str(action) 
#url ='https://www.freelancer-sandbox.com/api/projects/0.1/bids/4/?action=award' 
head = {"Freelancer-OAuth-V1": access, "Content-Type": "application/x-www-form-urlencoded"}
dat = '{"work_limit": 30, "billing_cycle": "30.5"}'
r = requests.put(url, headers = head, data = dat)
