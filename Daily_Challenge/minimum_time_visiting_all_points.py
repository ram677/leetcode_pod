#1266. Minimum Time Visiting All Points

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Calculate minimum time to visit all points in order.
      
        Time is calculated using Chebyshev distance (diagonal moves allowed).
        The minimum time between two points is the maximum of absolute differences
        in x and y coordinates.
      
        Args:
            points: List of [x, y] coordinates to visit in order
          
        Returns:
            Minimum time (seconds) to visit all points
        """
        total_time = 0
      
        # Iterate through consecutive pairs of points
        for i in range(len(points) - 1):
            current_point = points[i]
            next_point = points[i + 1]
          
            # Calculate absolute differences in x and y coordinates
            x_distance = abs(current_point[0] - next_point[0])
            y_distance = abs(current_point[1] - next_point[1])
          
            # Time needed is the maximum of x and y distances (Chebyshev distance)
            # This accounts for diagonal movement being allowed
            time_between_points = max(x_distance, y_distance)
          
            total_time += time_between_points
      
        return total_time

# Time Complexity: O(n), where n is the number of points.
# Space Complexity: O(1).