# coding: utf-8
from rnnlm_gen import BetterRnnlmGen
import make_corpus as mc

# ハイパーパラメータの設定
batch_size = 20
wordvec_size = 100
hidden_size = 100
time_size = 30
lr = 20.0
max_epoch = 5
max_grad = 0.25
dropout = 0.5

# コーパスの読み込み
file_dir = "./corpus/akutagawa/*"
# file_dir = "./corpus/kafuka/*"
# file_dir = "./corpus/dazai/*"
corpus, word_to_id, id_to_word = mc.make_corpus(file_dir)

vocab_size = len(word_to_id)
corpus_size = len(corpus)

model = BetterRnnlmGen(vocab_size, wordvec_size, hidden_size, dropout)
model.load_params('./params/BetterRnnlm_akutagawa.pkl') # 学習済みのパラメータを指定する

# start文字とskip文字の設定
start_word = '私'
start_id = word_to_id[start_word]
skip_ids = []

# 文章生成
word_ids = model.generate(start_id, skip_ids, sample_size=300)
txt = ' '.join([id_to_word[i] for i in word_ids])
txt = txt.replace(' <eos>', '.\n')

print(txt)
