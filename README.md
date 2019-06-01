# writeNovelAI

RNNを使った文章生成プログラムです。

試しに芥川龍之介の小説を学習させて、出てきた結果がこちらです。

```厳然たる と 所 の 中 に この 心もち が 「 八 命 の 遠い 柳 を 油断 の し ど 易い 否 へ は いどま せ た の う と を 恐れ た もの を 考へ て い た 方 で 事実 で ござい ます 。```

意味不明ですｗｗｗ

文法的には間違ってない部分もあるんですけど。。。

学習データやハイパーパラメータに改善の余地がありそうですが、手持ちのノートPCではこれが限界でした。

## 実行環境

#### Windows10

#### Python3.7 Anaconda

https://www.anaconda.com/distribution/

#### Mecab

形態要素解析にMeCabを使用します。MeCabをインストールしてください。

MeCabについては以下を参考にして下さい。

https://taku910.github.io/mecab/

MeCabのインストールは以下が参考になると思います。

https://qiita.com/menon/items/f041b7c46543f38f78f7

## 使い方 

### １．コーパスの指定

```writeNovelAI/writeNovelAI/writeNovel/corpus/```に学習させたい文章を保存します。

### ２．コーパスの学習

```writeNovelAI/writeNovelAI/writeNovel/train_better_rnnlm.py```を実行します。

実行前に25行目にてコーパスを保存した場所を書き換えて下さい。

（例）```file_dir = "./corpus/akutagawa/*"```

学習が終わると、学習済みの重み```BetterRnnlm.pkl```が保存されます。

### ３．文章の作成

```writeNovelAI/writeNovelAI/writeNovel/generate_better_text.py```を実行します。

実行前にコーパスと学習済みの重みを保存した場所を書き換えて下さい。

コーパス　17行目
（例）```file_dir = "./corpus/akutagawa/*"```

学習済みの重み　27行目
（例）```model.load_params('./params/BetterRnnlm_akutagawa.pkl')```

## 参考文献

https://www.atmarkit.co.jp/ait/articles/1804/25/news143.html

https://www.oreilly.co.jp/books/9784873118369/
