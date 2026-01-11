
### Command

```sh
# app 追加
$ mkdir sample
$ docker compose exec app uv run django-admin startapp sample sample

http://127.0.0.1:8000/
http://127.0.0.1:8000/map/
http://127.0.0.1:8000/admin/

# セキュリティチェック
$ docker compose exec app uv tool run djcheckup http://host.docker.internal:8000/web/
```

```sh
# ライブラリ追加
$ docker compose exec app uv add "Django==6.0"
# dev用のライブラリ追加
$ docker compose exec app uv add "djlint==1.36.4" --dev
```

### Devin

- [Devin's Machine](https://app.devin.ai/workspace) でリポジトリ追加

#### 1.Git Pull
- そのまま

#### 2.Configure Secrets
```sh
# 環境変数用のファイル作成
$ touch .envrc
$ cp .envrc.example .envrc

$ direnv allow
or
$ source .envrc
```
- Google Console で Maps JavaScript API を有効にし、API Key を取得し、.envrc の GOOGLE_MAPS_API_KEY を更新

- ローカル用
```sh
$ brew install direnv
```
#### 4.Maintain Dependencies
```sh
$ docker compose up -d

# コンテナ作り直し
$ source ./remake_container.sh
```

#### 5.SetUp Lint
```sh
$ docker compose exec app uv run task check

- 下記を実行
# ruff によるチェック
$ docker compose exec app uv run ruff check .
# pyrefly による型ヒントチェック
$ docker compose exec app uv run pyrefly check --summarize-errors
$ docker compose exec app uv run pyrefly check --remove-unused-ignores
# djlint で HTML をチェック
$ docker compose exec app uv run djlint templates --extension html

# 参考) 最初の１回のみ実行、pyrefly の初期化
$ docker compose exec app uv run pyrefly init
```

#### 6.SetUp Tests
- no tests ran in 0.00s だと Devin の Verify が通らないっぽい
```sh
$ docker compose exec app uv run task test

- 下記を実行
$ docker compose exec app uv run pytest
```

### 7.Setup Local App

```sh
$ http://127.0.0.1:8000/がアプリケーションのURL
```

#### 8.Additional Notes
- 必ず日本語で回答してください
- Python, Django を利用する
- データベースは Postgres
- テストは pytest を利用する
を入力

#### Migration
```sh
$ docker compose exec app uv run task migration

- 下記を実行
$ docker compose exec app uv run python manage.py makemigrations
$ docker compose exec app uv run python manage.py migrate
```

#### 修正
```sh
$ docker compose exec app uv run task fix

- 下記を実行
$ docker compose exec app uv run ruff check . --fix \
    && docker compose exec app uv run ruff format . \
    && docker compose exec app uv run djlint templates --extension html --reformat
```

### カスタムコマンド
```sh
- SampleModel に 3 件データのダミーデータを追加
$ docker compose exec app uv run python manage.py sample_command 3
```
