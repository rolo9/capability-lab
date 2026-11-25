# Docker環境構築編 — Apple Silicon Mac

Human CapabilityのPython教材を実行するための共通の入口です。**Apple Silicon搭載のMac**を対象に、DockerとGitで環境を作ります。初回はセットアップと動作確認を行い、以後の単元では同じ環境を使います。

## 1. Mac側の準備

[Dockerの公式インストール手順](https://docs.docker.com/desktop/setup/install/mac-install/)で、対応するmacOSと「Mac with Apple silicon」用のDocker Desktopを確認し、インストール後に起動します。Macの「ターミナル」を開き、次を実行します。

```sh
git --version
make --version
docker info --format '{{.ServerVersion}}'
```

GitとMakeは、Mac側で教材を取得して環境構築を指示する道具です。見つからない場合は `xcode-select --install` でAppleのコマンドライン・デベロッパツールを導入してから再確認します。Dockerのコマンドでサーバーのバージョンが表示されれば、Docker Desktopと通信できています。初回は教材や依存パッケージの取得にネット接続を使います。Pythonはこの後に作るコンテナに入っています。

## 2. 教材を取って、コンテナを作る

初めて取得するときは、教材を置きたいフォルダで次を実行します。

```sh
git clone https://github.com/rolo9/capability-lab.git
cd capability-lab
make up
```

取得済みの場合は、使う単元のファイルを含む手元の `capability-lab` フォルダで `make up` を実行します。同じフォルダを使うコンテナが起動済みなら、そのまま次の確認へ進めます。

`make up` は [Makefile](../Makefile) の手順に従い、[Dockerfile](../Dockerfile) からPythonと必要なライブラリを含む**イメージ**を作り、そのイメージから `capability-lab-jupyter` という**コンテナ**を起動します。この名前はこの手順で作るコンテナの名前です。

| どこにあるか | 役割 |
| --- | --- |
| Mac上の `capability-lab` | Gitで取得した教材、CSV、コードを置くフォルダ |
| コンテナ内の `/app` | 同じフォルダが見える場所。Dockerのバインドマウントでつながっている |
| コンテナ内のPython | `/app` のコードを実行する。NotebookのPythonもコンテナ内で動く |

## 3. Pythonと教材がつながっているかを確かめる

```sh
docker exec capability-lab-jupyter python --version
docker exec -w /app capability-lab-jupyter python learning/statistics-ai/01-observations/observe.py
```

最初のコマンドではコンテナ内のPythonのバージョンが表示されます。次のコマンドでは、コンテナ内の `/app` から教材のスクリプトを実行します。**「測定1: 20 ℃、ずれ -2 g」「全体: 9 件、平均 +0.0 g」** が表示されれば、Pythonが起動し、教材のCSVを読めています。スクリプトやCSVが見つからないときは、コンテナを起動したフォルダと、手元にある教材の版を確認します。

Notebookを使う単元では、同じリポジトリのフォルダから `make jupyter` でブラウザを開きます。作業を終えたらファイルを保存し、`make down` でコンテナを停止します。保存した教材や変更はMac側のフォルダに残ります。

[統計・AIの第1単元に進む](../learning/statistics-ai/01-observations/README.md) · [学習索引](../learning/README.md) · [詳しい再現手順](reproduce.md)
