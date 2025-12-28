#3074. Apple Redistribution into Boxes

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # 1. Get the total number of apples to store
        total_apples = sum(apple)
        
        # 2. Sort capacity in descending order to use the largest boxes first
        capacity.sort(reverse=True)
        
        boxes_used = 0
        
        # 3. Fill boxes one by one
        for cap in capacity:
            total_apples -= cap
            boxes_used += 1
            
            # If all apples are stored (total_apples <= 0), we are done
            if total_apples <= 0:
                return boxes_used
                
        return boxes_used

# Time Complexity: O(n log n) due to sorting the capacity list, where n is the number of boxes.
# Space Complexity: O(1) as we are using only a constant amount of extra space.