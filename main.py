class Solution:
    def permutation(self,s):
        def permute(data, i, length):
            if i == length:
                result.append(''.join(data) )
            else:
                for j in range(i, length):
                    data[i], data[j] = data[j], data[i]
                    permute(data, i + 1, length)
                    data[i], data[j] = data[j], data[i]
        result=[]
        permute(list(s),0,len(s))
        result=sorted(result)
        return result