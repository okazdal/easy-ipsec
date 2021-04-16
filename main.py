# -*- coding: utf-8 -*-
from router_list import routers
from itertools import permutations
from router import Router


def main():
    username = 'admin'
    password = ''

    # ADD IPSec profile and proposal
    for r in routers:
        router = Router(r['wan_ip'], user="admin", passwd="")
        router.add_proposal_profile()

    # IPSec configuration
    key = 'thisisaverysecureawesomepassword'
    for i in permutations(routers, 2):
        # print(i)
        router = Router(i[0]['wan_ip'], user='admin', passwd='')
        router.config_ipsec(remote_domain=i[1]['local_net'],
                            remote_peer=i[1]['wan_ip'],
                            shared_key=key)


if __name__ == '__main__':
    main()
