# -*- coding: utf-8 -*- 
from scrapy.spider import Spider
from scrapy.selector import Selector
import re
import thread
import urllib2

import os
#读取要爬的URL
def read_urls(filename):
    lst=[]
    f=open(filename)
    while True:
        line=f.readline()
        if not line:
            break
        line=line.split('html')[0]+'html'
        lst.append(line)
    f.close()
    return lst
#下载图片
def downloadimg(url,out_put_path):
    socket=urllib2.urlopen(url)
    data=socket.read()
    with open(out_put_path,'wb') as jpg:
        jpg.write(data)
    socket.close()
#主爬虫
class TwxshSpider4NewsText(Spider):
    name="twxshspider4newstext"
    allowed_domains=["http://eic.jnu.edu.cn/"]
    start_urls=read_urls('newsurl.txt')

    def parse(self,response):
        #新建各种文件和文件夹
        new_dir_name=response.url.split('/')[-1].split('.html')[0]
        
        cur_path='newstext\\'
        new_path=os.path.join(cur_path,new_dir_name)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
        #新建图片文件夹,用于储存图片
        img_path=os.path.join(new_path,'images')
        os.makedirs(img_path)

        filename=cur_path+new_dir_name+"\\"+new_dir_name+'.txt'
        imgsrcs=cur_path+new_dir_name+"\\"+'src.txt'
       
        sel=Selector(response)
       
        #处理标题
        title=sel.xpath('body/table[3]/tr[2]/td[1]/table[1]/tr[1]/td[1]/text()').extract()[-1].strip()
        #处理日期
        s="来源：添加时间：".decode('utf-8')
        date=sel.xpath('body/table[3]/tr[2]/td[1]/table[1]/tr[3]/td[1]/text()').extract()[0].decode('utf-8').replace(s,"")
        #处理正文
        content=sel.xpath('body/table[3]/tr[2]/td[1]/table[1]/tr[5]/td[1]/*')
        #摘取图片链接
        srcs=content.css("img[src]")
        ff=open(filename,'wb')
        fi=open(imgsrcs,'wb')
       
        #写入文件
        for src in srcs:
            img_sel=Selector(text=src.extract(),type="html")
            imgurl="http://eic.jnu.edu.cn"+img_sel.xpath("//@src").extract()[0]
            fi.write(imgurl+'\r\n')
            try:
                out_put_path=img_path+'\\'+imgurl.split('/')[-1]
                thread.start_new_thread(downloadimg,(imgurl,out_put_path))
            except:
                pass
            
        fi.close()

        ff.write("title: "+title+'\r\n')
        ff.write("date: "+date+'\r\n')
        ff.write("content: \r\n")
        for text in content:
            ff.write(text.extract())
        
        ff.write('\r\n')
        ff.close()
       
