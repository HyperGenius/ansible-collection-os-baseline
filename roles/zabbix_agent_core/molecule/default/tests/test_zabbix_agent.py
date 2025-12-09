# roles/zabbix_agent_core/molecule/default/tests/test_zabbix_agent.py


def test_zabbix_agent2_package_installed(host):
    """zabbix-agent2 パッケージがインストールされていることを確認"""
    pkg = host.package("zabbix-agent2")
    assert pkg.is_installed, "zabbix-agent2 パッケージがインストールされていません"


def test_zabbix_agent2_service_running(host):
    """zabbix-agent2 サービスが active (running) であることを確認"""
    svc = host.service("zabbix-agent2")
    assert svc.is_running, "zabbix-agent2 サービスが起動していません"


def test_zabbix_agent2_service_enabled(host):
    """zabbix-agent2 サービスが enabled であることを確認"""
    svc = host.service("zabbix-agent2")
    assert svc.is_enabled, "zabbix-agent2 サービスが自動起動設定されていません"


def test_zabbix_agent2_port_listening(host):
    """TCP 10050 でリッスンしていることを確認"""
    socket = host.socket("tcp://10050")
    assert socket.is_listening, "ポート 10050 でリッスンしていません"


def test_zabbix_agent2_process_exists(host):
    """zabbix_agent2 プロセスが存在することを確認"""
    processes = host.process.filter(comm="zabbix_agent2")
    assert len(processes) > 0, "zabbix_agent2 プロセスが存在しません"


def test_zabbix_agent2_d_directory_exists(host):
    """拡張設定ディレクトリ zabbix_agent2.d が存在することを確認"""
    directory = host.file("/etc/zabbix/zabbix_agent2.d")
    assert directory.exists, "/etc/zabbix/zabbix_agent2.d ディレクトリが存在しません"
    assert directory.is_directory, "/etc/zabbix/zabbix_agent2.d がディレクトリではありません"
    assert directory.user == "root", "/etc/zabbix/zabbix_agent2.d の所有者が root ではありません"
    assert directory.group == "root", "/etc/zabbix/zabbix_agent2.d のグループが root ではありません"
    assert directory.mode == 0o755, "/etc/zabbix/zabbix_agent2.d のパーミッションが 0755 ではありません"


def test_zabbix_agent2_conf_includes_d_directory(host):
    """zabbix_agent2.conf に Include 設定が含まれていることを確認"""
    conf_file = host.file("/etc/zabbix/zabbix_agent2.conf")
    assert conf_file.exists, "/etc/zabbix/zabbix_agent2.conf が存在しません"
    assert conf_file.contains("Include=/etc/zabbix/zabbix_agent2.d/*.conf"), \
        "zabbix_agent2.conf に Include=/etc/zabbix/zabbix_agent2.d/*.conf が含まれていません"
