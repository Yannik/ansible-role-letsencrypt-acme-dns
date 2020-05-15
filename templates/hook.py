#!/usr/bin/env python
import requests
import sys

server = "{{ letsencrypt_acme_dns_server }}"
hosts = {}
{% for subdomain in item.subdomains %}
hosts["{{ subdomain.name }}"] = {
        "subdomain": "{{ subdomain.subdomain }}",
        "user": "{{ subdomain.user }}",
        "password": "{{ subdomain.password }}",
}
{% endfor %}

# possible values: 'deploy_challenge', 'clean_challenge', 'deploy_cert',
#                  'unchanged_cert', 'startup_hook', 'exit_hook'
if sys.argv[1] == "deploy_challenge":
    data = hosts.get(sys.argv[2])
    if data is None:
        print("Couldn't find acme-dns deployment configuration")
        sys.exit(1)
    headers = {
        'X-Api-User': data['user'],
        'X-Api-Key': data['password'],
    }
    data = {
        "subdomain": data['subdomain'],
        "txt": sys.argv[4],
    }

    response = requests.post(server, headers=headers, json=data)
