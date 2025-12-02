# Role Name: security

OSのセキュリティ堅牢化（Hardening）を行います。
SSHD設定、Firewalld、SELinux、不要サービスの停止を一括管理します。

## Role Variables

| 変数名 | デフォルト値 | 説明 |
| :--- | :--- | :--- |
| `security_sshd_permit_root_login` | `no` | RootでのSSH直接ログイン許可 (yes/no/prohibit-password) |
| `security_sshd_password_auth` | `no` | パスワード認証の許可 (公開鍵認証を強制する場合はno) |
| `security_firewalld_enabled` | `true` | Firewalldの有効化 |
| `security_firewalld_allowed_services` | `[ssh]` | Firewalldで許可するサービス名のリスト |
| `security_selinux_state` | `enforcing` | SELinuxの状態 (enforcing/permissive/disabled) |

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: mycompany.rhel_baseline.security
      vars:
        security_sshd_permit_root_login: "no"
        security_firewalld_allowed_services:
          - ssh
          - http
          - https
