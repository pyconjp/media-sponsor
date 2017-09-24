# Pythonの本気！RaspberryPiやEdisonを使ったIoTシステムの構築

|項目|詳細|
|-----|-----|
|公式ページ|https://pycon.jp/2017/ja/schedule/presentation/32/|
|発表スライド|https://www.slideshare.net/yutakitagami/pycon-jp-2017yuta-kitagami/1|
|まとめ|https://togetter.com/li/1148920|

みなさん興味津々のIoTネタということで、北神雄太さんによる講演をご紹介します。  
北神さんは高校時代からハードウェアに手を出し、現在はハードウェアとソフトウェアの両方の知識を生かしご活躍されています。  
最近は[Intel Edisonマスターブック](http://gihyo.jp/book/2017/978-4-7741-8921-5)という本を出版されました。  

北神さんがIoTに精通しているということで、おそらく会場の皆さんは「IoTでこんなことができました」系のトークを期待されていたと思います。  
しかし北神さんは「できました系の話はつまらない。私はなぜそれができたかの話をします」というかっこいい発言で会場を沸かせていました。  
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/pyconjp/36303044513/in/album-72157685754005651/" title="IMG_9558"><img src="https://farm5.staticflickr.com/4441/36303044513_8417bd2950_o.jpg" width="640" height="427" alt="IMG_9558"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  

「IoT時代においてPythonは最強」という主張をした北神さん。  
Pythonはハードウェアが扱えるということがその理由だそうです。  

ではなぜPythonはハードウェアが扱えるのか？  
Pythonにはハードウェアのライブラリがあるというのがその理由ですが、そのライブラリはC言語のラッパーとして作成されています。  
C言語では例えばレジスタへアクセスできるため、GPIOなどのハードウェアを動かすという芸当ができるということなのです。  

そうなると、IoT領域においては低レイヤーのC言語がベストなのではという疑問が当然出てきます。  
それに対して北神さんは、「そんなC言語をラップできるPythonこそ最強」と答えます。  
つまり、低レイヤーにアクセスできるC言語に、多様なライブラリを要するPythonが合わさることで、実に様々なことが実現できるのです。  
例えば温湿度センサーの機能を使ってデータを取得しそれをDBに格納、サーバでデータを表示、そしてネットワークにも繋げるということも可能です。  

```
<iframe src="//www.slideshare.net/slideshow/embed_code/key/noOWzVT0B9dlgZ?startSlide=26" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/yutakitagami/pycon-jp-2017yuta-kitagami" title="PyCon JP 2017Yuta Kitagami" target="_blank">PyCon JP 2017Yuta Kitagami</a> </strong> from <strong><a href="//www.slideshare.net/yutakitagami" target="_blank">Yuta Kitagami</a></strong> </div>  
```

トークでは、北神さん自作の自宅の温湿度モニタリングシステムを披露していました。  

軽快なトークで会場を沸かせた北神さん。  
講演の時間だけでは足りず、終了後も場所を変えて参加者とIoT話に花を咲かせていたようです。  
<a data-flickr-embed="true"  href="https://www.flickr.com/photos/pyconjp/36310774094/in/album-72157685754005651/" title="IMG_4900"><img src="https://farm5.staticflickr.com/4394/36310774094_877884cba7_o.jpg" width="640" height="472" alt="IMG_4900"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>  
