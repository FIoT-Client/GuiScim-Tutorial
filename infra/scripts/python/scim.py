import json
import logging

import requests

from simple_list import get_token


def list_users(keystone_url, token):
    headers = {'X-Auth-token': token}

    response = requests.get(url=keystone_url + '/v3/OS-SCIM/v2/Users/',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('LIST USERS ### ' + response.text)


def users_info(users_id, keystone_url, token):
    headers = {'X-Auth-token': token}

    response = requests.get(url=keystone_url + '/v3/OS-SCIM/v2/Users/' + users_id,
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('USER INFO ### ' + response.text)


def list_organizations(keystone_url, token):
    headers = {'X-Auth-token': token}

    response = requests.get(url=keystone_url + '/v3/OS-SCIM/v2/Organizations',
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('LIST ORGS ### ' + response.text)


def organizations_info(org_id, keystone_url, token):
    headers = {'X-Auth-token': token}

    response = requests.get(url=keystone_url + '/v3/OS-SCIM/v2/Organizations/' + org_id,
                            headers=headers)

    if response.status_code in (201, 200):
        parsed = json.loads(response.text)
        logging.info(json.dumps(parsed, indent=4, sort_keys=True))
        return parsed
    else:
        logging.error('ORG INFO ### ' + response.text)


if __name__ == "__main__":
    logging.basicConfig(filename='script-scim.log', filemode='w', level=logging.DEBUG)
    logging.debug('starting...')

    keystone_url = "http://192.168.99.100:5000/"
    token = None
    users_id = []
    organizations_id = []

    token = get_token(keystone_url)

    data = list_users(keystone_url, token)
    for role in data['Resources']:
        users_id.append(role['id'])

    for id in users_id:
        users_info(id, keystone_url, token)

    data = list_organizations(keystone_url, token)
    for role in data['Resources']:
        organizations_id.append(role['id'])

    for id in organizations_id:
        organizations_info(id, keystone_url, token)
