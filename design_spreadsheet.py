#3484. Design Spreadsheet

from typing import List

class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = {}
        # The 'rows' parameter is a constraint, not strictly needed for this
        # dictionary-based implementation.

    def setCell(self, cell: str, value: int) -> None:
        self.grid[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.grid:
            del self.grid[cell]

    def _evaluate_operand(self, operand: str) -> int:
        if operand.isdigit():
            return int(operand)
        else:
            # .get(key, 0) elegantly handles unset cells by returning the
            # default value 0 if the key is not found.
            return self.grid.get(operand, 0)

    def getValue(self, formula: str) -> int:
        # Remove the leading '='
        expression = formula[1:]
        
        # Split the expression into two operand strings
        operand1_str, operand2_str = expression.split('+')
        
        # Evaluate each part and return their sum
        value1 = self._evaluate_operand(operand1_str)
        value2 = self._evaluate_operand(operand2_str)
        
        return value1 + value2
    
# Time Complexity:
# setCell: O(1) - Direct dictionary assignment.
# resetCell: O(1) - Direct dictionary deletion.         
# getValue: O(1) - Each lookup and arithmetic operation is O(1).
# _evaluate_operand: O(1) - Each lookup or conversion is O(1).
# Space Complexity: O(m) where m is the number of unique cells set in the grid.