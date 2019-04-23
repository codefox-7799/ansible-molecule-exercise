import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_molecule_hello_world_file(host):
    f = host.file('/tmp/molecule_hello_world')
    assert f.exists
    assert f.content_string in 'Molecule Hello World!'
