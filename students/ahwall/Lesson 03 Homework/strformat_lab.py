#!/usr/bin/env python3


# Task One:
def tupleFormat(tups):

    # defines and formats filename
    fname = tups[0]
    file_name = ('file{:03d}:'.format(fname))

# defines and formats first float
    num2tup = tups[1]
    num2tupfort = "{:.2f}".format(num2tup)

# defines and formats first integer
    int3tup = tups[2]
    int(int3tup)
    int3tupfort = "{:.2E}".format(int3tup)

# defines and formats first float
    float4tup = tups[3]
    float4tupfort = "{:.2E}".format(float4tup)

    print(file_name, num2tupfort, int3tupfort, float4tupfort)


# Task Two:
def altTupleFormat(tups):

    # defines and formats filename
    fname = tups[0]
    altFile_name = f"file{fname:03d}:"

# defines and formats first float
    altnum2tup = tups[1]
    altnum2tupfort = f"{altnum2tup:.2f}"

# defines and formats first integer
    altint3tup = tups[2]
    int(altint3tup)
    altint3tupfort = f"{altint3tup:.2E}"

# defines and formats first float
    altfloat4tup = tups[3]
    altfloat4tupfort = f"{altfloat4tup:.2E}"

    print(altFile_name, altnum2tupfort, altint3tupfort, altfloat4tupfort)


# Task Three:
def dynamicFormat(tups):


    leng = len(tups)
    dyntups = "The {:d} numbers are ".format(leng) + ",".join(["{}"]
    *leng).format(*tups)
    print(dyntups)


#Task Four:
tups = (4, 30, 2017, 2, 27)
newtup = []
for item in tups:
    if item < 10:
        newtup.append('{:02d}'.format(item))
    else:
        newtup.append(item)
tup2 = newtup[3:] + newtup[2:3] + newtup[:2]
print(tup2)


# Task Five
FruNumlist = ['oranges', 1.3, 'lemons', 1.1]
fFruNum = f"The Weight of an {FruNumlist[0]} is {FruNumlist[1]} and the \
weight of a {FruNumlist[2]} is {FruNumlist[3]}."
print(fFruNum)

fFruNum = f"The Weight of an {FruNumlist[0].upper()} is {FruNumlist[1]*(1.2)} \
and the weight of a {FruNumlist[2].upper()} is {FruNumlist[3]*(1.2)}."
print(fFruNum)


'''
if __name__ == "__main__":
    #tupleFormat(tups)
    altTupleFormat(tups)
'''
