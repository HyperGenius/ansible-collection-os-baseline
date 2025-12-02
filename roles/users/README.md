# Role Name: users

システム管理者および一般ユーザーのアカウント作成、SSH公開鍵の配置、Sudo権限の設定を行います。
パスワードハッシュはAnsible Vaultで暗号化して渡すことを推奨します。

## Role Variables

| 変数名 | デフォルト値 | 説明 |
| :--- | :--- | :--- |
| `users_admin_group` | `wheel` | 管理者権限を付与するグループ名 |
| `users_accounts` | `[]` | 作成するユーザー情報のリスト（辞書形式） |

### `users_accounts` list structure

| Key | 必須 | 説明 |
| :--- | :--- | :--- |
| `name` | Yes | ユーザー名 |
| `groups` | No | 所属サブグループ（リスト） |
| `ssh_key` | No | SSH公開鍵文字列（ssh-rsa ...） |
| `state` | No | `present` (作成) / `absent` (削除) |

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: mycompany.rhel_baseline.users
      vars:
        users_accounts:
          - name: "admin_user"
            groups: ["wheel"]
            ssh_key: "ssh-rsa AAAAB3NzaC..."
          - name: "retired_employee"
            state: "absent" # 退職者のID削除もコードで管理
