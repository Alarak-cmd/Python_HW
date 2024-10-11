st = input()
leng = 0
p = 1
st = st.replace('н', '!')
for i in range(len(st) - 1):
    if st[i] == st[i + 1]:
        p += 1
        leng = max(leng, p)
    else:
        p = 1
print(leng, st)

st = input()
sh_st = st[st.find('(') + 1 : st.find(')')]
print(sh_st)

st = input()
l = st.split(' ')
for i in range(len(st)):
    if l[i][0] == 'а' and l[i][-1] == 'я':
        print(l[i])
