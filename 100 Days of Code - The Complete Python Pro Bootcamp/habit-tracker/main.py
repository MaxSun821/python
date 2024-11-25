import requests
from config import *

# Create a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Post a pixela
# response = requests.post(url=record_endpoint, json=record_params, headers=headers)
# print(response.text)

# Update a pixela
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

# Delete a pixela
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)