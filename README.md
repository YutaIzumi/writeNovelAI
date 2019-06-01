# writeNovelAI

RNNを使った文章生成プログラムです。

試しに芥川龍之介の小説を学習させて、出てきた結果がこちらです。

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
