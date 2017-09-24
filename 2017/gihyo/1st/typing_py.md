# 1日目注目セッション「ベンリに使おう変数アノテーション - typing.pyとの楽しいお付き合い」 - Takumi Sueda

Takumi Sueda氏による変数アノテーションをテーマにしたセッションを紹介します。
Sueda氏はFuller, Inc.に所属するエンジニアで、普段はPythonやGo言語を扱っており、この講演はGo言語にあるUnmarshalerという機能を、アノテーションを利用してPythonへ移植してみるという内容のセッションでした。

まずPythonのアノテーションの背景として、[PEP 3107](https://www.python.org/dev/peps/pep-3107/)、[PEP 484](https://www.python.org/dev/peps/pep-0484/)、[PEP 526](https://www.python.org/dev/peps/pep-0526/)の紹介がなされた後、移植したい機能であるGo言語のUnmarchalerについての説明がありました。
Sueda氏曰く、これは「PythonのjsonライブラリよりPythonic」だと感じる機能のようで、本セッションのモチベーションはこの点にあったようです。

![写真: Unmarchalerについての説明をするSueda氏](./36964031691_8ffbc472d2_z.jpg)

そして、ここからは実際にPythonでbuiltin型、ジェネリック型、カスタムクラスを正しく区別し処理するunmarshalerを作成した過程をみていきます。

最初にアノテーションとして渡した情報が、ジェネリック型にどのように格納されているかを調べるところから始まりました。
まずはジェネリック型であるList[str]のmro()を呼び出し追っていきます。
すると、`typing.GenericMeta.__getitem__`が呼ばれ、そこからさらに自分自身のインスタンスを生成して返していました。
そしてその際に`self.__args__`へ渡された`str`を格納しています。
これはつまり、ジェネリック型の情報は__args__から取得できるということになります。

ちなみに筆者も手元で実際にやってみましたが、たしかに__args__で情報が取れていました！

```python
$ python3
Python 3.6.2 (default, Aug 11 2017, 16:57:55) 
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from typing import List
>>> List[str].__args__
(<class 'str'>,)
>>> from typing import Optional
>>> Optional[str].__args__
(<class 'str'>, <class 'NoneType'>)
```

そして、ここからさらにbuiltin型、ジェネリック型、カスタムクラスを正しく区別する処理が紹介されました。
判別の方法はbuiltin型かどうかを判定、builtin型でなければジェネリック型かどうかを判定、ジェネリック型でもなければカスタムクラスかどうかを判定するという流れで作成したようです。

ここまでの一連の流れの説明をもってセッションは終了しました。
実際に実装したコードは[puhitaku/typedmarshal](https://github.com/puhitaku/typedmarshal)リポジトリにあるとのことです。

そして、このセッションの動画は[こちら]()にあります。
非常に内容の濃いセッションだったため、セッション動画を見ながら実際に手元で動かしてみることをおすすめします！

## 参考

* [動画](https://www.youtube.com/watch?v=q0rxk5vSzVI)
* [スライド](https://speakerdeck.com/puhitaku/bian-li-nishi-oubian-shu-afalsetesiyon-typing-dot-py-tofalsele-siiofu-kihe-i)
