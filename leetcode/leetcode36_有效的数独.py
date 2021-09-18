class Solution:
    def vaidify(self,nums):
        uni = []
        for i in nums:
            if i!='.':
                if i not in uni:
                    uni.append(i)
                else:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        for i in range(m):
            # 验证行
            if not self.vaidify(board[i]):
                return False
            # 验证列
            if not self.vaidify([tmp[i] for tmp in board]):
                return False
            # 验证3*3的格子,从行开始，每次随着i验证一个3*3的格子
            tmp_nums = []
            for r_index in range(i//3*3,i//3*3+3):
                tmp_nums.extend(board[r_index][i%3*3:(i%3+1)*3])
            if not self.vaidify(tmp_nums):
                return False
            # columns:i%3*3:(i%3+1)*3
            # rows:i//3*3:i//3*3+3
        return True
