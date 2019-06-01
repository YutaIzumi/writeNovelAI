# -*- coding: utf-8 -*-
import glob
import MeCab
import numpy as np

# ディレクトリ内のすべてのテキストファイルを１つにまとめる
def make_corpus(file_dir):
    fileNames = glob.glob(file_dir)
    
    corpus = ""
    save_flag = False # コーパスへの追記をコントロールするフラグ
    count = 0         # ヘッダーの終わりを取得するためのカウンタ
    
    for name in fileNames:
        f = open(name, encoding="shift_jisx0213")
        
        # テキストを１行ずつ抽出
        for line in f:
            # フッターはコーパスに追記しない
            # フッターは'底本：'から始まる
            footer = line.find('底本：')
            if footer != -1:
                save_flag = False
                count = 0
            
            # テキストをコーパスに追記する
            if save_flag:
                corpus += line
            
            # ヘッダーはコーパスに追記しない
            # ヘッダーは'-------------------------------------------------------'で囲まれている
            idx = line.find('-------------------------------------------------------')
            if idx != -1:
                count += 1
                if count == 2:
                    save_flag = True
    
    # コーパスをテキストファイルとして保存する
    f = open('corpus.txt','w', encoding="shift_jisx0213")
    f.write(corpus)
    f.close()
    
    # MeCabでコーパスを分かち書きする
    m = MeCab.Tagger ("-Owakati")
    corpus = m.parse(corpus)
    corpus = corpus.split(' ')
    
    # word_to_id：単語からidに変換するためのディクショナリ
    # id_to_word：idから単語に変換するためのディクショナリ
    # idに変換済みのコーパス
    word_to_id = {}
    id_to_word = {}
    for word in corpus:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word    
    corpus = np.array([word_to_id[w] for w in corpus])

    return corpus, word_to_id, id_to_word

if __name__ == '__main__':
    make_corpus("./corpus/akutagawa/*")
    