#encoding=utf8
from pyecharts import WordCloud
from snownlp import SnowNLP
import jieba

##词云

filename = "wdqbs.txt"
with open(filename) as f:
 mytext = f.read()
#print mytext

s= SnowNLP(unicode(mytext,'utf8'))
for word in s.keywords(10):
    print word.encode('utf8')

seg_list = jieba.cut(mytext)

punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')
# 对str/unicode
filterpunt = lambda s: ''.join(filter(lambda x: x not in punct, s))
# 对list
filterpuntl = lambda l: list(filter(lambda x: x not in punct, l))

dict={}
for word in filterpuntl(seg_list):
    if word in dict:
        dict[word]=int(dict[word])+1
    else:
        dict[word]=1
name=[]
for word in dict.keys():
    name.append(word.encode('utf8'))
print name
value = dict.values()
print value
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.show_config()
wordcloud.render()
