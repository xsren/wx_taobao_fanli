# encoding: utf-8
"""
@author: xsren 
@contact: bestrenxs@gmail.com
@site: xsren.me

@version: 1.0
@license: Apache Licence
@file: main.py
@time: 2017/5/29 上午10:11

"""

from lib import

def run():
    app = Application()
    # 设置窗口标题:
    app.master.title('Hello World')
    # 主消息循环:
    app.mainloop()


if __name__ == '__main__':
    run()