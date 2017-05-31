# encoding: utf-8
"""
@author: xsren 
@contact: bestrenxs@gmail.com
@site: xsren.me

@version: 1.0
@license: Apache Licence
@file: test_itchat.py
@time: 2017/5/31 下午5:38

"""
import threading

import itchat


class MyItchat:
    @itchat.msg_register(itchat.content.TEXT)
    def text_reply(msg):
        print msg.text

    def run(self):
        itchat.auto_login()
        itchat.run()


if __name__ == '__main__':
    mi = MyItchat()
    t = threading.Thread(target=mi.run, args=())
    t.start()
