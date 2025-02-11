#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_configure, napalm_cli

nr = InitNornir(config_file="config.yaml")

results = nr.run(task=napalm_configure, dry_run=False, configuration="interface loopback 1000")

print_result(results)