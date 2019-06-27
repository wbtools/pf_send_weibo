from spider.tqs import TqsParse
spiders = [
    TqsParse(),  # 获取库里面的商品
]

currentIndex = 0
count = len(spiders)

def nextSpider():
    global currentIndex
    spider = spiders[currentIndex]
    currentIndex = (currentIndex + 1) % count
    return spider
