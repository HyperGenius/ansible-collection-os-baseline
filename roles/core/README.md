# Role Name: core

RHEL系OSの基本設定を行います。
タイムゾーン、ロケール、必須パッケージのインストール、ネットワークの基本設定を担当します。

## Requirements

- RHEL 8 / 9, AlmaLinux, Rocky Linux

## Role Variables

| 変数名 | デフォルト値 | 説明 |
| :--- | :--- | :--- |
| `core_timezone` | `Asia/Tokyo` | サーバーのタイムゾーン設定 |
| `core_locale` | `ja_JP.UTF-8` | システムロケール設定 |
| `core_packages_base` | `[curl, vim, git, net-tools]` | 全サーバーに必ずインストールするパッケージリスト |
| `core_enable_ipv6` | `false` | IPv6の無効化設定（JTC環境では無効化が多いため） |

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: os_baseline.rhel_baseline.core
      vars:
        core_timezone: "Asia/Tokyo"
