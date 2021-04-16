## Easy IPSec Configuration Script for MikroTik RouterOS in Python

Using this script you can create IPSec tunnels on RouterOS devices.

This script will configure full mesh IPSec for all the routers configured in routers_list.py
This script will use RouterOS API service to connect to your routers. You can configure API or API-SSL.
By default, script uses API. You can configure router.py, so it uses API-SSL.

### How to use:
- pipenv shell
  
- pipenv install
- Edit routers_list.py. This is a simple python file which contains just a dictionary
with information about your routers.
  
- Edit main.py. Change key variable to a secure password. This will be set as you IPSec shared key.
- Optional. Edit router.py if you want to change IPSec configuration.

- python main.py

### TODO
- Router configuration (IP addresses, local network and remote network) is in .py file for simplicity.
This can be easily modified so configuration can be in a YML file or any other configuration file format.
  
- This script is currently working sequentially. I will also push a concurrent version.
