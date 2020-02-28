# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
import pyperclip
import base64

class Main(Wox):

    def query(self, keyword):
        encode = str(base64.b64encode(keyword.encode('utf-8')),'utf-8')
        results = list()
        results.append({
            "Title": "encode",
            "SubTitle": encode,
            "IcoPath": "Images/base64.ico",
            "JsonRPCAction": {
                "method": "test_func",
                "parameters": [encode],
                "dontHideAfterAction": False
            }
        })
        decode = str(base64.b64decode(keyword.encode('utf-8')),'utf-8')
        results.append({
            "Title": "decode",
            "SubTitle": decode,
            "IcoPath": "Images/base64.ico",
            "JsonRPCAction": {
                "method": "test_func",
                "parameters": [decode],
                "dontHideAfterAction": False
            }
        })
        return results

    def test_func(self, keyword):
        pyperclip.copy(keyword)


if __name__ == "__main__":
    Main()
