from cs50 import get_string
import re

number = get_string("Number:")
length = len(number)

a = int(number) % 10
b = int(int(number) % 100 / 10)
c = int(int(number) % 1000 / 100)
d = int(int(number) % 10000 / 1000)
e = int(int(number) % 100000 / 10000)
f = int(int(number) % 1000000 / 100000)
g = int(int(number) % 10000000 / 1000000)
h = int(int(number) % 100000000 / 10000000)
i = int(int(number) % 1000000000 / 100000000)
j = int(int(number) % 10000000000 / 1000000000)
k = int(int(number) % 100000000000 / 10000000000)
m = int(int(number) % 1000000000000 / 100000000000)
n = int(int(number) % 10000000000000 / 1000000000000)
o = int(int(number) % 100000000000000 / 10000000000000)
p = int(int(number) % 1000000000000000 / 100000000000000)
r = int(int(number) % 10000000000000000 / 1000000000000000)
    
aa = ((a * 2) % 10) + int(a * 2 / 10)
bb = ((b * 2) % 10) + int(b * 2 / 10)
cc = ((c * 2) % 10) + int(c * 2 / 10)
dd = ((d * 2) % 10) + int(d * 2 / 10)
ee = ((e * 2) % 10) + int(e * 2 / 10)
ff = ((f * 2) % 10) + int(f * 2 / 10)
gg = ((g * 2) % 10) + int(g * 2 / 10)
hh = ((h * 2) % 10) + int(h * 2 / 10)
ii = ((i * 2) % 10) + int(i * 2 / 10)
jj = ((j * 2) % 10) + int(j * 2 / 10)
kk = ((k * 2) % 10) + int(k * 2 / 10)
mm = ((m * 2) % 10) + int(m * 2 / 10)
nn = ((n * 2) % 10) + int(n * 2 / 10)
oo = ((o * 2) % 10) + int(o * 2 / 10)
pp = ((p * 2) % 10) + int(p * 2 / 10)
rr = ((r * 2) % 10) + int(r * 2 / 10)
    
if length == 15:
    if re.search("^34", number) or re.search("^37", number):
        first_sum = bb + dd + ff + hh + jj + mm + oo
        second_sum = first_sum + a + c + e + g + i + k + n + p
        modulo = second_sum % 10
        if modulo is 0:
            print("AMEX")
        else:
            print("INVALID")

elif length == 16:
    if re.search("^51", number) or re.search("^52", number) or re.search("^53", number) or re.search("^54", number) or re.search("^55", number):
        first_sum = bb + dd + ff + hh + jj + mm + oo + rr
        second_sum = first_sum + a + c + e + g + i + k + n + p
        modulo = second_sum % 10
        if modulo is 0:
            print("MASTERCARD")
        else:
            print("INVALID")
            
    elif re.search("^4", number):
        first_sum = bb + dd + ff + hh + jj + mm + oo + rr
        second_sum = first_sum + a + c + e + g + i + k + n + p
        modulo = second_sum % 10
        if modulo is 0:
            print("VISA")
        else:
            print("INVALID")

elif length == 13:
    if re.search("^4", number):
        first_sum = bb + dd + ff + hh + jj + mm
        second_sum = first_sum + a + c + e + g + i + k + n
        modulo = second_sum % 10
        if modulo is 0:
            print("VISA")
        else:
            print("INVALID")

else:
    print("INVALID")