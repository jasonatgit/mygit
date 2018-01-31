import re

data = '''【警情概况】
上周（2017.12.18-2017.12.24），\
市公安局110报警服务台共接各类报警、求助、咨询及滋扰电话等99525个，\
较前一周（2017.12.11-2017.12.17）上升0.6%，\
其中刑事、治安、交通和消防类占33.8%，投诉类占0.2%，\
举报类占3.3%，社会联动类占1.8%，求助咨询类占17.2%，\
其他报警类占22.3%，无效报警类占21.4%。\
上周，全市刑事类1110宗，较前一周上升1.6%，\
治安类3231宗，较前一周下降2.8%。\
涉骗类共接报1263宗，\
较前一周下降0.2%，\
其中网络诈骗260宗，较前一周下降5.1%，\
手机短信诈骗162宗，较前一周上升52.8%，\
其他诈骗类841宗，较前一周下降5.0%。'''

def text_spliter(text_data):
    #文本中无关信息处理
    txt0 = re.sub('），|）',('，'),text_data)
    txt1 = re.sub('【警情概况】|个|宗|其中|其他|公安局110|（|）',(''),txt0, flags=re.IGNORECASE)
    txt2 = re.sub('，|。',('\n'), txt1, flags=re.IGNORECASE)
    txt3 = txt2.strip('\n')
    txt4 = txt3.split('\n')


    for txt in txt4:
    #文本清洗，切分文字与日期/数字串
        new_txt = re.split(r'(\d+\.\d\%)|(\d*\.\d*\.\d*\-\d*\.\d*\.\d*)|(\d+)',txt)
        #print(new_txt)
        while '' in new_txt:#删除列表中空元素
            new_txt.remove('')
            #print(new_txt)
        #把文字与数字按照对应关系建立键值
        for i in new_txt:
            if new_txt.index(i) == 0:
                key_text = '键：%s'%i
            elif i is not None:
                value_text = '值：%s'%i
        print(key_text+','+value_text)

text_spliter(data)


