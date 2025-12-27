from collections import Counter
def summing(numbers):
    even,odd = 0,0
    number = [n for n in numbers if -100<=n<=100]
    for i,v in enumerate(number):
        if v%2==0:
            even += v
        else:
            odd += v
    i+=1
    difference = even-odd
    return difference

# sliding window
def sliding_window(panel,codes):
    result = []
    # loop through the code
    for code in codes:
        # then loop through the index and pattern
        for i in range(1,len(code)):
            index_str = code[:i]
            pattern_str = code[i:]
            index = int(index_str)
            pattern = len(pattern_str)
            # index<panel, and panel has the pattern
            if index<len(panel) and panel[index:index+pattern] == pattern_str:
                result.append(pattern_str)
            else:
                result.append("Not Found")
        
def solution(grid):
    row = len(grid)
    col = len(grid[0])
    result = []
    for r in range(row):
        total_weight = 0
        curr_row= r
        dir = -1
        for c in range(col):
            total_weight+=grid[curr_row][c]
            if c<col-1:
                next_row = curr_row+dir
                if next_row<0:
                    dir = 1
                    curr_row = 1
                    
                elif next_row>=row:
                    dir = -1
                    curr_row = row-2
                else:
                    curr_row = next_row
        starting_row = grid[r][0]
        result.append((total_weight,starting_row))
    result.sort()
    return [v[1] for v in result]
    
solution([[2,3,2],[0,2,5],[1,0,1]])

def longestPossiblePalindrome(s):
    count = Counter(s)
    left = []
    mid = ""
    sorted_char = sorted(count.keys())
    for c in sorted_char:
        pairs = count[c]//2 
        left.append(c*pairs) 
        count[c] %= 2
    for c in sorted_char:
        if count[c]>0:
            mid = c
            break
    left_str = "".join(left)
    return left_str + mid + left_str[::-1]
longestPossiblePalindrome("aaabb")

def vowels(s):
    vowels = ["a","e","i","o","u"]
    count = 0
    for i in s:
        if i in vowels:
            count+=1
        else:
            count+=2
    return count

def solution(words, variableName):
    if not variableName:
        return False
    non_duplicates = set(words)
    parts = []
    curr = ""
    for c in variableName:
        if c.isupper() and curr!=" ":
            parts.append(c.lower())
            curr = c
        else:
            curr += c
    if curr:
        parts.append(curr.lower())
    for part in parts:
        if part not in non_duplicates:
            return False
    return True
        
def solution(board, word):
    row = len(board)
    col = len(board[0])
    n = len(word)
    count = 0
    if not board or not word:
        return 0
    for r in range(row):
        row_str = "".join(board[r])
        for i in range(len(row_str)-n+1):
            if row_str[i:i+n] == word:
                count+=1
    for c in range(col):
        col_str = "".join(board[r][c] for r in range(row))
        for j in range(len(col_str)-n+1):
            if col_str[j:j+n]==word:
                count+=1
    start = []
    for r in range(row):
        start.append((r,0))
    for c in range(1,col):
        start.append((0,c))
    for r,c in start:
        diag = []
        curr_r, curr_c = r,c
        while curr_r<row and curr_c<col:
            diag.append(board[curr_r][curr_c])
            curr_r+=1
            curr_c+=1
        diag_str = "".join(diag)
        for i in range(len(diag_str)-n+1):
            if diag_str[i:i+n] == word:
                count+=1
    return count
        
        
        
        
            

