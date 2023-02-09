class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0 # MAX AREA OF ISLAND
        visited = set() # tracks if we visited a coordinate already
        for row in range(len(grid)): # loop over grids
            for col in range(len(grid[0])): # loop over current grid and since they are all the same size we use 0
                current = self.discoverIsland(grid, visited, row, col) # recursive call to check for island length or if island exists
                res = max(res, current) #if the current island was greater then res, we update res
        return res
    
    def discoverIsland(self, grid, visited, r, c):
        row_bound = 0 <= r < len(grid) # makes sure we are in bounds for row
        col_bound = 0 <= c < len(grid[0]) # makes sure we are in bounds for column
        if not row_bound or not col_bound:
            return 0 # meaning its outside of range
        if (r, c) in visited: # we have already visited this coord so we return 0 to add nothing
            return 0
        visited.add((r,c)) # make sure to add this to visited to keep track
        if grid[r][c] == 0: # we return 0 because this is not a island
            return 0
         # otherwise we recursively call because now we know it is a island. we add one
        return 1 + self.discoverIsland(grid, visited,  r + 1, c) + self.discoverIsland(grid, visited, r, c + 1) + self.discoverIsland(grid, visited, r - 1, c) + self.discoverIsland(grid, visited, r, c -1)

#Issue i had with figuring out this problem is i had everything correct but
# I was calling visited in discover island, instead of making it a global variable.
#so it was using up alot of memory, it was creating a set for every position 
# which lead up to TLE
