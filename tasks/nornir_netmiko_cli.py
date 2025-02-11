#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=netmiko_send_config, config_commands="ip scp server enable")

print_result(results)