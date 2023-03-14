# line-height:29px
# text-indent:32px
# font-size:16px;font-family:宋体
# '[\u4e00-\u9fa5]+'多个中文字符
# \d+ 多个数字
import re

content_0 = 'line-height:100px'
content_1 = 'text-indent:100px'
content_2 = "letter-spacing: 0;font-size: 21px;background: rgb(255, 255, 255)font-size: 21px;"
content_3 = 'font-family:哈哈体'
regex_0=re.compile("line-height:"+'(\d+)'+"px") # 修改行间距为 29px
regex_1=re.compile("text-indent:"+'(\d+)'+"px") # 修改首行缩进为 32px
regex_2=re.compile("font-size:"+'[ ]*(\d+)'+"px") # 修改字体大小为 16px
regex_3=re.compile("font-family:"+'[\u4e00-\u9fa5]+') # 修改字体为 宋体
new_content_0 = re.sub(regex_0,'line-height:29px',content_0)
new_content_1 = re.sub(regex_1,'text-indent:32px',content_1)
new_content_2 = re.sub(regex_2,'font-size:16px',content_2)
new_content_3 = re.sub(regex_3,'font-family:宋体',content_3)

print(new_content_0+" "+new_content_1+" "+new_content_2+" "+new_content_3)
# name = regex.sub('29', name)
"""
<span style="font-family: 宋体;letter-spacing: 0;
font-size: 21px;background: rgb(255, 255, 255)">
<span style="font-family:哈哈">　　（一）放宽科研项目申报有关条件。</span></span>
"""

