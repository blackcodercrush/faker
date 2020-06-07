#!/bin/python2.7
# coding: utf-8

import requests, os, sys, time, getpass

"""
Author: Desta Adyangga Saputra
Make: 7 june, 2020
Team: Black Coder Crush
"""

bi = '\x1b[34;1m'
cy = '\x1b[36;1m'
i = '\x1b[32;1m'
ku = '\x1b[33;1m'
lbi = '\x1b[94;1m'
lcy = '\x1b[95;1m'
lpur = '\x1b[95;1m'
me = '\x1b[31;1m'
pu = '\x1b[37;1m'
pur = '\x1b[35;1m'
reset = '\x1b[0;1m'

os.system('clear')

print(bi+''' \t _____     _        _   _
\t|  ___|_ _| | _____| | | |___  ___ _ __
\t| |_ / _` | |/ / _ \ | | / __|/ _ \ '__|
\t|  _| (_| |   <  __/ |_| \__ \  __/ |
\t|_|  \__,_|_|\_\___|\___/|___/\___|_|\n''')
print('\t\t{}[ {}Black Coder Crush {}]\n').format(me,pu,me)
print('\t{}Author{}: {}Mr.Đ`HACK {}/ {}Desta').format(cy,me,pu,me,pu)
print('\t{}Team{}: {}Black Coder Crush').format(cy,me,pu)

print('\t'+i+'_'*40)

getpass.getpass('\n\t{}[{}+{}] Enter To Get Data User{}: '.format(pu,i,pu,me))

print('\t'+i+'_'*40+'\n')

res = requests.get('https://randomuser.me/api').json()["results"][0]

print('\t{}------------ {}information {}-----------').format(me,pu,me)
print('\t{}[{}+{}] FirstName{}: {}{}').format(pu,i,pu,me,cy,res["name"]["first"].encode('utf-8'))
print('\t{}[{}+{}] LastName{}: {}{}').format(pu,i,pu,me,cy,res["name"]["last"].encode('utf-8'))
print('\t{}[{}+{}] FullName{}: {}{}').format(pu,i,pu,me,cy,res["name"]["first"].encode('utf-8')+' '+res["name"]["last"].encode('utf-8'))
print('\t{}[{}+{}] Title{}: {}{}').format(pu,i,pu,me,cy,res["name"]["title"])
print('\t{}[{}+{}] Date{}: {}{}').format(pu,i,pu,me,cy,res["dob"]["date"])
print('\t{}[{}+{}] Age{}: {}{}').format(pu,i,pu,me,cy,res["dob"]["age"])
print('\t{}[{}+{}] Gender{}: {}{}').format(pu,i,pu,me,cy,res["gender"])
print('\t{}[{}+{}] ID{}: {}{}{}, {}{}').format(pu,i,pu,me,cy,res["id"]["name"],me,cy,res["id"]["value"])
print('\t{}[{}+{}] Cell{}: {}{}').format(pu,i,pu,me,cy,res["cell"])
print('\t{}[{}+{}] Phone{}: {}{}').format(pu,i,pu,me,cy,res["phone"])
print('\t{}[{}+{}] City{}: {}{}').format(pu,i,pu,me,cy,res["location"]["city"].encode('utf-8'))
print('\t{}[{}+{}] Country{}: {}{}').format(pu,i,pu,me,cy,res["location"]["country"].encode('utf-8'))
print('\t{}[{}+{}] Latitude{}: {}{}').format(pu,i,pu,me,cy,res["location"]["coordinates"]["latitude"].encode('utf-8'))
print('\t{}[{}+{}] Longitude{}: {}{}').format(pu,i,pu,me,cy,res["location"]["coordinates"]["longitude"].encode('utf-8'))
print('\t{}[{}+{}] State{}: {}{}').format(pu,i,pu,me,cy,res["location"]["state"].encode('utf-8'))
print('\t{}[{}+{}] Street{}: {}{}{}, {}{}').format(pu,i,pu,me,cy,res["location"]["street"]["number"],me,cy,res["location"]["street"]["name"].encode('utf-8'))
print('\t{}[{}+{}] Postcode{}: {}{}').format(pu,i,pu,me,cy,res["location"]["postcode"])
print('\t{}[{}+{}] Timezone{}: {}{} {}').format(pu,i,pu,me,cy,res["location"]["timezone"]["description"],res["location"]["timezone"]["offset"])
print('\t{}[{}+{}] Nat{}: {}{}').format(pu,i,pu,me,cy,res["nat"].encode('utf-8'))

ask = raw_input('\n\t{}[{}?{}] Reset{}/{}Exit{}[{}R{}/{}E{}]{}: {}'.format(pu,ku,pu,me,pu,bi,i,pu,i,bi,me,cy))

if ask.lower() == 'r':
	os.system('python2 fake.py')
else:
	exit(reset)

"""
Don't recode !!
Reedit? Write Author
https://github.com/blackcodercrush
""""
