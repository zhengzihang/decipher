#! /usr/bin/env python
# coding=utf8

from collections import Counter

def decrypt():
    #明文字符串
    plain = ""
    #存放可能的密钥，三个小写字母，对应ascii码表的97-122
    key = []
    #组成明文的英语单词字母集
    letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    cipher = open("./cipher.txt","r")
    content = cipher.read()
    content_arr = content.split(",")
    first_key = Counter() #统计密钥第一、二、三个字母最可能的是哪个，按符合条件的数量找出最大的
    second_key = Counter()
    third_key = Counter()

    i = 0
    for x in content_arr:#循环密文的每个ascii码
        i += 1
        if i%3 == 1:
            for k in range(97,122):#循环密钥中26个小写字母对应的ascii码
                m = k^int(x)
                if chr(int(m)) in letter:#明文是英语字母则符合条件
                    first_key[k] +=1
        if i%3 == 2:
            for k in range(97,122):
                m = k^int(x)
                if chr(int(m)) in letter:
                    second_key[k] +=1
        if i%3 == 0:
            for k in range(97,122):
                m = k^int(x)
                if chr(int(m)) in letter:
                    third_key[k] +=1
    key.append((first_key.most_common(1))[0][0])#第一个密钥最可能的值
    key.append((second_key.most_common(1))[0][0])
    key.append((third_key.most_common(1))[0][0])
    j =0
    for x in content_arr:
        j += 1
        if j%3 ==1:
            plain += chr(int(x)^int(key[0]))
        if j%3 ==2:
            plain += chr(int(x)^int(key[1]))
        if j%3 ==0:
            plain += chr(int(x)^int(key[2]))
    return plain #明文字符串



if __name__ == "__main__":
    plain = decrypt()
    decipher = open("./decipher.txt","a")
    decipher.write(plain)
    decipher.close()
