#!/bin/python

ignor_list = ['"', ',', "?", ".", ":", ")", "("]
def get_num():
    counter = 0
    try:
        fh = open("./soc-camera.txt", 'r')
        txt = fh.read()
        for x in ignor_list:
            txt = txt.replace(x, " ")
        for num in txt.split(" "):
            counter += 1
        print counter
        print txt
    except IOError :
        print "file not exite"
    finally:
        fh.close()
if __name__ == '__main__':
    get_num()
    pass





























