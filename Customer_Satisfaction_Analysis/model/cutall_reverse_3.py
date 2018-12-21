def cutall_reverse():
    word_df = []
    #统计词频的字典
    word_count = {}
    for line in open('key/cut_all.txt','r',encoding='utf-8'):
        words = line.strip().split(" ")
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    for word in word_count.keys():
        if word:
            word_df.append([word, str(word_count.get(word))])
        else:continue
    with open("key/cut_all_reverse.txt", 'w',encoding='utf-8') as wf2:
        word_df.sort(key=lambda x: int(x[1]),reverse=True)
        wf2.truncate()
        for item in word_df:
            for word in item:
                wf2.write(word + ' ')
            wf2.write('\n')
        print('全分词字典倒序排序已经成功 ')
    wf2.close()
if __name__ == '__main__':
    cutall_reverse()
