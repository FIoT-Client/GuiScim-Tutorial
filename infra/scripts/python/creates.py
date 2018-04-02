import json
import logging

import requests


def create_group(keystone_url, token):
    json_payload = {
        "group": {
            "description": "Contract developers",
            "domain_id": "default",
            "name": "Contract developers"
        }
    }

    headers = {'X-Auth-token': token, 'Content-Type': 'application/json'}
    response = requests.post(url=keystone_url + '/v3/groups',
                             data=json.dumps(json_payload),
                             headers=headers)

    if response.status_code == 201:
        logging.info(response.text)
    else:
        logging.error(response.text)


def create_domain(keystone_url, token):
    json_payload = {
        "domain": {
            "description": "test domain description",
            "enabled": True,
            "name": "test_domain 02"
        }
    }

    headers = {'X-Auth-token': token, 'Content-Type': 'application/json'}
    response = requests.post(url=keystone_url + '/v3/domains',
                             data=json.dumps(json_payload),
                             headers=headers)

    if response.status_code == 201:
        logging.info(response.text)
    else:
        logging.error(response.text)


def create_user(keystone_url, token):
    json_payload = {
        "user": {
            "default_project_id": "idm_project",
            "domain_id": "default",
            "enabled": True,
            "name": "User Test 01",
            "password": "secretsecret"
        }
    }

    headers = {'X-Auth-token': token, 'Content-Type': 'application/json'}
    response = requests.post(url=keystone_url + '/v3/users',
                             data=json.dumps(json_payload),
                             headers=headers)

    if response.status_code == 201:
        logging.info(response.text)
    else:
        logging.error(response.text)


def create_polices(keystone_url, token):
    json_payload = {
        "policy": {
            "blob": "{'foobar_user': 'role:member'}",
            "type": "application/json"
        }
    }

    headers = {'X-Auth-token': token, 'Content-Type': 'application/json'}
    response = requests.post(url=keystone_url + '/v3/policies',
                             data=json.dumps(json_payload),
                             headers=headers)

    if response.status_code == 201:
        logging.info(response.text)
    else:
        logging.error(response.text)
