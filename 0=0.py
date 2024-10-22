import requests
url="https://api.bilibili.com/x/web-interface/wbi/search/type?category_id=&search_type=video&ad_resource=5654&__refresh__=true&_extra=&context=&page=4&page_size=42&pubtime_begin_s=0&pubtime_end_s=0&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E7%94%9C%E5%A6%B9&qv_id=kvbG83fbqq4uKpWKsN14yx9xHBZy4yvU&source_tag=3&gaia_vtoken=&dynamic_offset=90&web_location=1430654&w_rid=a1b9b32d5180ea76075ba7b4d30f8409&wts=1729595934"


header='user-agent:''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
response=requests.get(url,header)
data=response.json()['data']['result']

for info in data:
    id=info['id']
    play=info['play']

with open('b站.csv','a+')as f:
    f.write('{},{}\n'.format(id,play))

