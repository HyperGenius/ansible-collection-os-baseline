# core/molecule/default/tests/test_locale.py


# ロケール設定確認テスト
def test_locale_setting(host):
    """ロケールが 'ja_JP.UTF-8' に設定されていること
    注意: コンテナ環境では glibc-langpack-ja が必要になる場合がある
    """
    LANG = "ja_JP.UTF-8"

    # 1. command: echo $LANG の確認
    lang_output = host.run("echo $LANG").stdout.strip()
    assert lang_output == LANG, f"LANGが期待値と異なります: {lang_output}"

    # 2. command: echo $LC_ALL の確認
    lc_all_output = host.run("echo $LC_ALL").stdout.strip()
    assert lc_all_output == LANG, f"LC_ALLが期待値と異なります: {lc_all_output}"

    # 2. command: locale の確認
    locale_output = host.run("locale").stdout
    assert f"LANG={LANG}" in locale_output
    assert f"LC_ALL={LANG}" in locale_output
