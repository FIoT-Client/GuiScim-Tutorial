from __future__ import print_function

import requests
import json
import logging


def get_token(keystone_url):
    logging.debug('getting token...')

    json_payload = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": "idm",
                        "domain": {"id": "default"},
                        "password": "idm"
                    }
                }
            }
        }
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url=keystone_url + '/v3/auth/tokens',
                             data=json.dumps(json_payload),
                             headers=headers)

    if response.status_code in (201, 200):
        token = response.headers['X-Subject-Token']
        logging.info('TOKEN --- ' + token)
        return token
    else:
        logging.error('GET TOKEN ### ' + response.text)


def list_domains(keystone_url, token):
    headers = {'X-Auth-token': token}

    response = requests.get(url=keystone_url + '/v3/domains',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('LIST DOMAINS ### ' + response.text)


def list_projects(keystone_url, token):
    headers = {'X-Auth-token': token, 'Content-type': 'application/json'}

    response = requests.get(url=keystone_url + '/v3/projects',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('LIST PROJECTS ### ' + response.text)


def list_users(keystone_url, token):
    headers = {'X-Auth-token': token, 'Content-type': 'application/json'}

    response = requests.get(url=keystone_url + '/v3/users',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('LIST USERS ### ' + response.text)


def list_groups(keystone_url, token):
    headers = {'X-Auth-token': token, 'Content-type': 'application/json'}

    response = requests.get(url=keystone_url + '/v3/groups',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('LIST GROUPS ### ' + response.text)


def list_roles(keystone_url, token):
    headers = {'X-Auth-token': token, 'Content-type': 'application/json'}

    response = requests.get(url=keystone_url + '/v3/roles',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('LIST ROLES ### ' + response.text)


def list_policies(keystone_url, token):
    headers = {'X-Auth-token': token, 'Content-type': 'application/json'}

    response = requests.get(url=keystone_url + '/v3/policies',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('LIST POLICIES ### ' + response.text)


def list_regions(keystone_url, token):
    headers = {'X-Auth-token': token, 'Content-type': 'application/json'}

    response = requests.get(url=keystone_url + '/v3/regions',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('LIST REGIONS ### ' + response.text)


def domain_details(domain_id, keystone_url, token):
    headers = {'X-Auth-token': token, 'Content-type': 'application/json'}

    response = requests.get(url=keystone_url + '/v3/domains/' + domain_id,
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
    else:
        logging.error('DOMAIN DETAILS ### ' + response.text)


def domain_group_roles(group_id, keystone_url, token, domain_id='default'):
    headers = {'X-Auth-token': token, 'Content-type': 'application/json'}

    response = requests.get(url=keystone_url + '/v3/domains/' + domain_id + '/groups/' + group_id + '/roles',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
    else:
        logging.error('RELATIONS DOMAIN GROUP ROLES ### ' + response.text)


def domain_group_role(group_id, role_id, keystone_url, token, domain_id='default'):
    headers = {'X-Auth-token': token, 'Content-Type': 'application/json'}
    response = requests.put(url=keystone_url + '/v3/domains/' + domain_id + '/groups/' + group_id + '/roles/' + role_id,
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
    else:
        logging.error('PUT RELATIONS DOMAIN GROUP ROLES ### ' + response.text)


def user_groups(user_id, keystone_url, token):
    headers = {'X-Auth-token': token, 'Content-Type': 'application/json'}
    response = requests.get(url=keystone_url + '/v3/users/' + user_id + '/groups',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
    else:
        logging.error('GET RELATIONS USERS GROUPS ### ' + response.text)
