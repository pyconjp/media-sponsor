PyCon JP は日本国内外の Python ユーザーが一堂に会し、互いに交流を深め、知識を分け合い、新たな可能性を見つけられる場所として毎年 9 月中旬に開催される国際カンファレンスです。

PyCon JP 2020 は、2020 年 8 月 23 日から約１週間に渡るスプリント、8 月 28 日、29 日のカンファレンス、8 月 30 日のチュートリアルと１週間の会期で開催されました。

当初の予定では大田区産業プラザ PiO での開催で準備を進めていましたが、新型コロナウイルス感染症(COVID-19)の影響を考え、オンラインで開催されました。オンライン開催は初の試みでしたが、多数の参加者・視聴者の方が訪れてくださり大盛況のうちに PyCon JP 2020 は幕を閉じました。

今回は 28 日に行われたカンファレンスの中から、注目セッションの様子と感想について運営スタッフがレポートします。

## 基調講演 ー芝世弐氏

キーノートセッションの 1 日目は、芝世弐氏によるものでした。芝氏は大学で研究・教鞭を執るかたわら、独学で 2017 年から機械学習を始め、同年の将棋電王トーナメントに初参加ながら準優勝。またその翌年には、世界コンピュータ将棋選手権に初参加で優勝してしまうほどの凄腕の研究者(エンジニア)です。今回の講演では、自身の機械学習を学んできた道筋をコンピューター将棋を中心に話されていました。講演前半は氏がコンピューター将棋に興味を持った理由や技術の話、後半は電脳戦などの大会の話や氏の強さの秘訣を話されていました。

氏がコンピューター将棋を始めた当時は、ディープラーニングの題材として将棋を選んでいた人はごく少数であり、そういった理由からも氏はコンピューター将棋を題材に選ぶことにしたと語ります。そして、将棋全般のデータ構造の話に移っていきます。将棋独特のコマの動き方やルールをプログラム上でどのように表現するのかはとても興味深い部分でした。Python のオープンソースライブラリに「python-shogi」というのがあり、氏はこのライブラリを使いプログラムを組んだそうです。

ここで一旦、芝氏は自身のディープラーニングの成果を振り返りました。この段階で作成したプログラムでは将棋の入門者ほどにしか指すことが出来ず、ルール違反なく最後までゲームをやり切ることができる程度、という評価を氏はしました。個人的には、短期間でここまでの成果を出せることが既にすごいことだと感じました。

何回か対戦を繰り返していくうちに、氏の興味が「ノータイムで指して強いものを作りたい」という方向に移っていきます。これは、実際の人間同士の対戦では思考の時間の長さが必ずしも良手を指せる確率と比例しない、ということから着想を得たそうです。そして、「評価関数・枝刈り・高速化・並列化・時間管理」という、氏が目指す強いプログラムを組むために必要なことが洗い出されていきます。

当時は一般的に序盤から終盤まで、同じぐらいの時間を一手に使うことが通説であったのに対して、氏は即指しが出来ないかと考えます。そこで、氏は相手の持ち時間を待つのではなく、相手の指し手を仮読みする(ponder)を複数行い、ponder が当たる割合を上げていく事にしました。相手の持ち時間の間に自分の指し手を読む事によって、自分の差し時間を短くすることが可能になりました。ここが、他の開発者とは違う氏の独自技術です。自己対戦を繰り返す他の開発者に対して、他者との対戦を繰り返す事によって、プログラムの精度を上げていきます。

そして、電脳トーナメント、コンピューター将棋世界大会の話になります。ドワンゴ社が主催の電脳トーナメントに参加を決めた氏の思惑は、他の対戦を観戦したり、開発者と話をしたいという気軽なものでした。しかし、あれよあれよという間に準優勝。世界大会の切符を手に入れてしまいます。さすがに世界大会では活躍しなければと思い立ち、プログラムを改良。そしてそのまま優勝してしまいます。その後に参加した大会でも準優勝、優勝を繰り返し、現在でも最強の名をほしいままにしています。そして特筆すべき点、数千万もの予算をかけている開発者が多くいる中、氏の開発にかけた予算はわずかであり、電脳トーナメントの賞金（１００万）で黒字が出るほどで、2020 年現在でもその賞金で開発予算を賄えているそうです。

最後にまとめとして、「とりあえず、やってみる」「出来たものを出してみる」ということが大切であると氏は言っていました。完璧なプログラムを組んでから動かすのではなく、何となく動きそうだったらとりあえず動かしてみて短い期間で試行錯誤を繰り返し最適化を計ったことが大きな勝因であったと氏は振り返りました。

氏の講演は、開発者・技術者に対して非常に多くの示唆に富んだもので、開発をする際に心がけたい tips が満載でした。これからコンピューター将棋を始めてみたいと思った方はもちろん、エンジニアの方々にも是非見て欲しいと思えるような講演でした。

## セッション「数理最適化 × 機械学習コラボレーションによる課題解決」 ー鈴木庸氏

鈴木氏による「数理最適化 × 機械学習コラボレーションによる課題解決」のセッションを紹介します。

