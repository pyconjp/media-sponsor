
導入
@ksugahara

# 2日目基調講演

@nikkie

![写真タイトル](./_static/hogehuga.jpg)

### 資料リンク

* [動画]()
* [スライド]()

# トークセッション（1）

@nikkie

![写真タイトル](./_static/hogehuga.jpg)

### 資料リンク

* [動画]()
* [スライド]()

# トークセッション（2）

@nao_y

![写真タイトル](./_static/hogehuga.jpg)

### 資料リンク

* [動画]()
* [スライド]()

# 新米Pythonistaが贈るAirflow入門 & 活用事例紹介のレポート

(@HiraoMotoki)

松田直樹氏による「新米Pythonistaが贈るAirflow入門 & 活用事例紹介」の発表です。
Airflowとは元Airbnb製のPythonで作られたオープンソースで、バッチ処理からなるワークフローのスケジューリング＆モニタリングが可能なプラットフォームです。現在はApacheソフトウェア財団が管理、開発を活発に行なっています。
AirflowではPythonコードでワークフローをDAG（Directed acyclic graph, 有向非巡回グラフとも）表現します。
これによりワークフローを構成するタスクを作成し、処理を実行していきます。

発表では、社内での活用事例を取り上げていました。社内向けのデジタル広告プランニングツールを開発するプロダクトに携わっているそうですが、その中の課題としてデータがRDBに入っていないものがあり必要なデータをたどるのが大変であるという課題がありました。そこで、データマートを作成することで、開発プロダクト用に必要なデータを作成する方法についてお話されていました。
AWS Fargateを使い、その内部でAirflowを使ってカラム名を寄せるなどの処理を実現し、活用可能なデータの取り出しを実現していました。
実現する上でハマったポイントの共有もありました。タスク間のデータのやり取りと、Dockerを用いたローカル開発環境の構築についてお話されていました。

![松田直樹氏](./_static/NaokiMatsuda.jpg)

### 資料リンク

* [動画](https://www.youtube.com/watch?v=T0JVQWfnRAo)
* [スライド](https://speakerdeck.com/matsudan/pycon-jp-2019-xin-mi-pythonistagazeng-ruairflowru-men-and-huo-yong-shi-li-shao-jie)

# Ansibleを通じて「べき等性」を理解してみよう

(@HiraoMotoki)

Kazuya Takei氏による「Ansibleを通じて「べき等性」を理解してみよう」の発表です。
冪等性とはざっくりいうとある操作を何度実行しても、同じ結果になる性質を持つことを意味します。
AnsibleはPython製の構成管理ツールで、主にサーバーのセットアップなどに用いられます。Ansibleでは「動作」でなく「状態」を定義して使用する特徴があります。この理由を設定ファイル内のPlaybackを見ながら説明をなされていました。
同じPlaybackを実行しても2回目以降は状態に変化がないことから、ある操作を何度実行しても同じ結果になるので、
Ansibleは定義された「状態に対する冪等性」を担保されるようになっています。

発表の後半では実際のAnsibleのコードを読みながら、Ansibleが実現している冪等性についてお話されていました。
pip コマンド経由で、Pythonパッケージの状態を管理するpipモジュールを例として取り上げていました。
コードの内部では、求める状態に応じて、地道にコマンドを生成していました。実行結果（リターンコード、標準出力、標準エラー）を見ながら、状態に変化があったかどうかを判定していました。


![Kazuya Takei氏](./_static/KazuyaTakei.jpg)

### 資料リンク

* [動画](https://www.youtube.com/watch?v=Em1xC5bIGl0)
* [スライド](https://attakei.net/slides/pyconjp-2019/index.html/)

# 2日目ライトニングトーク

説明 @ksugahara

## 1つ目タイトル

@nikkie

![写真タイトル](./_static/hogehuga.jpg)


## 2つ目タイトル

@nao_y

![写真タイトル](./_static/hogehuga.jpg)

## 2日目ライトニングトーク一覧

@nikkie

今回ご紹介しきれなかったものも含め、2日目のライトニングトークの一覧はこちらです。また、Pythonの公式アカウントに[ライトニングトークの動画]()がアップロードされています。

# クロージング

@HiraoMotoki
