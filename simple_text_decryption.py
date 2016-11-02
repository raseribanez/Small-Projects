encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"
 
plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)
