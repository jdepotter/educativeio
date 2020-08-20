class Solution:
    def move(self, cnt, tab):     
        if cnt == self.n:
            self.res.append(tab[:])
        
        for i in range(cnt, self.n):
            tab[cnt], tab[i] = tab[i], tab[cnt]
            self.move(cnt + 1, tab)
            tab[cnt], tab[i] = tab[i], tab[cnt]
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.n = len(nums)
        
        self.move(0, nums)
        return self.res