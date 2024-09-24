
import lxml.html


html = '''
</html>
<body>
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
    <div id="useless">这是我不需要的内容</div>
</body>
</html>
'''

selector = lxml.html.fromstring(html)
context = selector.xpath('//div[starts-with(@id,"test")]/text()')
context1 = selector.xpath('//div[@id="useless"]/text()')
print(context)
print(context1)
