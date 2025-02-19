# -*- coding: utf-8 -*-
"""ptt_food_jieba.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZwK-F3wcOArfrlVGf9fxu3e6nj0Vk1QZ
"""

!pip install snownlp

"""# 1.将csv文件中的文本逐行取出，存新的txt文件"""

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/ptt_food/ptt_food.csv', encoding='utf-8')
# print(df.head())

for text in df['body']:
    # print(text)
    if text is not None:
        with open('/content/drive/MyDrive/ptt_food/ptt_body.txt', mode='a', encoding='utf-8') as file:
            file.write(str(text))

print('寫入完成')

"""2.使用停用词获取最后的文本内容"""

import jieba

jieba.load_userdict('/content/drive/MyDrive/ptt_food/user_dict.txt')
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 對句子進行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('/content/drive/MyDrive/ptt_food/stop_words.txt')  # 停用詞的路徑
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

inputs = open('/content/drive/MyDrive/ptt_food/ptt_body.txt', 'r', encoding='utf-8')
outputs = open('/content/drive/MyDrive/ptt_food/ptt_body_outputs.txt', 'w', encoding='utf-8')
for line in inputs:
    line_seg = seg_sentence(line)  # 這裡的返回值是字符串
    print(line_seg)
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()

"""3.1 jieba 分詞其他應用 - 關鍵詞提取"""

import jieba.analyse
content = open('/content/drive/MyDrive/ptt_food/ptt_body_outputs.txt', 'r', encoding='utf-8')
keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=())
# 訪問提取結果
for item in keywords:
    # 分別爲關鍵詞和相應的權重
    print(item[0], item[1])

# 同樣是四個參數，但allowPOS默認爲('ns', 'n', 'vn', 'v')
# 即僅提取地名、名詞、動名詞、動詞
# keywords = jieba.analyse.textrank(content, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
# # 訪問提取結果
# for item in keywords:
#     # 分別爲關鍵詞和相應的權重
#     print(item[0], item[1])

"""3.制作词云图"""

from wordcloud import WordCloud
import jieba
import numpy
import PIL.Image as Image

def cut(text):
    wordlist_jieba=jieba.cut(text)
    space_wordlist=" ".join(wordlist_jieba)
    return space_wordlist
with open(r"/content/drive/MyDrive/ptt_food/ptt_body.txt" ,encoding="utf-8")as file:
    text=file.read()
    text=cut(text)
    mask_pic=numpy.array(Image.open(r"/content/drive/MyDrive/ptt_food/Taiwan.jpg"))
    wordcloud = WordCloud(font_path=r"/content/drive/MyDrive/ptt_food/微軟正黑體-1.ttf",
    collocations=False,
    max_words= 100,
    min_font_size=10, 
    max_font_size=500,
    mask=mask_pic).generate(text)
    image=wordcloud.to_image()
    # image.show()
    wordcloud.to_file('/content/drive/MyDrive/ptt_food/词云图.png')  # 把词云保存下来

"""4.分词统计"""

import sys
import jieba
import jieba.analyse
import json  # 把詞頻字典 json.dumps() 存成 json 以便下次用 json.loads() 讀取
import xlwt  # 寫入Excel表的库

# reload(sys)
# sys.setdefaultencoding('utf-8')

if __name__ == "__main__":

    wbk = xlwt.Workbook(encoding='ascii')
    sheet = wbk.add_sheet("wordCount")  # Excel单元格名字
    word_lst = []
    key_list = []
    for line in open('/content/drive/MyDrive/ptt_food/ptt_body.txt', encoding='utf-8'):  # 需要分词统计的原始目标文档

        item = line.strip('\n\r').split('\t')  # 制表格切分
        print(item)
        tags = jieba.analyse.extract_tags(item[0])  # jieba分词
        for t in tags:
            word_lst.append(t)

    word_dict = {}
    with open("分词结果.txt", 'w') as wf2:  # 指定生成文件的名称

        for item in word_lst:
            if item not in word_dict:  # 统计數量
                word_dict[item] = 1
            else:
                word_dict[item] += 1

        orderList = list(word_dict.values())
        orderList.sort(reverse=True)
        # print orderList
        for i in range(len(orderList)):
            for key in word_dict:
                if word_dict[key] == orderList[i]:
                    wf2.write(key + ' ' + str(word_dict[key]) + '\n')  # 寫入txt文檔
                    key_list.append(key)
                    word_dict[key] = 0
    with open('word_dict.json', 'w') as fp:
        json.dump(word_dict, fp)
        
    for i in range(len(key_list)):
        sheet.write(i, 1, label=orderList[i])
        sheet.write(i, 0, label=key_list[i])
    wbk.save('/content/drive/MyDrive/ptt_food/wordCount_all_bodies.xls')  # 保存為 wordCount.xls文件

"""5.情感分析的统计值"""

from snownlp import SnowNLP

# 積極/消極
# print(s.sentiments)  # 0.9769551298267365  positive的概率


def get_word():
    with open("/content/drive/MyDrive/ptt_food/ptt_body.txt", encoding='utf-8') as f:
        line = f.readline()
        print(line)
        word_list = []
        while line:
            line = f.readline()
            word_list.append(line.strip('\r\n'))
        f.close()
        return word_list


def get_sentiment(word):
    text = u'{}'.format(word)
    try:
        s = SnowNLP(text)
        print(s.sentiments)
    except ZeroDivisionError:
        print(word, ' = ZeroDivisionError')


if __name__ == '__main__':
    words = get_word()
    for word in words:
        get_sentiment(word)

