#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_cli

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=napalm_cli, commands=["show interfaces summary"])

print_result(results)