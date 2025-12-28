#2483. Minimum Penalty for a Shop

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Start with a score of 0.
        # We don't need the absolute penalty value, just the relative minimum.
        # However, to be intuitive: 
        # current_penalty could start at customers.count('Y') (closing at 0).
        # But a simpler "score" approach works: 
        # 'Y' decreases score (good to be open), 'N' increases score (bad to be open).
        
        max_score = 0  # To track the "best" gain from being open
        score = 0
        best_hour = 0
        
        for i, char in enumerate(customers):
            if char == 'Y':
                score += 1 # Found a customer, score improves (penalty goes down)
            else:
                score -= 1 # No customer, score drops (penalty goes up)
            
            # If our current score is the highest we've seen, this is the best time 
            # to close (right after this hour)
            if score > max_score:
                max_score = score
                best_hour = i + 1
                
        return best_hour
    
# Time Complexity: O(n), where n is the length of the customers string.
# Space Complexity: O(1), we use a constant amount of extra space.