import json
import logging

import requests

from simple_list import get_token


def list_domains():
    headers = {'X-Auth-token': token}

    response = requests.get(url=keystone_url + '/authzforce-ce/domains',
                            headers=headers)

    if response.status_code in (201, 200):
        return response.text
    else:
        logging.error('LISt DOMAINS ### ' + response.text)


def delete_domain(id):
    headers = {'X-Auth-token': token}

    response = requests.delete(url=keystone_url + '/authzforce-ce/domains/' + id,
                            headers=headers)

    if response.status_code in (201, 200):
        return response.text
    else:
        logging.error('DELETE DOMAINS ### ' + response.text)

if __name__ == "__main__":
    logging.basicConfig(filename='script-authzforce.log', filemode='w', level=logging.DEBUG)
    logging.debug('starting...')

    keystone_url = "http://192.168.99.100:8080"
    token = None

    token = get_token(keystone_url)

    list_domains()
