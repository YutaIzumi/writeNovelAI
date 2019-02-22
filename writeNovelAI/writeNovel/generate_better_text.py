# coding: utf-8
import sys
sys.path.append('..')
from rnnlm_gen import BetterRnnlmGen
import make_corpus as mc

# ハイパーパラメータの設定
batch_size = 20
wordvec_size = 450
hidden_size = 450
time_size = 30
lr = 20.0
max_epoch = 60
max_grad = 0.25
dropout = 0.5

# 学習データの読み込み
# file_dir = "./akutagawa/*"
file_dir = "./kafuka/*"
# file_dir = "./dazai/*"
# file_dir = "./dazai_mini/*"
# file_dir = "./yoshikawa_mini/*"
# file_dir = "./dowa/*"
# file_dir = "./dowa_devil/*"
corpus, word_to_id, id_to_word = mc.make_corpus(file_dir)

vocab_size = len(word_to_id)
corpus_size = len(corpus)

model = BetterRnnlmGen(vocab_size, wordvec_size, hidden_size, dropout)
model.load_params('BetterRnnlm_kafuka.pkl')

# start文字とskip文字の設定
start_word = '私'
start_id = word_to_id[start_word]
skip_ids = []

# 文章生成
word_ids = model.generate(start_id, skip_ids, sample_size=300)
txt = ' '.join([id_to_word[i] for i in word_ids])
txt = txt.replace(' <eos>', '.\n')

print(txt)
