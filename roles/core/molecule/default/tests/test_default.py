# roles/core/molecule/default/tests/test_default.py
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_hosts_file(host):
    """hostsファイルが存在し、root所有であることを確認するサンプル"""
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_service_is_running(host):
    """(例) 何かサービスをインストールした後の確認"""
    # 例えば cron サービスが動いているか
    # service = host.service("crond")
    # assert service.is_running
    # assert service.is_enabled
    pass
