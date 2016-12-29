# coding:utf-8

import urllib
import urllib2
import re
import cl_findpic_from_tiezi
import os




class cl_findall_tiezi_from_page:
    '从贴吧获得所有帖子的网址'

    def __init__(self):
        self.tie_url_name_list=[]
        self.num_page=0

    def get_html_str_from_url(self, url):
        '通过URL来获得html，返回一个字符串'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    def get_tieziurl_name_from_html(self,html):
        '通过html获得帖子的URL和名字'
        content = html.decode('utf-8')
        pattern = re.compile('<a href="/p/(.{10})" title=".*?" target="_blank" class="j_th_tit ">(.*?)</a>', re.S)
        items = re.findall(pattern, content)
        self.tie_url_name_list+=items

    def main(self,name,num,path):
        tiezi=cl_findpic_from_tiezi.findpic_from_tiezi()
        i=0
        while i<num:
            html=self.get_html_str_from_url('http://tieba.baidu.com/f?kw='+name+'&ie=utf-8&pn='+str(i*50))
            self.get_tieziurl_name_from_html(html)
            i+=1
        i=0
        for url_name in self.tie_url_name_list:
            if(url_name[1] not in os.listdir(path)):
                os.mkdir(path+'/'+url_name[1])
            tiezi.main('http://tieba.baidu.com/p/'+url_name[0],path+'/'+url_name[1],i+1)
            i+=1

