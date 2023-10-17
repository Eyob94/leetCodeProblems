func countNegatives(grid [][]int) int {
    rowLen, colLen := len(grid), len(grid[0])
    count := 0
    row, col := 0, colLen - 1
    for row < rowLen && col >=0{
        if grid[row][col]<0{
            col--
            count += rowLen - row
        }else{
            row++
        }
    }
 return count
}