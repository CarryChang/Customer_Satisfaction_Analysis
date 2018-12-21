import os
def delete_spaces():
    file_path = 'key_list'
    try:
        os.mkdir(file_path)
        print(file_path+'文件夹已经建立，请查看当前文件路径')
    except Exception as e:
        print('文件夹已经存在，请查看当前程序路径')
    #分词+去除空行
    #词性标注集http://ltp.readthedocs.io/zh_CN/latest/appendix.html
    # cont = open('key/pinglun_resource.txt','r',encoding='utf-8')
    cont = open('key/cut_resouce.txt','r',encoding='utf-8')
    f = open('key/pure_cut_final.txt','w',encoding='utf-8')
    for sentence in cont:
        if sentence.strip() != '':
            f.write(sentence)
        else:continue
    f.close()
if __name__ == '__main__':
    delete_spaces()
    print('delete_spaces 完成')