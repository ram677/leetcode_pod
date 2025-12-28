#812. Largest Triangle Area

class Solution:
  def largestTriangleArea(self, points: list[list[int]]) -> float:
    ans = 0

    for Ax, Ay in points:
      for Bx, By in points:
        for Cx, Cy in points:
          ans = max(ans, 0.5 * abs((Bx - Ax) * (Cy - Ay) - (Cx - Ax) * (By - Ay)))

    return ans

# Time Complexity: O(n^3) where n is the number of points.
# Space Complexity: O(1) since we are using only a constant amount of extra space.