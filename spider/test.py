import os

# for test
import sys
sys.path.insert(0, '..')

from tqs import TqsParse

if __name__ == '__main__':
    types = [
       TqsParse
    ]
    for c in types:
        print(os.linesep + '************* ' + str(c) + ' start *************')
        try:
            p = c()
            for i in range(1):
                weibo = p.get_weibo_message()
                print(weibo)
                # print('has image: ' + str(weibo.has_image))
                # print(str(c) + 'text success!')
        except Exception as e:
            print(e)
            print(str(c) + ' failure!')

        print('************* ' + str(c) + ' end *************' + os.linesep)
