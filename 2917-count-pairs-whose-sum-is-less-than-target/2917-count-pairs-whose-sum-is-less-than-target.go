import (
    "sort"
    "fmt"
)
func countPairs(nums []int, target int) int {
    sort.Ints(nums)

    l, r:= 0, 1

    count:=0

    fmt.Println(nums)

    for l < r {
        
        if l>=len(nums)-1{
            break
        }
        
        if r > len(nums) - 1{
            if l >= len(nums)-2{
                break
            }
            l++
            r=l+1
        }
        fmt.Println(l, r, len(nums))
        
        res := nums[l]+nums[r]
        if res < target{
            r++
            count++
        } else {
            l++
            r=l+1
        }

    }

    return count
}