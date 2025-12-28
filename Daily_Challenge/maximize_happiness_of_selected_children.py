#3075. Maximize Happiness of Selected Children

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort in descending order to pick the happiest children first
        happiness.sort(reverse=True)
        
        total_happiness = 0
        
        for i in range(k):
            # The i-th child selected has their happiness reduced by i
            current_val = happiness[i] - i
            
            # If the calculated value is <= 0, this child and all subsequent 
            # children (who are smaller and have higher penalties) contribute 0.
            if current_val <= 0:
                break
                
            total_happiness += current_val
            
        return total_happiness

# Time Complexity: O(n log n) due to sorting the happiness list, where n is the number of children.
# Space Complexity: O(1) as we are using only a constant amount of extra space.