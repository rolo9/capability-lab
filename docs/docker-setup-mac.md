# Docker環境構築編 — Macで初めて始める方へ

このページのゴールは、**手元に教材と実行環境を作り、最初のPythonプログラムがCSVを読めるところまで確認すること**です。Apple Silicon搭載のMacを例に進めます。Appleメニューの「このMacについて」で「チップ」がApple Mシリーズか確認できます。別の環境を使う方は、末尾の[Mac以外で実行する場合](#mac以外で実行する場合)から始めてください。

## 1. GitHubで何を準備するか

やりたいことによって、準備が変わります。

| やりたいこと | 準備 |
| --- | --- |
| 教材を読む・ダウンロードして実行する | この教材は公開されています。GitHubアカウントやログインは不要です。MacにはGitを用意します。 |
| 手元でコードを変え、変更履歴を残す | Gitに自分の名前とメールアドレスを設定します。コミットは手元に残ります。 |
| 自分のGitHubでも学習記録を管理する | GitHubアカウントを作成し、ログインします。元のリポジトリに書き込む権限がなければ、ページ右上の **Fork** から自分のコピーを作ります。手元には自分のコピーをクローンし、GitHub CLIなどで書き込み用の認証を設定します。 |

GitHubでの保存まで行う場合は、[フォークの作り方](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)と、[GitHub CLIのログイン手順](https://cli.github.com/manual/gh_auth_login)を使えます。GitHub CLIをインストールして `gh auth login` を実行し、GitHub.com、HTTPS、ブラウザでのログインを選び、Gitの認証を設定します。フォークを使う場合は、次の取得手順のURLを自分のフォークのURLに置き換えます。

## 2. Macで道具を準備する

MacのSpotlightで「ターミナル」を検索して開きます。次のコマンドを一行ずつ入力し、Enterを押します。

```sh
git --version
make --version
```

どちらもバージョンが表示されれば準備完了です。インストール画面が出たら、Appleのコマンドライン・デベロッパツールをインストールします。表示されずコマンドが見つからない場合は `xcode-select --install` を実行し、インストール後に上の2行をもう一度試します。

続いて、[Dockerの公式手順](https://docs.docker.com/desktop/setup/install/mac-install/)で自分のmacOSが対応していることを確認し、Apple Silicon版のDocker Desktopをインストールして起動します。ターミナルで次を実行します。

```sh
docker info --format '{{.ServerVersion}}'
```

Dockerのサーバーバージョンが表示されたら先に進めます。接続エラーが出たら、Docker Desktopが起動し終わるまで待ってから再実行します。初回は教材と依存パッケージの取得にネット接続を使います。Mac側にPythonを入れる必要はありません。

## 3. 教材を置き、実行環境を作る

初めて教材を取得する方は、ターミナルで次を一行ずつ実行します。最初の2行でホームフォルダに作業場所を作ります。

```sh
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/rolo9/capability-lab.git
cd capability-lab
pwd
```

`git clone` はGitHubの教材を手元にコピーします。`pwd` は、ターミナルが今いる場所を表示します。ここでは末尾が `/Projects/capability-lab` になります。同じ名前のフォルダがあると表示されたら、その場所にはすでにファイルがあります。上書きせず、取得済みのリポジトリならそのフォルダに移動します。使う単元のファイルが手元にあることも確認します。

手元でコミットを作る方は、このフォルダで次のように設定できます。例の名前とメールアドレスは自分の値に置き換えます。公開する記録に個人メールを載せたくない場合は、[GitHubの設定で確認できる noreply アドレス](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)を使えます。

```sh
git config user.name "Your Name"
git config user.email "YOUR_GITHUB_NOREPLY_ADDRESS"
```

同じフォルダで `make up` を実行します。

```sh
make up
```

[Makefile](../Makefile)が、[Dockerfile](../Dockerfile)の定義からPythonなどを含む**イメージ**を作り、そのイメージを使って `capability-lab-jupyter` という**コンテナ**を起動します。初回はダウンロードを伴うので、プロンプトが戻るまで待ちます。コンテナ名が既に使われているという表示が出た場合は、次の手順で、そのコンテナがどのフォルダを使っているか確認してください。

## 4. マウントとPythonを確かめる

**マウント**は、Macのフォルダをコンテナ内からも見えるようにする仕組みです。現在の `make up` は、起動した場所の教材フォルダ全体をコンテナ内の `/app` に接続します。次のコマンドで、実際に起動しているコンテナの接続先を確認できます。

```sh
pwd
docker inspect --format '{{range .Mounts}}{{.Type}} {{.Source}} -> {{.Destination}}{{println}}{{end}}' capability-lab-jupyter
```

2行目の出力に `bind …/capability-lab -> /app` のように表示され、左側が `pwd` で確認した教材フォルダなら、意図したマウントです。別のフォルダが表示された場合は、そのコンテナで作業中のファイルを保存してから停止し、使いたいフォルダで `make up` を実行します。コンテナが見つからなければ、同じフォルダで `make up` の結果を確認します。

続いて、コンテナ内のPythonで教材を実行します。

```sh
docker exec capability-lab-jupyter python --version
docker exec -w /app capability-lab-jupyter python learning/statistics-ai/01-observations/observe.py
```

1行目はコンテナ内のPythonのバージョンを表示します。2行目は、コンテナ内で `/app` に移動して教材のPythonを実行します。**「測定1: 20 ℃、ずれ -2 g」「全体: 9 件、平均 +0.0 g」**が表示されたら完了です。ファイルが見つからない場合は、上のマウント元と、Mac側に教材一式があるかを確認します。

Notebookを使うときはMacのターミナルで `make jupyter` を実行すると、ブラウザで開けます。マウント先の `/app` 以下に保存した変更は手元のフォルダに残ります。GitHubにも残したい変更は、コミットして、1で認証した自分のリポジトリへプッシュします。作業を終えるときは保存してから `make down` でコンテナを停止します。

## Mac以外で実行する場合

以下は環境ごとに置き換える箇所です。この教材で動作確認の記録があるのはApple Silicon Macです。Intel搭載のMacを使う場合は、公式手順で対応するDocker Desktopを確認し、同じ手順で動くか確かめてください。

- **Windows**では、[Docker DesktopのWSL 2統合](https://docs.docker.com/desktop/features/wsl/)を有効にしたLinuxディストリビューションを使います。そのLinux側でGitとMakeを用意し、教材をLinux側のホームフォルダにクローンします。以下の操作もWSLのターミナルで行います。
- **Linux**では、[Docker Engine](https://docs.docker.com/engine/install/)と、使っているディストリビューション向けのGit・Makeを用意します。Dockerが起動し、普段使うユーザーで `docker info` を実行できることを確認します。そのターミナルで教材をクローンします。
- どちらも、[手順3](#3-教材を置き実行環境を作る)の取得コマンドを使えます。取得したリポジトリのルートで `make up` を実行し、[手順4](#4-マウントとpythonを確かめる)でマウントとPythonを確認します。Notebookを開くときは `make jupyter` の代わりに、`docker logs capability-lab-jupyter` で表示される `http://127.0.0.1:8889/…` のトークン付きURLを、そのコンピューターのブラウザで開きます。URLのトークンはログインに使うため、共有しないでください。

[統計・AIの第1単元に進む](../learning/statistics-ai/01-observations/README.md) · [学習索引](../learning/README.md) · [詳しい再現手順](reproduce.md)
