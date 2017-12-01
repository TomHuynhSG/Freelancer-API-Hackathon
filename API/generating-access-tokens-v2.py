from flask import Flask, redirect, request
import os
import requests
import sys

# UPDATE these variables for each new client
#client_secret = '10717f462f4d7fa316b3f1a08788e8f3d832b4a5b6b79a292ad3edf140a885fd7144ad6556ec1728335ca12d35a4489e3f4d5b8ac85c90d4847504459fc8387d'
#client_id = '25504b28-6d2b-4b84-8ede-83bb286b19ad'
#REAL ONE
client_secret = sys.argv[1]
client_id = sys.argv[2]

#UPDATE url,redirect
#oauth_uri = 'https://accounts.freelancer-sandbox.com/oauth/authorise'
#REAL ONE
oauth_uri = 'https://accounts.freelancer.com/oauth/authorise'

#testing in Evelyn's laptop
#redirect_uri = 'http://127.0.0.1:9000/auth'
#REAL ONE
redirect_uri = sys.argv[3]

prompt = 'select_account consent'
advanced_scopes = '1%202%203%204%205%206' # %20 is used to represent space in HTML
accesstokenreal = None

app = Flask(__name__)

# Users who hit this endpoint will be redirected to the authorisation prompt
@app.route('/authorize')
def handle_authorize():
    return redirect(
        '{0}?response_type=code'
        '&client_id={1}&redirect_uri={2}'
        '&scope=basic&prompt={3}'
        '&advanced_scopes={4}'.format(
            oauth_uri, client_id, redirect_uri, prompt, advanced_scopes
        )
    )


# The endpoint waiting to receive the authorisation grant code
@app.route('/auth')
def handle_redirect():
    global accesstokenreal
    authorisation_code = request.args['code']

    payload = {
        'grant_type': 'authorization_code',
        'code': authorisation_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
    }

    #UPDATE the link
    response = requests.post('https://accounts.freelancer-sandbox.com/oauth/token', data=payload)
    result = response.json()
    accesstokenreal = result['access_token']
    
    
#if __name__ == '__main__':
#	app.secret_key = os.urandom(12)
#	app.run(debug=True, use_reloader=True, port=9000)
app.secret_key = os.urandom(12)
app.run(debug=True, use_reloader=True, port=9000)
