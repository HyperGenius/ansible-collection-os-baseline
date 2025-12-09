# Role Name: zabbix_agent_core

全サーバーの標準監視エージェントとして **Zabbix Agent 2** を導入します。
OSのベースライン設定の一部として、`os-baseline` コレクションに配置されています。

## Requirements

- RHEL 8 / 9, AlmaLinux, Rocky Linux
- インターネット接続 (Zabbix公式リポジトリへのアクセス)

## Role Variables

| 変数名 | デフォルト値 | 説明 |
| :--- | :--- | :--- |
| `zabbix_version` | `6.0` | Zabbix Agent 2のメジャーバージョン (LTS推奨) |
| `zabbix_server_ip` | `127.0.0.1` | デフォルトのZabbix Server IP (環境ごとに上書きすること) |

## 設計方針

### 1. Zabbix Agent 2 の採用
従来のC言語版Agentではなく、拡張性と並行処理に優れたGo言語版 (Agent 2) を採用しています。

### 2. 設定の分離 (conf.dパターン)
- `zabbix_agent2.conf` 本体は最小限の設定（PidFile, LogFile等）にとどめます
- `Include=/etc/zabbix/zabbix_agent2.d/*.conf` を設定し、`ServerActive` や `Hostname` 等の環境固有値は別ファイルで管理する設計としています
- 環境固有の設定は `/etc/zabbix/zabbix_agent2.d/` 配下に別途配置してください

### 3. リポジトリ管理
Zabbix公式リポジトリを使用し、GPG鍵の検証を行っています。

## Dependencies

なし

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - role: os_baseline.rhel_baseline.zabbix_agent_core
      vars:
        zabbix_version: "6.0"
        zabbix_server_ip: "192.168.1.100"
```

### 環境固有設定の例

このRoleは基本設定のみを行います。環境固有の設定は `/etc/zabbix/zabbix_agent2.d/` に配置してください。

例: `/etc/zabbix/zabbix_agent2.d/server.conf`
```
ServerActive=192.168.1.100
Hostname=web-server-01
```

## License

Private

## Author Information

HyperGenius
