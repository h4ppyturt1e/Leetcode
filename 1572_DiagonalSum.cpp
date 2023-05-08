class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int matSize = mat.size();
        int sum = 0;

        // left and right ptr
        for (int left = 0, right = matSize - 1; left < matSize; left++, right--) {
            sum += mat[left][left] + mat[left][right];
        }

        // if matSize is odd, subtract the middle element
        if (matSize % 2 == 1) {
            sum -= mat[matSize / 2][matSize / 2];
        }

        return sum;
    }
};