import requests
from bs4 import BeautifulSoup
live = '&sp=EgJAAQ%253D%253D'
link  = input('paste the youtube link here(please note that live filter will be applied automativally):')
if live in link:
    uplink = link
else:
    uplink = link+live    
youtube = requests.get(uplink)  # Apply live filter in youtube and paste(replace) the link here.
soup = BeautifulSoup(youtube.content, 'html.parser')
rname = soup.get_text('|')
# print(rname)
nlst = rname.split(' watching|')
# print(nlst)
numlst = []
chanlst = []
for i in nlst:
    tstr = []
    for j in range(-1,-30,-1):
        if i[j] == '|':
            cnsf = j-3
            break
        else:
            tstr.append(i[j])
    nstr = tstr[::-1]        
    num = ''.join(nstr)
    numlst.append(num)
# print(numlst)  
for i in nlst:
    cn = []
    for j in range(cnsf,cnsf-30,-1):
        if i[j] == '|':
            break
        else:
            cn.append(i[j])
    cn = cn[::-1]
    cstr = ''.join(cn)
    chanlst.append(cstr)        
    
nmlst = []
for i in numlst:
    if ',' in i:
        ind = i.index(',')
        st = i[:ind]+i[ind+1:]
        nst = int(st)
        nmlst.append(st)  
    else:
        nmlst.append(i)

nmlst = nmlst[:-1]    
nmlst = [int(i) for i in nmlst]     # ultimate number of people watching list
# print(nmlst)      
# print(chanlst)
# print(rname)
lstfname = rname.split('all filters')
# print(rname)
# print(lstfname)
# print(len(lstfname))
# print(lstfname)
neecstr = lstfname[1]
# print(neecstr)
neeclist = neecstr.split('|\n|\n|\n| |\n|\n|\n|')
# print(neeclist)
neeclist = neeclist[1:-1]
# print(neeclist)
clst = []
for i in neeclist:
    de = i.index('|')
    cname = i[:de]
    clst.append(cname)
# print(clst)       #ultimate  list of channels
mergewc = tuple(zip(clst,nmlst))    #tupple version of merge
mergdict = {clst[i]:nmlst[i] for i in range(len(clst))}    #unsorted dictionary version of merge
sortdict = {k: v for k, v in sorted(mergdict.items(), key=lambda item: item[1])}   #sorted dictionary version of merge(ultimate required list)
print(sortdict)
print('goodluck')
a = input()




           
            

