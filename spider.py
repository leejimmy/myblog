import  re
content = '<br/></p><p><br/></p><p><img src="/media/uploads/images/dapengsuocheng_2_20161127052608_936.jpg" alt="dapengsuocheng_2.jpg" style="width: 265px; height: 367px; float: left;" width="265" height="367"/><img src="/media/uploads/images/dapengsuocheng_1_20161127054614_480.jpg" alt="dapengsuocheng_1.jpg" style="width: 266px; height: 367px;" width="266" height="367"/></p>'
p = re.findall('src="(.*?)" alt.*',content)
print p[0]