import logging

from creates import create_user, create_domain, create_polices
from simple_list import get_token, list_domains, list_projects, list_users, list_groups, list_roles, domain_details, \
    domain_group_roles, \
    domain_group_role, user_groups, list_policies, list_regions

if __name__ == "__main__":
    logging.basicConfig(filename='script-keystone.log', filemode='w', level=logging.DEBUG)
    logging.debug('starting...')

    keystone_url = "http://192.168.99.100:5000/"
    token = None

    domains_id = []
    projects_id = []
    users_id = []
    groups_id = []
    roles_id = []

    token = get_token(keystone_url)
    """
    ###### LISTS
    # domains
    data = list_domains(keystone_url, token)
    for domain in data['domains']:
        domains_id.append(domain['id'])

    # projects
    data = list_projects(keystone_url, token)
    for project in data['projects']:
        projects_id.append(project['id'])

    # users
    data = list_users(keystone_url, token)
    for user in data['users']:
        users_id.append(user['id'])

    # groups
    data = list_groups(keystone_url, token)
    for group in data['groups']:
        groups_id.append(group['id'])

    # roles
    data = list_roles(keystone_url, token)
    for role in data['roles']:
        roles_id.append(role['id'])

    list_policies(keystone_url, token)
    list_regions(keystone_url, token)

    ###### DETAILS
    for id_ in domains_id:
        domain_details(id_, keystone_url, token)

    # Create
    # create_group(keystone_url, token)"""
    create_domain(keystone_url, token)
    """# create_user(keystone_url, token)
# create_polices(keystone_url, token)

# Relationship
# PUT
# domain_group_role('default', 'f8400711f1664a6284ec6c85cb47c697', 'af74f15a4d19442db118f86b8b1b0e17')

###### GET
for id in groups_id:
    domain_group_roles(group_id=id, keystone_url=keystone_url, token=token,
                       domain_id='default')

for id in users_id:
    user_groups(id, keystone_url, token)"""
