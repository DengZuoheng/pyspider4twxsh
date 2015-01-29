这是一个爬暨大电气院学生会旧网站(简称"旧站")的文章的爬虫

**旧站地址**: http://eic.jnu.edu.cn/twxsh/  
(应该是红色风格, 如果不是, 说明更新了)

**编程纪要**: http://dengzuoheng.github.io/a-scrapy-for-twxsh/

**仓库结构**:
爬虫是先抓文章地址, 然后再抓文章内容, 所以先会产生几个文件存放地址:

./twxsh/xxxurl.txt

这类文件就是存放地址的文件.

抓下来的内容是`./xxxtext/`这类文件夹

爬虫代码位于`./twxsh/twxsh/spiders/`

这个仓库只是用于保存代码和抓下来的数据的, 估计不会更新了.