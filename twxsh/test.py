from scrapy import Selector
doc = """
    <div>
         <ul>
             <li id="id" class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
     </div>
    """
sel = Selector(text=doc, type="html")
#print(sel.xpath('//li//@href').extract())
print(sel.xpath('//div/*').extract())
print(sel.css('#id').extract())
#print(sel.xpath('//li[re:test(@class, "item-\d$")]//@href').extract())
