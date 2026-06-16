class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        fir,las=0,n-1
        while fir<las:
            tot=numbers[fir]+numbers[las]
            if tot==target:
                return [fir+1,las+1]
            elif tot<target:
                fir+=1
            else:
                las-=1
        return []