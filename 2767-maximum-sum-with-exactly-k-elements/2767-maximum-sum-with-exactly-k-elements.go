
func maximizeSum(nums []int, k int) int {
    out:=0
    max := 0 
    for _, v:=range nums{
        if v > max{
            max = v
        }
    }
    for k >0{
        out += max
        max++
        nums[len(nums)-1] = max
        k--
    }

    return out
}