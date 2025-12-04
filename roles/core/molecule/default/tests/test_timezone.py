# roles/core/molecule/default/tests/test_timezone.py


def test_timezone(host):
    """タイムゾーンが Asia/Tokyo になっているか確認.
    timedatectlコマンドの結果や、リンク先を確認する方法などがあります
    """

    # 簡易チェック: /etc/localtime のリンク先を確認
    f = host.file("/etc/localtime")
    assert f.exists
    assert "Tokyo" in f.linked_to
