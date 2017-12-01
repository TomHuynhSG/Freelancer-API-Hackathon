import requests

"""
data = '{"title": "Build my Supe", "description": "I need this website to make visual basic GUIs","budget": {"minimum": 1000},"jobs": [{"id": 3}]}'

access_token = 'ysTDu4SqrMT3sYBMd4zNqDvxn0CMsV'
head = {"Freelancer-OAuth-V1": access_token, "Content-Type": "application/json"}

response = requests.post("https://www.freelancer-sandbox.com/api/projects/0.1/projects/", headers = head, data=data)
print(response)
"""

# 3D printing, manufacturing
def post_project(sketch_link, image_link, access_token, min_budget, max_budget, project_name = None):
    title = 'Make my Handbag come True!'
    description = "Hey, I need someone to make this handbag for me, this is the sketch and the picture of the handbag that I want. The sketch:" \
    + sketch_link + "\n The handbag image: " + image_link
    head = {"Freelancer-OAuth-V1": access_token, "Content-Type": "application/json"}
    # javascript 9, python 13, website design 17, AI 913
    data = '{"title": "%s", "description": "%s", "budget": {"currency_id": 3, "minimum": %d, "maximum": %d},\
    "jobs": [{"id": 630}, {"id": 83}]}' % (title, description, min_budget, max_budget)
    #print(data)
    response = requests.post("https://www.freelancer-sandbox.com/api/projects/0.1/projects/", headers = head, data=data)
    #print(response)
    #print(response.content)

    
if __name__ == '__main__':
    post_project("Link A", "Link B", 'ysTDu4SqrMT3sYBMd4zNqDvxn0CMsV', 100, 1000, "asdfghjk")
    
