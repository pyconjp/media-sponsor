# SREエンジニアがJupyter＋BigQueryでデータ分析基盤をDev＆Opsする話

|項目|詳細|
|-----|-----|
|公式ページ|https://pycon.jp/2017/ja/schedule/presentation/38/|
|発表スライド|https://speakerdeck.com/yuzutas0/20170909|
|まとめ|https://togetter.com/li/1148968|

株式会社リクルートテクノロジーズでグループのIT施策全般を担当されているyuzutas0さんの講演を紹介します。  
プロダクト開発におけるデータ活用の一事例として、組織が抱えていた問題、そしてそれを解決するための取り組みをお話くださいました。  
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/pyconjp/36998850801/in/album-72157685754005651/" title="IMG_9673"><img src="https://farm5.staticflickr.com/4416/36998850801_e8f881f64c_o.jpg" width="640" height="427" alt="IMG_9673"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  

yuzutas0さんが担当されているゼクシィ縁結びやゼクシィ恋結びでは事業が拡大しており、各部署にステークホルダーが多く存在していました。  
yuzutas0さんのチームではステークホルダーへ多種多様なデータを提供しており、それらのデータを活用するためにはデータ自動化・可視化が不可欠と感じていました。  
というのは、各部署によって必要なデータ、データ形式、データ疎通環境が異なるという混沌とした状況になっており、それに伴い調査コストなどのエンジニアチームの負荷が増加していたからです。  

そういった事情からデータ基盤システムを作ることになりましたが、設計にあたって2つのことを意識したそうです。  
一つ目は「ModelとViewを分ける」こと。
部署や職種によって必要とされるViewは異なります。  
Excel,Tableau,Re:dash,Jupyterなど、多様なViewに対応できるようにしています。  

```
<script async class="speakerdeck-embed" data-slide="56" data-id="d520b273412b44bbb1b503e5a3ce83d5" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>  
```

二つ目は「なるべくラクしてつくる」こと。  
世の中には便利なツールが多くあり、全て自分たちで作る必要はありません。  
アプリ層においては「Python」を採用しました。  
汎用的なプログラム処理を書くことができたり、データ分析関連のライブラリやツールが充実していたことがその理由です。  
また、インフラ（データ保存）に関してはBigQueryを採用しました。  
安い、早い、安心の三拍子揃ったシステムということで、インフラはGoogleに任せる判断をしたそうです。  

```
<script async class="speakerdeck-embed" data-slide="68" data-id="d520b273412b44bbb1b503e5a3ce83d5" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>  
```

そのほかにもデータフローを回す上での工夫や、開発プロセスをトライアンドエラーで整備していったお話など、参考になる知見がたくさんありました。  

そして最後に、データ文化を組織に定着させることの重要性を主張しました。  
今までは、各ステークホルダーが協力することができず、データ活用が十分にできない状況にありました。  
（例えばビジネス側では各種データをExcelで扱っていたため、エンジニアからは手を出しづらかった、など）  
その状況を「テクノロジー」と「文化・プロセス」で解決しようとしたのが今回ご紹介してきた取り組みです。  

```
<script async class="speakerdeck-embed" data-slide="129" data-id="d520b273412b44bbb1b503e5a3ce83d5" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>  
```

現状ではまだ理想状態にはないということで、今後も試行錯誤して「データ活用がされる組織」を目指したいということでした。  

ちなみに詳細は後述しますが、このyuzutas0さんの講演は、PyCon JP 2017の「ベストトークアワード」の優秀賞に見事輝きました！  
組織におけるデータ活用やその運用方法について、やはりみなさん興味を持たれているのだなと実感する投票結果となりました。  
