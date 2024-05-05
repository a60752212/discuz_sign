# 需要提前执行：(报错请用pip3 install xxxxxx)
# pip install requests
# pip install bs4

#--------------------------------------
#此处修改成你的配置
url='https://zodgame.xyz/plugin.php?id=dsu_paulsign:sign'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Connection": "keep-alive",
  "Cookie" : "qhMq_2132_saltkey=qTJZ8sAq; qhMq_2132_auth=2d0cI43kQj6xkLaVuZdHAVC1OTWVDBFhf1BVOiXUsbgJogb%2BES5LRUhANjB3pnhaagp2V9t0hr9HoBfn68cN2R3jnWM",
  "Host": "zodgame.xyz",
  "Referer": "https://zodgame.xyz/plugin.php?id=dsu_paulsign:sign"}
#以上请修改成自己的配置
#--------------------------------------

import re
import requests
from bs4 import BeautifulSoup
import html

#心情
form_data = {
    "formhash": "cb4f0a01",
    "qdxq": "kx",
    "todaysay": "￣︶￣",
}

#发送请求获取响应
r= requests.post(url, data=form_data, headers=headers)
r.encoding="UTF-8"
soup = BeautifulSoup(r.text, 'xml')
html_text = html.unescape(soup.text)
soup1 = BeautifulSoup(html_text, 'html.parser')

#寻找提示语句
div = soup1.find('div', class_='c')
text = div.get_text()

#输出
print(text)
