from collections import Counter
from debug_decorator import debug

@debug(
    [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]],
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]],
)
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            
            box_idx = (r // 3) * 3 + (c // 3)
            
            if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                return False
            
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)
            
    return True


@debug([[1,2,3],[4,5,6],[7,8,9]])
def spiral_order(matrix):
    if not matrix: return []

    # 初始化四面墙的边界
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    res = []

    while True:
        # 1. 从左向右走 (在 top 行)
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1 # 顶墙下移
        if top > bottom: break

        # 2. 从上向下走 (在 right 列)
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1 # 右墙左移
        if left > right: break

        # 3. 从右向左走 (在 bottom 行)
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1 # 底墙上移
        if top > bottom: break

        # 4. 从下向上走 (在 left 列)
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1 # 左墙右移
        if left > right: break

    return res


@debug([[1,2,3],[4,5,6],[7,8,9]])
def rotate(matrix):
    # 上下对称再转置就行了
    matrix.reverse()
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


    return matrix

@debug([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
def set_zeros(matrix):
    # 只需要记录哪一行和哪一列需要置0,而且使用第一行第一列来存储
    rows, cols = len(matrix), len(matrix[0])
    row0_flag = any(matrix[0][j] == 0 for j in range(cols))
    col0_flag = any(matrix[i][0] == 0 for i in range(rows))

    # 使用第一行和第一列做标记
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # 根据标记置零
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # 别忘了处理第一行和第一列
    if row0_flag:
        for j in range(cols): matrix[0][j] = 0
    if col0_flag:
        for i in range(rows): matrix[i][0] = 0

    return matrix

@debug([[0,1,0],[0,0,1],[1,1,1],[0,0,0]], exec=True)
def game_of_life(board):
    if not board: return

    rows, cols = len(board), len(board[0])
    # 8个邻居的方向坐标
    neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    for r in range(rows):
        for c in range(cols):
            # 统计周围活细胞数量
            live_neighbors = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                # 只要编码是 1 或 2，说明原状态是活的
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in [1, 2]:
                    live_neighbors += 1

            # 规则判断
            if board[r][c] == 1:
                # 规则 1 & 3: 活变死
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = 2
            else:
                # 规则 4: 死变活
                if live_neighbors == 3:
                    board[r][c] = 3

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 2: board[r][c] = 0
            elif board[r][c] == 3: board[r][c] = 1



