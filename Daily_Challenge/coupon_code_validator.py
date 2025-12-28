#3606. Coupon Code Validator

class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        # Map business lines to their sort priority
        priority_map = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        valid_coupons = []
        n = len(code)
        
        for i in range(n):
            c = code[i]
            b = businessLine[i]
            active = isActive[i]
            
            # 1. Check if active
            if not active:
                continue
                
            # 2. Check valid business line
            if b not in priority_map:
                continue
                
            # 3. Check code validity
            if not c:  # Check if empty
                continue
                
            # Check characters (alphanumeric or underscore)
            is_valid_code = True
            for char in c:
                if not (char.isalnum() or char == '_'):
                    is_valid_code = False
                    break
            
            if is_valid_code:
                # Store tuple: (business_line, code_string)
                valid_coupons.append((b, c))
        
        # Sort based on:
        # 1. Priority of business line (using the map)
        # 2. Code string (lexicographical)
        valid_coupons.sort(key=lambda x: (priority_map[x[0]], x[1]))
        
        # Extract just the codes for the result
        return [item[1] for item in valid_coupons]
    
# Time Complexity: O(n log n) due to sorting, where n is the number of coupons.
# Space Complexity: O(n) for storing valid coupons.