import requests
from datetime import datetime
import os

# replace usermane and token with your name
TOKEN =os.environ.get("TOKEN")
USERNAME =os.environ.get("USERNAME")

pixela_endpoint = "https://pixe.la/v1/users"
#? creating an account
required_parameters ={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response1 =requests.post(url=pixela_endpoint,json=required_parameters)
# print(response1.text)

# ? creating a graph
graph_endpoint = f"https://pixe.la/v1/users/USERNAME/graphs"

graph_parameters={
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"hrs",
    "type":"float",
    "color":"sora"
}

headers ={
    "X-USER-TOKEN":TOKEN,
}

# response = requests.post(url=graph_endpoint,json=graph_parameters,headers=headers)
# print(response.text)
# ?creating a pixel
new_pixel_endpoint =f"https://pixe.la/v1/users/USERNAME/graphs/graph1"

today =datetime.now()
pixel_parameters ={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many hours did you code today? ")
}

response3 = requests.post(url=new_pixel_endpoint,json=pixel_parameters,headers=headers)
print(response3.text)