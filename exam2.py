import time
print("{0:.0f}".format(time.time()))
alphabetic=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','I','J','K','L','M','N',
'O','P','Q','R','S','T','V','W','X','Y','Z']

random=int("{0:.0f}".format(time.time()))%25

print(alphabetic[random])