鈴木氏はリーディングエッジ社所属のエンジニアで、主に物流の組み合わせの最適化、データ分析に従事しています。Python 歴 は６年ほどで、書籍「Python エンジニア育成推進協会監修 Python3 スキルアップ教科書」の共同著者でもあります。

近年ではデータから機械学習を行った結果をもとに、数理最適化で意思決定を行うことが増えていると氏は語ります。Python であれば、その両方が簡単に出来ると紹介していました。そして、「採用面談のスケジューリング」という実際に氏が経験した課題を取り上げ、課題の解決方法を順を追って話されました。この課題に取り組んだ背景に、応募者とのスキルのミスマッチを防ぎたい、担当面接官の割り当てを自動化したい、というものがありました。これは、どの会社でも解決したい課題ではないでしょうか。

詳細はアーカイブとドキュメント に譲りますが、講演は、課題の設定方法、解決方法、数値化における技術選定、プログラムの実装、計算結果とライブラリやパッケージを紹介しながら進められていきました。

講演内容は機械学習と数理最適化に分けられ、また、取り上げた課題はどの会社でも起こりうるような身近なものであったため、内容はハイレベルながら大変理解しやすい講演でした。特に、機械学習を現在も実務で用いている方には非常に参考になるような tips が多く含まれていたと思います。機械学習を既に実務等で用いている方はもちろん、機械学習をこれから始めようという方にもお勧めしたい講演でした。

## セッション「2020 年代のコンテナ時代の Python アーキテクチャ&デプロイ」 -渋川よしき氏

渋川氏による「2020 年代のコンテナ時代の Python アーキテクチャ&デプロイ」のセッションを紹介します。

渋川氏はフューチャー株式会社所属のエンジニアで、多数の書籍を執筆しているエンジニアです。

セッションの内容は、近年クラウド・コンテナの時代が進んでおり、その中でもコンテナに適した Python の開発を主軸とした話となりました。

まずはコンテナとはどういうものか、VirtualBox や VMWare に代表される仮想化・Docker に代表されるコンテナ・ネイティブ実行での違いをわかりやすく解説。そのうえで開発支援ツール・デプロイツールとしてのコンテナ利用法を紹介されました。
開発支援ツールとしては、本番環境がコンテナ環境でなくとも開発/テスト環境の構築が便利であり、例えば RDS や様々なアプリケーションツールのイメージが配布されておりそれらをネットワークやストレージでの共有の設定も容易にできることがアプリケーションエンジニア視点からメリットが大きいと紹介されました。

発表のなかでは VScode で最近発表された VScodeRemote を主軸に Docker で動いている python のアプリケーションの編集方法について様々な手法を紹介されましたので、詳細については発表資料やアーカイブをご覧ください。

デプロイに関しては AWS、GCP、Azure といった大手のクラウド環境では Docker コンテナをデプロイして動かすことができ、ローカルで開発していたアプリケーションがそのままデプロイできることのメリットを説明。そのうえで本番環境の Docker の作法やコンテナにおける Python アーキテクチャを紹介。

講演全体を通してコンテナをどう運用したらよいか体系的に学べる内容となっており、現在コンテナサービスを使用している、もしくは今後コンテナを用いた運用を考えている方には必見の講演でした。

## セッション「Python × AWS × Serverless 初学者が次の一歩を踏み出すためのテクニック」 - hassaku 氏

hassaku 氏による「Python × AWS × Serverless 初学者が次の一歩を踏み出すためのテクニック」のセッションを紹介します。

hassaku 氏は株式会社サーバーワークス所属のエンジニアです。

AWS のサーバレスに焦点を当てたセッションで、冒頭ではまずサーバーレスの基本のおさらいを紹介。サーバーレスを始めたばかりの方が入門者にもわかりやすい内容となっておりました。

本公演のメインは Serverless Framework を利用したサーバーレス構築に関する Tips となっており、特に

- プロジェクト構成

- ステージ管理

- ロギング

の三点に焦点を当てて紹介しております。

プロジェクト構成・ステージ管理では具体的な実装例を挙げ、Serverless Framework で実装する上でよく困る機密情報の保持の仕方やローカルでの実行方法をなどを紹介しています。

特にロギングの部分では、AWS の cloudwatch Logs Insights によるログのネストした検索ができるように JSON で出力すべきという点と、その実装の方法を複数提示し、実際の業務で壁に突き当たりやすい部分を丁寧にフォローしており、今今困っていなくとも今後かならず課題となる部分なんではないでしょうか。

具体的なコードやディレクトリ構成なども紹介していますのでぜひアーカイブをご覧いただければと思います。

## 次回は

カンファレンス 1 日目のレポートは以上です。今回紹介できなかったセッションも多数あるのですが，それらは下記のリンクから見ることができます。みなさまの気になるセッションやトークは見つかりましたか？

- [Youtube PyCon JP 公式アカウント](https://www.youtube.com/user/PyConJP/featured)

カンファレンス 2 日目のレポートも楽しみにしていてください！