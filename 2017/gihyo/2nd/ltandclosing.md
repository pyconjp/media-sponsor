# LTとクロージング

|項目|詳細|
|-----|-----|
|公式ページ|https://pycon.jp/2017/ja/events/lightning-talks/|
|まとめ|https://togetter.com/li/1149071|

# LT
さて、PyCon JPでは毎回恒例のLT(Lightning Talk)があります。  
プログラムに組み込まれている通常のトークは事前先行がありますが、LTに関しては毎日先着順で申し込むことができます。  
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/pyconjp/36925102386/in/album-72157685754005651/" title="IMG_9139"><img src="https://farm5.staticflickr.com/4418/36925102386_4f710b1433_o.jpg" width="640" height="427" alt="IMG_9139"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  

2日目のLTは全部で8つ。  
競馬でのデータ分析やPythonの設計思想の話など興味深い話が多い中、ここでは2つピックアップしてご紹介したいと思います。  

まずはmomijiameさんによる「Re: Respect the Built-in Names」です。  
<script async class="speakerdeck-embed" data-id="30b883607cf94ce18f56db80f8e4a0d7" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>  
前日のLT「[Re: Respect the Built-in Names](https://speakerdeck.com/hayaosuzuki/respect-the-built-in-names)」（内容：ビルトイン関数への人権侵害はやめよう！）を聞いたのをきっかけに、このLTを思いついたそうです。  
※この「人権侵害」というのは、ビルトイン関数（strやmaxなど）へうっかり代入をしてしまう、あるあるネタのことです。（詳細は[スライド](https://speakerdeck.com/hayaosuzuki/respect-the-built-in-names)参照）
このあるあるを撲滅するために静的コード解析ツールを活用しようということで、今回はPylintを紹介してくれました。  
Pythonコーディング規約のPEP8によると、このような人権侵害を回避する例として\_（アンダースコア）を利用すると良いそうですよ！  

続いてmatsu7874さんによる「PyCon JPで彼女作ってみた。」です。  
[PyCon JPで彼女作ってみた。](https://slideship.com/users/@matsu7874/presentations/2017/09/43ha6mtJX4Z8mfGVBD6oD5/)  
現在彼女がいないmatsu7874さんが、技術力を駆使して彼女を作ってしまおうという（ネタ）企画です！  
Project KNJと命名されたこの企画では、twitterの過去のツイートを形態素解析(janome)し、マルコフ連鎖で短文生成(2-gram)、LINEアプリでおしゃべり(LINE Messaging API)させてしまおうという計画のもと進められました。  
一通り出来上がった後にKNJと対話を試みようとしましたが、意味不明の文章が帰ってきてしまい、まだまだ彼女をゲットするには程遠いという状況だったそうです。  
これにめげずに、頑張って理想のKNJを作り上げてくださいね！  

# クロージング
LTの熱気冷めやらぬ中、クロージングにも多くの方にご参加いただきました。  
翌日に開催されるスプリントの紹介やスプリントリーダーの挨拶に続き、座長の吉田から挨拶をさせていただきました。  
今回のPyCon JPではなんと690人以上の方にご参加いただいたそうです。  


そして今回初めて実施された「ベストトークアワード」。  
参加者から評判の良いトークを表彰したいという思いで今回企画されました。  
優秀賞はGraham Dumpletonさんの「[Secrets of a WSGI master](https://pycon.jp/2017/ja/schedule/presentation/9/)」、yuzutas0さんの「[SREエンジニアがJupyter＋BigQueryでデータ分析基盤をDev＆Opsする話](https://pycon.jp/2017/ja/schedule/presentation/38/)」、そして最優秀賞はGreg Priceさんの「[Clearer Code at Scale: Static Types at Zulip and Dropbox](https://pycon.jp/2017/ja/schedule/presentation/12/)」でした。  
残念ながら表彰式はyuzutas0さんのみとなりましたが、三者三様の興味深いトーク、ありがとうございました！  
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/pyconjp/36975518012/in/album-72157685754005651/" title="IMG_5009"><img src="https://farm5.staticflickr.com/4410/36975518012_dfec54c20b_o.jpg" width="640" height="427" alt="IMG_5009"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  

その後、今年のDiamondスポンサーであるSQUEEZEの関根氏や一般社団法人PyCon JP寺田氏の挨拶に加えて、恒例のプレゼントタイムということでビンゴ大会が執り行われました。  
Pythonカンファレンスらしくrandom関数で抽選をするという演出もありました。  
スポンサー企業の皆様、今年も素敵なプレゼントの数々ありがとうございました！  
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/pyconjp/36957969096/in/album-72157685754005651/" title="IMG_5057"><img src="https://farm5.staticflickr.com/4358/36957969096_341990cc49_o.jpg" width="640" height="427" alt="IMG_5057"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  

そして最後に来年のPyCon JPについてのお知らせが発表されました。  
来年のカンファレンスは2018/09/17,18に[大田区産業プラザPiO](http://www.pio-ota.net/)で実施されます。ぜひ皆様、来年もお越しくださいね！  

さて、「Output & Follow」をテーマに据えて実施された今年のPyCon JPでしたが、いかがでしたでしょうか？  
本連載でご紹介できた内容はPyCon JPのごくごく一部です。  
ネット上で今年のPyCon JPの振り返りブログが多く掲載されているので、是非是非皆様ご覧ください。  

それではまた来年お会いしましょう！  
