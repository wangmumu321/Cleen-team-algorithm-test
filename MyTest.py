import sys
import os

metal_W = 0
metal_H = 0
entries = []
profit = []
profit_ave = []
sort_profit_ave = []
#min_w = 1
#min_h = 1

def get_min():
    global min_h,min_w
    min_w = min([entrie[0] for entrie in entries])
    min_h = min([entrie[1] for entrie in entries])
    pass



def getdata():
    f = open('./input.txt', 'r')
    i = 0
    for line in f.readlines():
        line = line.strip()
        #print("line is:" + line + "***")
        if i < 1:
            w, h = line.split(" ")
            global metal_H,metal_W
            metal_W = int(w)
            metal_H = int(h)
            i=i+1
        else:
            w, h, p = line.split(" ")
            entries.append([int(w),int(h)])
            profit.append(int(p))
            profit_ave.append(int(p)/(int(w) * int(h)))


def verify_data():
    if metal_W<=0 or metal_H<=0:
        return -1
    elif len(entries) != len(profit):
        return -2
    return 1

def get_total_profit(w,h):
    if w==0 or h ==0:
        print("get profit : 0")
        return 0
    '''
    if w<min_w or h<min_h:
        print("get profit : -1")
        return -1
    '''
    for p_av in sort_profit_ave:
        index = profit_ave.index(p_av)
        w1 = entries[index][0]
        h1 = entries[index][1]
        if w>=w1 and h>=h1:
            print("get profit : ",profit[index] )
            print("w and h is :",w1,h1)
            return profit[index] + get_total_profit(w-w1,h) + get_total_profit(w1, h-h1)
    print("get profit : -1")
    print("w and h is :", w, h)
    return -1


if __name__ == '__main__':
    getdata()
    print("metal_W is: " , metal_W)
    print("metal_H is: " , metal_H)
    print("entries is: " , entries)
    print("profit is: " , profit)
    print("profit_ave is: ", profit_ave)

    if verify_data():
        sort_profit_ave = sorted(profit_ave)
        sort_profit_ave.reverse()
        print("sort_profit_ave is: ",sort_profit_ave)

        #get_min()
        print("min_w is :", min_w)
        print("min_h is :", min_h)

        print(get_total_profit(metal_W,metal_H))
