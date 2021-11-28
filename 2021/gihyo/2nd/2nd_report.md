先日公開したPyCon JP 2021 1日目のカンファレンスレポートはいかがでしたでしょうか？ 本レポートでは引き続き、2日目の様子をご紹介します。

[PyCon JP](https://www.pycon.jp/)は日本国内外のPythonユーザーが一堂に会し、互いに交流を深め、知識を分け合い、新たな可能性を見つけられる場所として毎年開催される国際カンファレンスです。

[PyCon JP 2021](https://2021.pycon.jp/)は2021年10月15日〜16日のカンファレンスと2日間の会期で開催されました。

今回は16日に行われたカンファレンスの中から、注目セッションと感想について運営スタッフがレポートします。

# Day2 Keynote: A Perfect match - Mr. Brandt Bucher

（nikkie）

この10月にリリースされたPython3.10。
その目玉機能といえば、Structural Pattern Matching（以下、 **パターンマッチ**）ですね！
PyCon JP 2021 2日目のキーノートスピーカーは、[パターンマッチのPEP](https://www.python.org/dev/peps/pep-0622/)の筆頭著者のBrandtさんです。
パターンマッチについて

- History
- Design
- Implementation
- Future

の4つのパートから共有していただきました。

Historyのパートは、過去のswitch文のPEPの紹介（[一例](https://www.python.org/dev/peps/pep-3103/)）から始まりました。
そしてBrandtさんは「*パターンマッチはswitch文ではない*」(Structural Pattern Matching is not a switch statement!) と強調します。
私は十分にキャッチアップできていなかったので、「そうなのかな？」と思ったのですが、キーノートを聞き終わる頃にはswitch文との違い（よりパワフル！）に納得しました。

続くDesignでは、パターンマッチを構成する2つの要素について述べられます。

- 制御フロー（control flow）
- destructuring

キーノートで登場した例ですが、パターンマッチを使ったFizzBuzzのコードは **制御フローがスッキリ** 書けていて衝撃的でした。

```python
def fizzbuzz(number):
    match number % 3, number % 5:
        case 0, 0: return "FizzBuzz"
        case 0, _: return "Fizz"
        case _, 0: return "Buzz"
        case _, _: return str(number)
```

destructuringは耳慣れない言葉でしたが、例を通じて、パターンマッチの中で **オブジェクトから値を取り出す** ことと理解しました。
リスト、辞書、クラスなどは、パターンマッチの中でアンパックや属性アクセスを使うことで、値を取り出して処理を進められます。
これは他の言語のswitch文とは大きく違うところと理解しました。

Implementationでは、バイトコードの解説や、**soft keyword** による後方互換性について説明がありました。
``match match:`` のように書け、過去に書いたコードも修正不要というのは、パターンマッチを導入しやすそうですね。

Futureのパートによると、制御構造として冗長な動きやUnreachable checkを改善していくそうです。

[PEP 636のTutorial](https://www.python.org/dev/peps/pep-0636/)で素振りしたり、
[言語リファレンスのmatch文の項目](https://docs.python.org/ja/3/reference/compound_stmts.html#the-match-statement)を読んでみたりすると
パターンマッチに習熟できそうですね。
パターンマッチを使ったコードを書くのが楽しみになるキーノートでした！

## セッション「Pythonによるアクセスログ解析入門」 - 石原 祥太郎氏

(吉田 健太)

石原氏は株式会社日本経済新聞社所属し上級研究員としてデータ分析・サービス開発に従事しておりKaggle Masterや書籍を執筆している他、INMAが選出する30 Under 30 Awardsにてアジア太平洋部門の最優秀賞を受賞しています。
本発表ではPythonでアクセスログを解析する手法及びそれらを用いたレコメンドなどの活用事例を紹介しています。

![log-ss](./_static/log-ss.png)

新聞社のあり方として紙から電子版に移行しており、公開した記事の反応やレコメンド等においてアクセスログが重要となっています。そして、実際にアクセスログを解析しデータ分析という文脈に落とし込むのがデータサイエンティストの仕事となっています。
では、Pythonを利用するところはどこかというと、データを処理するところでデータを取得後にリアルタイムで可視化・集計しながら、探索したい場合やデータを取得後に高度な処理が必要な場合は現状ではまだSQLだけでは難しく、Pythonを使って加工をしています。
また、実際の処理の仕方として株式会社Gunosyが公開しているデータセットを利用し、データセットの読み込みから記事単位での集計や記事推薦など、pandasを用いたサンプルコードが[Googlecolab上に提供されています](https://colab.research.google.com/drive/1r4GcXWvM-j-dlfT0XF-O-Y5DiyAM-gGq?usp=sharing)。

他にもKaggleへの出題や年齢推定など応用例もあがっていますので、気になる方は[こちらから動画アーカイブや発表資料](https://2021.pycon.jp/time-table/?id=269506)を御覧ください。

## セッション「他人が書いたコードのリファレンスをSphinxで作る方法」 - 杉山 剛氏

(高倉 佑輔)

杉山氏の「[他人が書いたコードのリファレンスをSphinxで作る方法](https://2021.pycon.jp/time-table/?id=271453)」というセッションの紹介をいたします。

杉山氏は事務系のお仕事を33年間勤める傍ら独学でPythonを学び、業務のデータ分析でも最近Pythonを使うようになった方です。また、書籍のレビューを積極的に行っており、過去に14冊もレビューし、さらには現在も1冊レビューの最中とのことです。

このセッションでは、他者が書いたPythonのコードにdocstringをつけていくことを通じて、Pythonコードの保守性をあげていくことを題材としています。Pythonにはコードのドキュメントをわかりやすく記載するdocstringというしくみがあり、これを記載すればSphinxなどのツールを使ってコードのリファレンスをお手軽に作ることができます。

今回のセッションでは、初老の事務系サラリーマンSさん（仮名）が急遽退社する事になってしまった後輩から引き継いだdocstringの無いコードにdocstringを書きながら、コードの全容を把握するためのドキュメントを書いていくというエピソードを題材としています。あくまでもフィクションとのことですが、問題のコードは後輩がデータ分析で書いたコードが気がつくと業務で利用されることになり、その間にWebアプリ化されてコードが書けない人も使うようになったコードです。業務で使われているのだから、メンテナンスができなくなることは死活問題です。

しかし、そのコードにはいろいろな問題がありました。Pythonにはというコーディング規範があるのですが、そのコードは全くPEP-8を守っていない上に、処理内容と辻褄が合わないコメントや冗長な処理など、読みづらくなる要素がてんこ盛りなコードでした。もちろん、テストもありません。Sさんは処理そのものは手を加えずにPEP-8準拠にコードを書き換え間違っているコメントを直していきました。もちろん、docstringを書き加えながら。書き上げたdocstringは、Sphinxによって一瞬でドキュメントになったのでした。そのドキュメントの甲斐あって、テストの追加もリファクタリングも無事できましたとさ。めでたしめでたし。

筆者の経験でも、ドキュメントの無いコードは厄介なモノということを理解しています。しかし、だいたいコードの変更が先になってしまいドキュメントの無いコードが量産されることはよくあることです。そして、そのドキュメントの無いコードをメンテナンスする際に思うことは、「ちゃんとドキュメント書いておけばよかった……」ということだったりします。筆者自身が書いたコードでさえ昔書いたコードの全容を忘れてしまうものですから、他者が書いたドキュメントのないコードを理解するということはあまりにも大変なことなのです。そういう大変なことをSさんはやり遂げたわけです。

## セッション 「Loggingモジュールではじめるログ出力入門」 - 堤 利史氏

(神田 佳積)

堤 利史氏による「[Loggingモジュールではじめるログ出力入門](https://2021.pycon.jp/time-table/?id=272259)」のセッションを紹介します。

堤氏はGMOペパボ株式会社にてデータエンジニアとしてデータ基盤の構築・運用に従事しております。

このセッションではPythonに標準搭載しているloggingモジュールの利用判断基準、構成要素、ならびに、ログ出力方法と実装例に関して取り上げられました。(対象バージョンは3.9)

最初にloggingモジュールの利用判断基準としてprint関数でも良いケースについて説明がありました。
確かにデバッグなり軽い挙動確認等ライフタイムが短く、イベント記録以外の場合はprint関数でも良さげという感じがしました。
また便利ポイントとして説明されたイベント時刻・発生箇所の記録、エラーや警告等ログレベル指定が必要となる場合はloggingモジュールを用いた方が適切という感じがしました。

![print関数でも良い場合について説明する堤氏](./_static/day2_1350_tsutsumi.png)

続いてloggingモジュールの主な構成要素として

1. Logger
1. Level
1. LogRecord
1. Filter
1. Handler
1. Formatter

が存在し、各々の要素についての説明がありました。
Handler、Formatter以外のloggingモジュールの構成要素を無意識に使用していることが多いです。しかし、ログ出力ではファイルに対しても書き出すことがあります。そのため、HandlerやFormatterを意識したログ出力をすると良さそうです。
またloggingモジュールの性質で階層構造についての説明があり、読み込まれた時点でroot logger(全てのLoggerの祖先)が生成されるというのが印象的でした。よく参考書等で直接記録するサンプルコードを見かけますが、これらはroot loggerで行っているものだと改めて認識させられました。ちなみにpropagate属性を用いれば上位のLoggerに伝播できるとのことです。

ログ出力方法としてアプリケーション、ライブラリ各々のお作法、AWSならびにGCPでの出力の仕方について説明がありました。
アプリケーションでの設定では以下設定方法について説明がありました。

1. コードで直接指定
1. `logging.basicCongfig`
1. `logging.config.dictConfig`

またライブラリでは詳細設定を行わず、NullHandlerのみは設定して問題ないとのことでした。

アプリケーションの設定ですと簡単なものでしたらコードで直接指定、クラス構造がはっきりしているものは `logging.config.dictConfig` で行った方が最善ではないかなと説明を聞いていて感じました。

AWSならびにGCPでの出力の仕方については、Twelve-Factor Appを前提としてAWSではLambda及びAWS Glue Python Shellジョブタイプを用いたCloudWatch Logsへの出力、GCPではCloud Functions及びCloud Runを用いたCloud Loggingへの出力のプログラム例について説明がありました。
詳細は割愛しますが、実際にGitHubに[ソースコード](https://github.com/tosh2230/pycon-jp-2021)があるとのことですので、実際に手を動かしてみるのも良いかと思います。

筆者(神田)自身ここ最近Pythonを触り出した者としてLoggingモジュールが標準で用意されていることは知っているものの、構成要素等詳細なところまではわからないところがありました。このセッションでどういう構成要素がどんな動きをするかが理解出来、設定方法のバリエーションやパブリッククラウドでの利用例等も聞けて有意義でした。

Pythonを用いたシステム開発を行っている方に加えて、これから開発に関わる初学者の方にもお勧めしたいセッションでした。

## ライトニングトーク

PyCon JP 2021ではクロージングの前にライトニングトークを行いました。5枠の発表がありましたが、主なものではテプラをMicroPythonを用いて印刷する話やPythonでブラウザを一杯動かしたという話がありました。また海外(インドネシア)からも発表がありました。いずれも興味深く大変盛り上がりました。

カンファレンス 2 日目のレポートは以上です。1 日目と同様に今回紹介できなかったセッションも多数あるのですが，それらは下記のリンクから見ることができます。

- [Youtube PyCon JP 公式アカウント](https://www.youtube.com/user/PyConJP/featured)

みなさまの気になるセッションは見つかりましたか？ぜひ他のセッションも見ていただければと思います！