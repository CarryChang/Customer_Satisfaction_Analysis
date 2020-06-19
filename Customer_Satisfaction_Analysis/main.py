import time
from cut_words_1 import cut_sentence
from find_topic_txts_2 import find_topic_txts
from topic_sa_analysis_3 import topic_sa_analysis
if __name__ == '__main__':
    st = time.time()
    cut_sentence()
    find_topic_txts()
    topic_sa_analysis()
    print('总用时间为 {} (单位s)'.format(time.time()-st))