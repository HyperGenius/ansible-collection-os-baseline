# Ansible Collection: os_baseline.rhel_baseline

![CI Status](https://img.shields.io/badge/build-passing-brightgreen)
![Ansible Version](https://img.shields.io/badge/ansible-2.9%2B-blue)
![License](https://img.shields.io/badge/license-Private-red)

**RHEL系OS（RHEL/AlmaLinux/Rocky）の標準構成管理を行うAnsible Collectionです。**

本コレクションは、OSの「ベースライン（最低限あるべき姿）」を定義し、環境ごとの差異（開発・本番・DR）を変数によって吸収する設計となっています。
手動手順による設定ミスや、プロジェクトごとの設定のバラつき（属人化）を排除することを目的としています。

---

## 📦 Included Roles (収録ロール)

本コレクションには以下の機能別ロールが含まれています。
詳細は各ロールディレクトリ内の `README.md` を参照してください。

| Role Name | Description | Scope (責務) |
| :--- | :--- | :--- |
| **[core](roles/core/)** | OS基本設定 | タイムゾーン、ロケール、必須パッケージ、Network等の「足回り」設定。 |
| **[security](roles/security/)** | セキュリティ堅牢化 | SSHD設定、Firewalld、SELinux、パスワードポリシー等のコンプライアンス準拠設定。 |
| **[users](roles/users/)** | アカウント管理 | 管理者ユーザー作成、SSH鍵配布、Sudoers権限管理。 |
| **[monitoring](roles/monitoring/)** | 監視エージェント | Zabbix Agent, Datadog, Fluentd等のインストールと初期設定。 |
| **[zabbix_agent_core](roles/zabbix_agent_core/)** | Zabbix Agent 2 | 全サーバー標準監視エージェント（Zabbix Agent 2）のインストールと基本設定。 |

---

## 🚀 Installation

### 1. ローカル開発環境 (Online)
`ansible.cfg` で設定されたパスにインストールします。

```bash
# GitHubから直接インストールする場合（SSH設定済み）
ansible-galaxy collection install git@github.com:HyperGenius/ansible-collection-os-baseline.git
```

### 2. クローズド環境への持ち込み (Offline / JTC Style)
インターネット接続のない環境へ適用する場合、ビルド済みのTarballを使用します。

#### 1. Build (開発機)

```bash
ansible-galaxy collection build
# => os_baseline-rhel_baseline-1.0.0.tar.gz が生成されます
```

#### 2. Transfer (ターゲット環境)

生成された .tar.gz ファイルをターゲット環境へ転送します。

#### 3. Install (ターゲット環境)

```bash
ansible-galaxy collection install os_baseline-rhel_baseline-1.0.0.tar.gz
```
```

## 📖 Usage
Playbookからは、名前空間付きのFQCN (os_baseline.rhel_baseline.role_name) で呼び出してください。

site.yml (Example)
```yaml
---
- name: Apply OS Baseline
  hosts: all
  become: true
  
  # 変数は group_vars/ または inventory で管理することを推奨
  vars:
    core_timezone: "Asia/Tokyo"
    security_sshd_permit_root_login: "no"

  roles:
    # 1. 基本設定
    - role: os_baseline.rhel_baseline.core
    
    # 2. セキュリティ堅牢化 (coreの後に実行)
    - role: os_baseline.rhel_baseline.security
    
    # 3. ユーザー管理
    - role: os_baseline.rhel_baseline.users
      vars:
        users_accounts:
          - name: admin-user
            groups: [wheel]
            ssh_key: "{{ vault_admin_ssh_key }}"

    # 4. 監視エージェント (本番のみ適用する例)
    - role: os_baseline.rhel_baseline.monitoring
      when: env_type == 'production'
    
    # 5. Zabbix Agent 2 (全サーバー標準監視)
    - role: os_baseline.rhel_baseline.zabbix_agent_core
      vars:
        zabbix_version: "6.0"
        zabbix_server_ip: "192.168.1.100"
```

## 🛠 Development & Testing

本コレクションは Molecule + Docker による自動テスト環境をサポートしています。  
PRを作成する前に、ローカル環境でテストを通過させてください。

### Prerequisites
- Docker Desktop (or OrbStack / Colima)
- Python 3.9+
- Ansible 2.10+

### Run Tests
```bash
# 依存ライブラリのインストール
pip install molecule molecule-plugins[docker] ansible-lint

# 全ロールのLintチェック
ansible-lint

# 特定ロールのテスト実行 (例: core)
cd roles/core
molecule test
```


## 📐 Architecture Philosophy (設計思想)

### 1. Separation of Concerns (関心事の分離):

1つの巨大なRoleを作らず、機能ごとに適度な粒度でRoleを分割しています。

ミドルウェア（Apache/Nginx等）の設定はこのコレクションには含めません。

### 2. Secure by Default:

変数を上書きしない限り、最も安全な設定（Rootログイン不可、不要ポート閉鎖）が適用されるようにデフォルト値を設計しています。

### 3. Environment Agnostic:

IPアドレスやホスト名などの環境固有値はハードコードせず、必ず変数 (vars) として外出ししています。
