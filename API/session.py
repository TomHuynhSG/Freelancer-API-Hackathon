from freelancersdk.session import Session
id = 304
token = 'FLN5PJTKB6A3DFYL9COGRHH3FESSJ6R6'

class FreelancerAPISession:
	def __init__(self, id, token):
		self.id = id
		self.token = token
		self.session = Session(id=id, token=token)

#api_session= FreelancerAPISession(id,token)
#print (api_session.session)