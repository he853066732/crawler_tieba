# -*- coding:utf-8 -*-

'''从贴吧下载图片，还有一些编码上的bug，以后再说'''

import cl_findall_tiezi_from_page
import os

f=cl_findall_tiezi_from_page.cl_findall_tiezi_from_page()
tieba_name=raw_input(u'please input the name of tieba:')
num_page=int(raw_input(u'input num of page:'))
path=raw_input(u'input the path:')



f.main(tieba_name,num_page,path)
