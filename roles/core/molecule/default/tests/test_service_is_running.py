# roles/core/molecule/default/tests/test_service_is_running.py


def test_service_is_running(host):
    """サービスが起動しているか確認"""
    service = host.service("crond")
    assert service.is_running, "crond サービスが実行されていません"
    assert service.is_enabled, "crond サービスが有効化されていません"
