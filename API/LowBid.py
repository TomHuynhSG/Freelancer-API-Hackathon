import requests
import json

def findwinner(projectid, access):
	
	url = 'https://www.freelancer-sandbox.com/api/projects/0.1/projects/'+ str(projectid) +'/bids/' #+ intl

	head = {"Freelancer-OAuth-V1": "6rpFBq8OYfmkd5s9siF8ZZExBnQgZe", "Content-Type": "application/json"} #change the freelancer aouth with access
	r = requests.get(url, headers = head)
	#print(r.content)
	listbids = json.loads(r.content)
	bids = listbids['result']['bids']

	#getting the lowest amount
	lowest = None
	for i in bids:
		current = i['amount']
		if lowest != None:
			if lowest > current:
				lowest = current
		else:
			lowest = current

	#finding the bids id of the lowest bidder
	bidderid = []
	for i in bids:
		if i['amount'] == lowest:
			bidderid.append(i['id'])

	#the first bidderid win
	return bidderid[0]
