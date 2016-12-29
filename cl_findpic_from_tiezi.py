# -*- coding:utf-8 -*-

import urllib
import urllib2
import re




class findpic_from_tiezi:
    '把一个帖子里面的所有图片全部下载下来'
    def __init__(self):
        self.pic_list=[]
        self.num_page=0

    def get_html_str_from_url(self,url):
        '通过URL来获得html，返回一个字符串'
        try:
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError,e:
            print "获取html失败，原因",e.reason
            return None

    def findall_pic_from_html(self,html):
        '把此html中的所有图片链接放入list'
        content = html.decode('utf-8')
        pattern = re.compile('<img class="BDE_Image".*?src="(.*?.(jpg|png|gif))"', re.S)
        items = re.findall(pattern, content)
        self.pic_list=self.pic_list+items

    def down_pic_url_path(self, path,num):
        '把list中的图片下载到path中'
        i = 0;
        for pic in self.pic_list:
            try:
                urllib.urlretrieve(pic[0], path + "\%s." % i+pic[1])
                print str(num)+' downloading the ' +  str(i + 1) + ' pic'
            except BaseException:
                print "downloading error"
            i+=1

    def get_num_page(self,html):
        '通过html获得此贴有多少页'
        content = html.decode('utf-8')
        pattern = re.compile('</span>回复贴，共<span.*?>(.*?)</span>页</li>'.decode('utf-8'), re.S)
        items=re.findall(pattern,content)
        for item in items:
            self.num_page=int(item)
        if self.num_page>10:
            self.num_page=10

    def main(self,url,path,num):
        '主函数'
        self.pic_list=[]
        self.num_page=0
        html=self.get_html_str_from_url(url)
        self.get_num_page(html)
        i=0
        while i<self.num_page:
            html=self.get_html_str_from_url(url+'?pn='+str(i+1))
            self.findall_pic_from_html(html)
            i+=1
        self.down_pic_url_path(path,num)

