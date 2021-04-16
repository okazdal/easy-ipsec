# -*- coding: utf-8 -*-
import routeros_api
from router_list import routers


class Router(object):
    def __init__(self, ip, user, passwd):
        self.connection_ssl = routeros_api.RouterOsApiPool(ip, username=user, password=passwd,
                                                           # use_ssl=True,
                                                           use_ssl=False,
                                                           port=8728,
                                                           # ssl_verify_hostname=False,
                                                           # ssl_verify=False,
                                                           plaintext_login=True)

        self.ip = ip
        self.username = user
        self.passwd = passwd
        self.api = self.connection_ssl.get_api()
        self.ip_api = self.api.get_resource('/ip/address')
        self.interface_api = self.api.get_resource('/interface')
        self.bridge_api = self.api.get_resource('/interface/bridge')

        for r in routers:
            if ip == r['wan_ip']:
                self.identity = r['identity']
                self.local_net = r['local_net']
                self.local_ip = r['local_ip']
                self.wan_ip = r['wan_ip']

    def disconnect(self):
        self.connection_ssl.disconnect()

    def add_proposal_profile(self):
        profile = self.api.get_resource('/ip/ipsec/profile')
        profile.add(dh_group='modp1024', enc_algorithm='aes-256', hash_algorithm='sha256', name='proposal_1')
        proposal = self.api.get_resource('/ip/ipsec/proposal')
        proposal.add(auth_algorithms='sha256', enc_algorithms='aes-256-cbc', name='proposal1')

    def config_ipsec(self, remote_domain, remote_peer, shared_key):
        peer = self.api.get_resource('/ip/ipsec/peer')
        peer.add(name=remote_peer, local_address=self.wan_ip, address=remote_peer + '/32', profile='proposal_1')
        identity = self.api.get_resource('/ip/ipsec/identity')
        identity.add(notrack_chain='prerouting', peer=remote_peer, secret=shared_key)
        policy = self.api.get_resource('/ip/ipsec/policy')
        policy.add(dst_address=remote_domain, peer=remote_peer, src_address=self.local_net,
                   tunnel='yes')

    def reset_config(self):
        self.api.get_binary_resource('/').call('system/reset-configuration', {'no-defaults': 'yes'})

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)