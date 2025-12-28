#2353. Design a Food Rating System

from collections import defaultdict
import heapq
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """
        Initializes the system with food data and builds the necessary data structures.
        """
        # Map food -> rating for quick rating updates and validation.
        self.food_to_rating = {}
        # Map food -> cuisine to know which heap to update.
        self.food_to_cuisine = {}
        # Map cuisine -> min-heap of (-rating, food_name).
        # We use a min-heap with negative ratings to simulate a max-heap.
        self.cuisine_to_foods = defaultdict(list)

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            
            self.food_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            
            # Push (-rating, food_name) to the min-heap.
            # Python's tuple comparison will use food_name as a tie-breaker.
            heapq.heappush(self.cuisine_to_foods[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        """
        Changes the rating of a food and adds the new rating to the heap.
        """
        # Update the canonical rating of the food.
        self.food_to_rating[food] = newRating
        
        # Find the cuisine to know which heap to add to.
        cuisine = self.food_to_cuisine[food]
        
        # Add the new rating to the heap. The old rating entry is now "stale"
        # but we leave it in (lazy deletion).
        heapq.heappush(self.cuisine_to_foods[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        """
        Returns the highest-rated food for a cuisine, cleaning up stale entries.
        """
        # Get the specific heap for this cuisine.
        heap = self.cuisine_to_foods[cuisine]
        
        # The top of the heap might have a stale rating.
        # We loop until we find an entry whose rating matches the current
        # actual rating of that food.
        while heap:
            # Peek at the top element: (-rating, food_name)
            neg_rating, food = heap[0]
            
            # Check if the rating in the heap is the food's current rating.
            if -neg_rating == self.food_to_rating[food]:
                # If it's up-to-date, we've found our answer.
                return food
            else:
                # If not, it's a stale entry from a past rating. Pop it and check the next one.
                heapq.heappop(heap)

# Time Complexity:
# - __init__: O(n log n) for pushing n foods into heaps.
# - changeRating: O(log k) where k is the number of foods in the cuisine.
# - highestRated: O(log k) for the heap operations. 
# Space Complexity: O(n) for storing all foods and their ratings.
# where n is the number of foods and k is the number of foods in a specific cuisine.