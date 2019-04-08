##########################################
# 
# 
# 
#    FILE PURELY USED FOR TESTING 
#
#
#
#
#
##########################################


from Crypto.Hash import SHA
user = 'f20171499'

t = SHA.new()
t.update(user.encode('utf-8'))

a = t.hexdigest()

s = int(a, 16)

sum = 0

while s>0:
    temp = s%10
    sum = sum + temp

print(sum)