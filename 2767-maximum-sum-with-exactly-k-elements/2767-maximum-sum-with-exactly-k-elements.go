import "sort"
func maximizeSum(nums []int, k int) int {
    out:=0
    sort.Ints(nums)
    for k >0{
        out += nums[len(nums)-1]
        nums[len(nums)-1]++
        k--
    }

    return out
}