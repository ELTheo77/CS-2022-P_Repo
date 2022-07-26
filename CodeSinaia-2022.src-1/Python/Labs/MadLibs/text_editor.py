with open('simple.txt') as f:
    lines = f.readlines()
text=""
count = 0
for line in lines:
    count += 1
    res=line.split()
    rezultat=""
    for word in res:
        if word[0]=='<' or (word[0]=='"' and word[1]=='<'):
            print("Select a/an ", end="")
            i=1
            while word[i]!='>':
                print(word[i], end="")
                i+=1
            print("\n")
            new_word=input()
            print("\n", end="")
            rezultat+=new_word
            i+=1
            while i<len(word):
                rezultat+=word[i]
                i+=1
            rezultat+=" "
        else:
            rezultat+=word+" "
    text+=rezultat+"\n"
    #print(f'{rezultat}')
print(text)
f.close()