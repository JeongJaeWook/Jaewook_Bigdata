from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ""
with open("KaKaoTalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[4:]:
        if '] [' in line :
            text += line.split('] ')[2].replace('ㅋ','')\
                .replace('이모티콘\n','').replace('사진\n','').replace('삭제된 메시지입니다','')\
                .replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('지현','')\
                .replace('자기','').replace('웅웅','').replace('응응','') \
                .replace('근데', '').replace('그럼','').replace('내가','').replace('그래서','') \
                .replace('지금', '').replace('나는','')



#print(text[:10000])

wc = WordCloud(font_path="C:/WINDOWS/Fonts/Hancom Gothic Bold.ttf", background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")

# mask = np.array(Image.open('cloud.jpg'))
# wc = WordCloud(font_path="C:/WINDOWS/Fonts/Hancom Gothic Bold.ttf", background_color="black", mask=mask)
# wc.generate(text)
# wc.to_file("result_masked.png")
