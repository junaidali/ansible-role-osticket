import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_web_server_running(host):
    s = host.socket("tcp://0.0.0.0:80")
    assert s.is_listening
