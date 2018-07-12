import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mysql_client_is_installed(host):
    mysql_client = host.package('postgresql-client-9.6')

    assert mysql_client.is_installed


def test_mysql_server_is_installed(host):
    mysql_server = host.package('postgresql-9.6')

    assert mysql_server.is_installed


def test_mysql_is_running(host):
    mysql = host.service('postgresql')

    assert mysql.is_running
