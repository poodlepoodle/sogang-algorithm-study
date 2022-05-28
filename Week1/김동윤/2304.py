import sys

n = int(sys.stdin.readline().rstrip())
stk=[]
save=[]
res=0

for i in range(n) :
    save.append(list(map(int,sys.stdin.readline().rstrip().split()))) 

save.sort() # x축 기준으로 오름차순
for i in range(len(save)) :
    save[i].append(i)

# 가장 높이가 긴 아이의 인덱스를 찾기
maxheight=-999
maxidx=0
for i in save:
    if maxheight<i[1] :
        maxheight = i[1]
        maxidx=i[2]

stk.append(save[0])

#전
for i in range(1,maxidx+1) :
    if stk[-1][1] < save[i][1] : 
        res+=(save[i][0]-stk[-1][0])*stk[-1][1]
        stk.append(save[i])

# 가장 높은 것 만났을 때 
res+=save[maxidx][1]
stk.append(save[maxidx])

#후
stk2=[] # 새로운 스택 생성 
stk2.append(save[-1])

for j in range(n-2, maxidx-1, -1) : 
    if stk2[-1][1] <= save[j][1] : 
        res+=(stk2[-1][0]-save[j][0])*stk2[-1][1]
        stk2.append(save[j])

print(res)

