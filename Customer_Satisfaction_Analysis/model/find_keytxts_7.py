import os
def find_keytxts():
    file_path = 'key_emotion'
    try:
        os.mkdir(file_path)
        print(file_path+'文件夹已经建立，请查看当前文件路径')
    except Exception as e:
        print('文件夹已经存在，请查看当前程序路径')
    # 基于字典的查找
    key_words_list = [{'环境','周边','风景','空气','江景','小区','景点','夜景','街','周围','景区','声音','景色'},
                      {'价格','房价','性价比','价位','单价','价钱'},
                      {'特色','装潢','布置','建筑','结构','格调','装修','设计','风格','隔音'},
                      {'设施','设备','条件','硬件','房间','热水','马桶','电梯','阳台','卫生间','洗手间','空调','被子','床','大厅','电话','电','摆设'},
                      {'餐饮','早餐','咖啡','味道','饭','菜','水果','特产','餐','美食','烧烤','宵夜','食材','饭馆','小吃'},
                      {'交通','车程','地段','路程','停车','机场','离','车站','地理','位置','地理','中心','海拔','码头'},
                      {'服务','态度','前台','服务员','老板','掌柜','店家','工作人员'},
                      {'体验','整体','感觉'},]
    i = 0
    for key_words in key_words_list:
        find_keytxt(i,key_words)
        i += 1
def find_keytxt(number,key_words):
    key_list = {0: '环境',
                1: '价格',
                2: '特色',
                3: '设施',
                4: '餐饮',
                5: '交通',
                6: '服务',
                7: '体验',
                }
    f = open('key/pure_cut_final.txt','r',encoding='utf-8')
    key_txt = open('key_list/%s.txt'%key_list[number],'w',encoding='utf-8')
    for sentence in f:
        for i in key_words:
            if i in sentence:
               key_txt.write(sentence)
            else:continue
    f.close()
    key_txt.close()
    print(key_list[number]+'已经查找完成')
if __name__ == '__main__':
    find_keytxts()

