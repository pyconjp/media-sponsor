# 1日目ライトニングトークから

PyCon JP 2017では、１日目、２日目ともにクロージングでライトニングトークを行いました。

今年のライトニングトークは両日とも8枠用意しました。
トーク希望者には会場に用意していあるトークボードに開催内容を記載していただきましたが、開場後すぐに用意した8枠が埋まってしまうほどの人気でした。

ここでは、カンファレンス1日目のクロージングに行われたライトニングトークから２つを紹介します。
なお、当日の発表者と発表内容の一覧、および動画のリンクを後述していますのでぜひご覧になってください。



## １つ目は、Miyazaki Yusuke氏による「Introducing wsgi_lineprof」です。

ここに写真を挿入

Miyazaki氏は、自身で作成したWEBアプリケーションのプロファイラ「wsgi_lineprof」についてお話をされました。
氏は、ISUCONに参加された際の経験
ISUCONでは、限られた時間の中で既存のアプリケーションをより早く動くようにチューニングし、ベンチマークの数値を競います。

チューニングをするためにアプリケーションのボトルネックとなっている箇所を特定していきますが、そのためにはプロファイラの使用が必須です。
Python標準のプロファイラを含め多くのプロファイラが存在しますが、ISUCONのように短い時間の中で結果を出さなければならない状況では、
複雑な設定が必要になるようなものは使うのが難しいとのことです。

そういった課題をクリアするために、WSGIのミドルウェアとして「wsgi_lineprof」を作成しました。
本プロファイルはWSGIに対応しているアプリケーションやフレームワークを使用していれば動作が可能とのことです。

WEBアプリを作るのが好きな人。
そして、今よりも早く動かしたいと思っている人にぜひ使ってみて欲しいと話されました。

今後は、ISUCONでPythonを使って結果を残していきたいと意気込みを語っていました。



## ２つ目は、Takuya Noguchi氏による「OSS-Friday」の紹介です。

ここに写真を挿入

これから書く


# ライトニングトークの一覧
1日目の内容を以下の通りです。
* ギャル語ほんやく : PyLadies Tokyo hack-a-thon
* Introducing wsgi_lineprof : Yusuke Miyazaki(https://github.com/ymyzk)
* Respect the Built-in Names : Hayao Suzuki(https://twitter.com/cardinalxaro)
* 誰でも簡単に暗号通貨の取引Botを作れるようにしてみた : Daiki Shiroi(https://twitter.com/catcat_festival)
* Pythonが動く仕組み : Yoshiaki Shibutani(https://github.com/yotchang4s)
* OSS Friday : Takuya Noguchi(https://twitter.com/tn961ir?lang=ja)
* Dockerをローカルでドカドカ使う(from RejectCon) : @nasa9084
* 多言語の菓子の音声認識 : @RenyuanLyu

[PyCon JP 2017 クロージング動画](https://www.youtube.com/watch?v=cUewj2kRrbk&index=4&list=WL)


# 次回は？
1日目のカンファレンスレポート、いかがでしたでしょうか。PyCon JP 2017のカンファレンスは2日間で40を超えるセッションが開催されました。今回紹介できなかったセッションに下記のリンクから、ビデオや資料を見ることができますのでぜひご覧になってください。

[PyCon JP 2017 トーク一覧]()

次回、カンファレンス２日目のレポートもお楽しみに！
