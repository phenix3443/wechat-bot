# -*-coding:utf-8 -*-
""" 微信聊天机器人简单的实现
"""
import os
import itchat
import requests

def main():
    itchat.auto_login()
    itchat.run()


if __name__ == '__main__':
    main()
