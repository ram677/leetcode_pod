#3013. Divide an Array Into Subarrays With Minimum Cost II

from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # Cost of the first subarray is always nums[0]
        base_cost = nums[0]
        
        # We need to select k-1 additional starting positions.
        # The constraint is that the distance between the first and last selected index
        # is at most 'dist'. This effectively means we look at a sliding window
        # of size 'dist + 1' in nums[1:], and we need to find the sum of the 
        # smallest k-1 elements in that window.
        
        target_count = k - 1
        window_size = dist + 1
        
        # 'L' contains the smallest 'target_count' elements (active selection)
        # 'R' contains the rest of the elements in the current window
        L = SortedList()
        R = SortedList()
        
        current_sum = 0
        
        # 1. Initialize the first window
        # The window covers indices 1 to dist + 1 (inclusive)
        # Note: The problem guarantees n is large enough for at least one valid set.
        # We process nums[1] to nums[window_size] initially?
        # Actually, we just add elements and once we hit the window size, we record answers.
        
        # Let's verify constraints: window must be length dist+1.
        # We consider elements nums[1]...nums[dist+1].
        # From these, we pick the k-1 smallest.
        
        # We simply loop through nums starting from index 1.
        min_cost = float('inf')
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # --- ADD NEW ELEMENT ---
            # Try adding to L first to keep it populated
            L.add(num)
            current_sum += num
            
            # If L is too big, move the largest element from L to R
            if len(L) > target_count:
                largest = L.pop() # Removes the last (largest) element
                current_sum -= largest
                R.add(largest)
            
            # --- REMOVE OLD ELEMENT ---
            # If the window has moved past size 'dist + 1', remove the element that is sliding out.
            # The element to remove is at index 'i - (dist + 1)'
            if i > dist + 1:
                out_elem = nums[i - (dist + 1)]
                
                if out_elem in L:
                    L.remove(out_elem)
                    current_sum -= out_elem
                    
                    # L is now smaller than target_count, refill from R if possible
                    if R:
                        smallest_R = R.pop(0) # Pop smallest from R
                        L.add(smallest_R)
                        current_sum += smallest_R
                else:
                    R.remove(out_elem)
            
            # --- UPDATE ANSWER ---
            # We only check for answer if we have formed a full window of size at least 'k-1'
            # The window effectively grows until it hits size dist+1, then slides.
            # We just need to make sure we have enough elements to pick k-1.
            if i >= k - 1:
                min_cost = min(min_cost, base_cost + current_sum)
                
        return min_cost
    
# Time Complexity: O(n log(k)) due to SortedList operations, where n is the length of nums and k is the number of subarrays.
# Space Complexity: O(k) for storing elements in L and R.