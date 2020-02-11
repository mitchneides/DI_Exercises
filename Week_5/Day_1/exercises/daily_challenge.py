#
# class Subsets:
#     def __init__(self,list):
#         self.mylist = list
#         self.answerList = []
#
#     def getSubsets(self):
#         allVals = []
#         for c, val in enumerate(self.mylist):
#             loneVal = [val]
#             self.answerList.append(loneVal)
#             allVals.append(val)
#             while c < len(self.mylist)-1:
#                 newVals = [val,self.mylist[c+1]]
#                 self.answerList.append(newVals)
#                 c+=1
#         self.answerList.append(allVals)
#         self.answerList.append([])
#         print(self.answerList)
#
#
#
# l = [4,5,6]
# mySubset = Subsets(l)
# mySubset.getSubsets()





def GetToZero(l):

    l_len = len(l)
    found = False
    for i in range(0, l_len - 2):
        for j in range(i + 1, l_len - 1):
            for k in range(j + 1, l_len):
                if (l[i] + l[j] + l[k] == 0):
                    print([l[i], l[j], l[k]])
                    found = True

    if (found == False):
        print("No triplet combinations add to 0")


if __name__ == '__main__':
    list1 = [-25, -10, -7, -3, 2, 4, 8, 10]
    GetToZero(list1)



