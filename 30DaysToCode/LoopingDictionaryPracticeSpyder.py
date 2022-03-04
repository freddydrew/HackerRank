# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:30:00 2022

@author: dalia
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
name_numbers = [input().split() for i in range(n)]
phone_nums = {key:value for key,value in name_numbers}
query = None
while True:
    try:
        query = input()
        if query in phone_nums:
            print(f'{query}={phone_nums[query]}')
        else:
            print('Not found')
    except:
        break
