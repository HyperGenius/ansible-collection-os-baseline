# core/molecule/default/tests/test_packages.py


# 必須パッケージインストール確認テスト
def test_base_packages_installed(host):
    """READMEにあるデフォルトパッケージが全てインストールされていること
    ターゲット: curl, vim, git, net-tools
    ヒント: リストを使ってループでチェックするとスマート
    """
    packages = ["curl", "vim", "git", "net-tools"]
    for pkg_name in packages:
        pkg = host.package(pkg_name)
        assert pkg.is_installed, f"{pkg_name} がインストールされていません"
