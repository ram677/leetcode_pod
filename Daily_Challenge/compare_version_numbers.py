#165. Compare Version Numbers

class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    # Split the version strings by '.' to get lists of revision numbers
    revs1 = version1.split('.')
    revs2 = version2.split('.')
    
    n1 = len(revs1)
    n2 = len(revs2)
    
    # Iterate up to the length of the longer revision list
    for i in range(max(n1, n2)):
      # Get the integer value of the revision for version1.
      # If the index is out of bounds, treat the revision as 0.
      # The int() conversion automatically handles leading zeros (e.g., "01" -> 1).
      r1 = int(revs1[i]) if i < n1 else 0
      
      # Get the integer value of the revision for version2.
      r2 = int(revs2[i]) if i < n2 else 0
      
      # Compare the revisions
      if r1 < r2:
        return -1
      if r1 > r2:
        return 1
        
    # If the loop completes, it means all revisions are equal
    return 0

# Time Complexity: O(m + n) where m and n are the lengths of version1 and version2 respectively.
# Space Complexity: O(m + n) for storing the split revision lists.