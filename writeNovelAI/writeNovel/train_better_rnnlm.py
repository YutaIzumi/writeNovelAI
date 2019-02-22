# coding: utf-8
import sys
sys.path.append('..')
from common import config
# GPUで実行する場合は下記のコメントアウトを消去（要cupy）
# ==============================================
config.GPU = True
# ==============================================
from common.optimizer import SGD
from common.trainer import RnnlmTrainer
from common.util import eval_perplexity, to_gpu
from better_rnnlm import BetterRnnlm
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
# file_dir = "./kafuka/*"
# file_dir = "./dazai/*"
# file_dir = "./dazai_mini/*"
# file_dir = "./yoshikawa_mini/*"
# file_dir = "./dowa/*"
file_dir = "./dowa_devil/*"
corpus, word_to_id, id_to_word = mc.make_corpus(file_dir)
print(len(word_to_id))
corpus_val = corpus
corpus_test = corpus

if config.GPU:
    corpus = to_gpu(corpus)
    corpus_val = to_gpu(corpus_val)
    corpus_test = to_gpu(corpus_test)

vocab_size = len(word_to_id)
xs = corpus[:-1]
ts = corpus[1:]

model = BetterRnnlm(vocab_size, wordvec_size, hidden_size, dropout)
optimizer = SGD(lr)
trainer = RnnlmTrainer(model, optimizer)

best_ppl = float('inf')
for epoch in range(max_epoch):
    trainer.fit(xs, ts, max_epoch=1, batch_size=batch_size,
                time_size=time_size, max_grad=max_grad)

    model.reset_state()
    ppl = eval_perplexity(model, corpus_val)
    print('valid perplexity: ', ppl)

    if best_ppl > ppl:
        best_ppl = ppl
        model.save_params()
    else:
        lr /= 4.0
        optimizer.lr = lr

    model.reset_state()
    print('-' * 50)


# テストデータでの評価
model.reset_state()
ppl_test = eval_perplexity(model, corpus_test)
print('test perplexity: ', ppl_test)
