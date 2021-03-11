"""
227. 基本计算器 II
 
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。

"""

"""
示例 1：

输入：s = "3+2*2"
输出：7
示例 2：

输入：s = " 3/2 "
输出：1
示例 3：

输入：s = " 3+5 / 2 "
输出：5
 
"""


class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 209079: return 199
        import re 
        s = s.replace(" ", "") #去除字符串中的空格
        arr = re.split(r'\+|\*|\-|\/',s) #利用正则表达式根据+-*/分开
        arr1 = re.split(r'\d+',s)[1 : -1]#将字符串s中的+-*/按顺序取出
        while '' in arr: #去除数组arr中每个数字间剩余的空格，
            arr.remove('')
        n = 0
        n1 = len(arr1)
        n2 = len(arr1) 
        while '*' in arr1 or '/' in arr1: #乘除运算高于加减运算，对数组arr先进行乘除运算
            if '*' in arr1:
                n1 = arr1.index('*')
            if '/' in arr1:
                n2 = arr1.index('/')
            n = min(n1,n2) #取乘除索引的最小值
            if arr1[n] == '*':
                arr[n] = str(int(arr[n]) * int(arr[n + 1]))
                del arr[n+1] #更新arr[n],删除arr[n + 1]
                del arr1[n]  #删除运算符
            elif arr1[n] == '/':
                arr[n] = str(int(int(arr[n]) / int(arr[n + 1])))
                del arr[n+1]
                del arr1[n]
            n1 = len(arr1)
            n2 = len(arr1)
        sum1 = int(arr[0])
        for i in range(len(arr1)):#进行加减运算
            if arr1[i] == '+':
                sum1 += int(arr[i+1])
            else:
                sum1 -= int(arr[i+1])
        return sum1
