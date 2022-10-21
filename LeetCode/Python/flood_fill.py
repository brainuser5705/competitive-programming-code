class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_val = image[sr][sc]
        if curr_val == color:
            return image
        
        image[sr][sc] = color
        return self.recursiveCall(image, sr, sc, color, curr_val)
        
        
    def recursiveCall(self, image, sr, sc, color, prev):
        
        # check bounds
        top = sr - 1
        bottom =  sr + 1
        right = sc + 1
        left = sc - 1

        if top >= 0 and image[top][sc] == prev:
            image[top][sc] = color
            self.recursiveCall(image, top, sc, color, prev)
            
        if bottom <= len(image)-1 and image[bottom][sc] == prev:
            image[bottom][sc] = color
            self.recursiveCall(image, bottom, sc, color, prev)
            
        if right <= len(image[0])-1 and image[sr][right] == prev:
            image[sr][right] = color
            self.recursiveCall(image, sr, right, color, prev)
            
        if left >= 0 and image[sr][left] == prev:
            image[sr][left] = color
            self.recursiveCall(image, sr, left, color, prev)
            
        return image
        