#1733. Minimum Number of People to Teach

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        num_users = len(languages)
        
        # Convert languages to sets for O(1) lookups
        lang_sets = [set(langs) for langs in languages]
        
        # Find non-communicating friendships
        non_communicating_pairs = []
        for u, v in friendships:
            # Users are 1-indexed, adjust to 0-indexed
            u -= 1
            v -= 1
            
            # Check for common languages
            if not lang_sets[u].intersection(lang_sets[v]):
                non_communicating_pairs.append((u, v))
                
        # If all friends can communicate, no teaching is needed
        if not non_communicating_pairs:
            return 0
        
        min_teachings = float('inf')
        
        # Iterate through each language to find the best one to teach
        for lang in range(1, n + 1):
            users_to_teach = set()
            for u, v in non_communicating_pairs:
                # If user u doesn't know the language, they need to be taught
                if lang not in lang_sets[u]:
                    users_to_teach.add(u)
                # If user v doesn't know the language, they need to be taught
                if lang not in lang_sets[v]:
                    users_to_teach.add(v)
            
            min_teachings = min(min_teachings, len(users_to_teach))
            
        return min_teachings
    
#Time Complexity: O(F * L) where F is the number of friendships and L is the number of languages.
#Space Complexity: O(U + F) where U is the number of users and F is the number of friendships.