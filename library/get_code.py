#!/usr/bin/python3

from ansible.module_utils.basic import *
import requests


def get_code(url):
	try:
		response = requests.get(url)
	except requests.HTTPError as e:
		return e.code
	return response.status_code


def main():

	module = AnsibleModule(argument_spec={'url':{'required': True, 'type': 'str'}})
	status_code = get_code(module.params['url'])
	response = {"status": status_code}
	module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()