def first_delete_spaces():
    #分词+去除空行
    #词性标注集http://ltp.readthedocs.io/zh_CN/latest/appendix.html
    # cont = open('key/pinglun_resource.txt','r',encoding='utf-8')
    cont = open('resource.txt','r',encoding='utf-8')
    f = open('resource_new.txt','w',encoding='utf-8')
    for sentence in cont:
        if sentence.strip() != '':
            f.write(sentence)
        else:continue
    f.close()
    print('源评论去除空格完成')
if __name__ == '__main__':
    first_delete_spaces()