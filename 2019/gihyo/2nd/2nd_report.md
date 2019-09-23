
導入
@ksugahara

# 2日目基調講演

@nikkie

![写真タイトル](./_static/hogehuga.jpg)

### 資料リンク

* [動画]()
* [スライド]()

# 2日目注目セッション「知ろう！使おう！HDF5ファイル！」 ー thinkAmi

（nikkie）

thinkAmi氏による「知ろう！使おう！HDF5ファイル！」をレポートします。
​
株式会社日本システム技研（所在：長野市）所属のthinkAmi氏は、ブログ「[メモ的な思考的な](https://thinkami.hatenablog.com/)」やDjango Congress JP 2018、2019の登壇などで精力的にアウトプットされています。
今回はHDF5ファイルについてのトークでした。
HDF5ファイルは、例えばKerasを使った機械学習で、モデルの保存に使われますね。
（ちなみに、thinkAmi氏の他の日本システム技研メンバーも今回のPyCon JPで[IoT](https://www.youtube.com/watch?v=ZMjNAay-goQ)や[ライブコーディング](https://www.youtube.com/watch?v=lCQWLAJf6xQ)と多彩な発表をされています！）

最初のパート「知ろう！」では、HDF5ファイルは初めてという方向けにHDF5ファイルの導入がありました。
HDFはHierarchical Data Formatの略で、**階層構造を持ったデータフォーマット**を指します。
エクスプローラーやFinderであるディレクトリの下のディレクトリツリーを見ることができますが、HDF5ファイルは、そのディレクトリツリーをまるごとファイルにしたものと理解しました。
5というのは現在のバージョンで、過去には4というバージョンもあったそうです。
HDF5ファイルは、次の3つの要素から構成されます。

- データそのもので、ファイルに相当する「Dataset」
- Datasetを入れるもので、ディレクトリに相当する「Group」
- DatasetやGroupの注釈となる「Attribute」

HDF5ファイルには、クロスプラットフォームで使えるという特徴があります。

HDF5ファイルを見るためのツールを紹介した後、「使おう！」ということで、いよいよPythonからHDF5を操作します。
サードパーティモジュール`h5py`または`PyTables`で操作できるそうです。
画像やExcelファイルを読み込んで、`create_dataset`メソッドでgroupに保存したり、
`visititems`メソッドでHDF5ファイルを検索してから目的のファイルを開いたりといった操作の紹介がありました。
HDF5ファイルはローカルに保存するだけではなく、REST APIを介してHDF5ファイルを共有できるサーバ（h5serv）や、
サーバの機能をクラウドで使うためのサービス（HSDS）も提供されているそうです。

最後にHDF5ファイルのバージョンについての共有です。
現在の1.8系と1.10系があり、1.8系は2020年5月でパッチリリース終了、また、1.10.2以前と1.10.3以降とでは互換性がないそうです。
このトークを機に触ってみようという方にとってありがたいですね。

機械学習で登場するHDF5ファイルが一体何物なのかがわかりました。
理解を深めるために機械学習で使っているHDF5ファイルの中を覗いてみてもいいかもしれませね。

TODO: 写真がFlickrのAlbumに見当たらないので、他を書き上げてから探す

![写真タイトル](./_static/hogehuga.jpg)

### 資料リンク

* [動画](https://www.youtube.com/watch?v=bSdRlfC2yqA)
* [スライド](https://speakerdeck.com/thinkami/pycon-jp-2019-talk)
* [プレゼン用GitHubリポジトリ](https://github.com/thinkAmi/PyCon_JP_2019_talk)

# トークセッション（2）

@nao_y

![写真タイトル](./_static/hogehuga.jpg)

### 資料リンク

* [動画]()
* [スライド]()

# トークセッション（3）

@HiraoMotoki

![写真タイトル](./_static/hogehuga.jpg)

### 資料リンク

* [動画]()
* [スライド]()


# トークセッション（4）

@HiraoMotoki

![写真タイトル](./_static/hogehuga.jpg)

### 資料リンク

* [動画]()
* [スライド]()

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
