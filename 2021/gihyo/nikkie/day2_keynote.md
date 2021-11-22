# Day2 Keynote: A Perfect match (Mr. Brandt Bucher)

（nikkie）

この10月にリリースされたPython3.10。
その目玉機能といえば **パターンマッチ** ですね！
PyCon JP 2021 2日目のキーノートは、パターンマッチのPEPの筆頭著者のBrandtさんです。
パターンマッチについて

- history
- design
- implementation
- future

の4つのパートから共有していただきました。

まずhistoryでは、過去のSwitch文のPEPの紹介から始まり、「*パターンマッチはSwitchではない*」と強調されました。
私は十分にキャッチアップできていなかったので、「そうなのかな？」と思ったのですが、キーノートを聞き終わる頃には納得しました。

続くdesignでは、パターンマッチを構成する2つの要素について述べられます。

- 制御フロー（control flow）
- destructuring

キーノートで登場した例ですが、パターンマッチを使ったFizzBuzzのコードは制御フローがスッキリ書けていて衝撃的でした。

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
これはswitch文と大きく違うところと理解しました。

implementationでは、バイトコードの解説や、**soft keyword** による後方互換性について説明がありました。
``match match:`` のように書け、過去に書いたコードも修正不要というのは、パターンマッチを導入しやすそうですね。

futureによると、制御構造として冗長な動きやUnreachable checkを改善していくそうです。

[PEP 636のTutorial](https://www.python.org/dev/peps/pep-0636/)で素振りしたり、
[言語リファレンスのmatch文の項目](https://docs.python.org/ja/3/reference/compound_stmts.html#the-match-statement)を読んでみたりすると
パターンマッチに習熟できそうですね。
Python3.10でパターンマッチを使ったコードを書くのが楽しみになるキーノートでした！
