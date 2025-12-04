# roles/core/molecule/default/tests/test_default.py


def test_hosts_file(host):
    """hostsファイルが存在し、root所有であることを確認するサンプル"""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
