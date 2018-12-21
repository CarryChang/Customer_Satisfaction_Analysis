import time
from model.first_delete_spaces_1 import first_delete_spaces
from model.first_cut_2 import first_cut
from model.cutall_reverse_3 import cutall_reverse
from model.n_reverse_4 import n_reverse
from model.cut_words_5 import cut_words
from model.delete_spaces_6 import delete_spaces
from model.find_keytxts_7 import find_keytxts
from model.snow_analysis_8 import snow_analysis
# from model.fina_analysis_9 import fina_analysis
if __name__ == '__main__':
    start_time = time.clock()
    first_delete_spaces()
    first_cut()
    cutall_reverse()
    n_reverse()
    cut_words()
    delete_spaces()
    find_keytxts()
    snow_analysis()
    # fina_analysis()
    end_time = time.clock()
    T1 = end_time-start_time
    print('总用时间为(单位s)：%s'%T1)