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


class Subsets:
    def __init__(self, list):
        self.list = list

    def GetToZero(self):
        answers = []
        self.list.sort()
        for i in range(len(self.list) - 2):
            if i > 0 and self.list[i] == self.list[i - 1]:
                continue
            j = i + 1
            k = len(self.list) - 1
            while j < k:
                sum = self.list[i] + self.list[j] + self.list[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    answers.append([self.list[i], self.list[j], self.list[k]])
                    while j < k and self.list[j] == self.list[j + 1]:
                        j += 1
                        while j < k and self.list[k] == self.list[k - 1]:
                            k -= 1
                            j += 1
                            k -= 1
                        print(answers)
                        return answers


l = [-25, -10, -7, -3, 2, 4, 8, 10]
mySubset = Subsets(l)
mySubset.GetToZero()
