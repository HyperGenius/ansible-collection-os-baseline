# Role Name: monitoring

監視エージェント（Zabbix Agent, Datadog Agent, Fluentdなど）のインストールと設定を行います。
環境変数やInventory変数で接続先サーバーを切り替え可能です。

## Role Variables

| 変数名 | デフォルト値 | 説明 |
| :--- | :--- | :--- |
| `monitoring_zabbix_enabled` | `true` | Zabbix Agentのインストール要否 |
| `monitoring_zabbix_server_ip` | `127.0.0.1` | Zabbix Server/ProxyのIPアドレス |
| `monitoring_fluentd_enabled` | `false` | Fluentd (td-agent) のインストール要否 |

## Dependencies

- `mycompany.rhel_baseline.core` (リポジトリ設定などのため)

## Example Playbook

```yaml
- hosts: prod_servers
  roles:
    - role: mycompany.rhel_baseline.monitoring
      vars:
        monitoring_zabbix_server_ip: "192.168.10.50"
