#2943. Maximize Area of Square Hole in Grid

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_max_gap(bars):
            if not bars:
                return 1
            
            bars.sort()
            max_len = 1
            current_len = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_len += 1
                else:
                    current_len = 1
                max_len = max(max_len, current_len)
                
            return max_len + 1
        
        # Calculate the maximum contiguous gap for height and width
        max_height = get_max_gap(hBars)
        max_width = get_max_gap(vBars)
        
        # The square is limited by the smaller of the two dimensions
        side = min(max_height, max_width)
        
        return side * side
    
#Time Complexity: O(H log H + V log V), where H and V are the lengths of hBars and vBars respectively, due to sorting.
#Space Complexity: O(1).