func countNegatives(grid [][]int) int {
    count := 0
 for _, v := range grid{
     Inner:
     for j, x:= range v {
         if x <0{
             count += len(v) - j 
             break Inner
         }
     }
 }   
 return count
}