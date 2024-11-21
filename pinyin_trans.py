# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

from utils.PyTire import PyTrie


pyt = PyTrie()
pyt.setup()
dagparams = DefaultDagParams()

def pinyin2word(pinyin_str: str):
    """
    将拼音字符串转换成中文词语列表，基于拼音切分和dag算法

    Args:
        pinyin_str (str): 拼音字符串

    Returns:
        List[str]: 中文词语列表

    """

    words = pyt.scan(pinyin_str)
    pinyin_list = tuple(words)
    result = dag(dagparams, pinyin_list, path_num=1, log=True)

    if len(result) < 1:
        return []

    res_word = "".join(result[0].path)

    return res_word


if __name__ == "__main__":
    res = pinyin2word("chengxuyuan")
    print(res)  # 程序员
