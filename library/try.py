#!/usr/bin/python
import requests
from ansible.module_utils.basic import *

def main():

    module = AnsibleModule(argument_spec={})
    try:
        r = requests.head("http://nasirhussain.tech")
        response = r.status_code
    except requests.ConnectionError:
        print("Failed to Connect")
    module.exit_json(changed=False, Status_Code=response)


if __name__ == '__main__':
    main()
