from email.policy import HTTP
from django.shortcuts import render
from griffinsteffy import settings

# Plaid
# import plaid
# from plaid.api import plaid_api

# import requests


# import json

# SANDBOX_INSTITUTION = 'ins_109508'

# configuration = plaid.Configuration(
#     host=plaid.Environment.Sandbox,
#     api_key={
#         'clientId': settings.LOCAL_PLAID_CLIENT_ID,
#         'secret': settings.LOCAL_PLAID_SECRET,
#     }
# )

# api_client = plaid.ApiClient(configuration)
# client = plaid_api.PlaidApi(api_client)

def link(request):
    context = {}
    return render(request, 'category/index.html', context)


def testing(request):
    # data = requests.post('http://localhost:8001/api/create_link_token', {})
    # print(data)
    # data_json = json.dumps(data)
    # link_token = data_json['link_token']
    # print("Link Token: " + link_token)
    # request_id = data_json['request_id']
    # print("Request Id: " + request_id)
    # context = {
    #     'link_token': link_token
    # }
    context = {}
    return render(request, 'category/test.html', context)

# Plaid