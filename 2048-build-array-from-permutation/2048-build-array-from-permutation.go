func buildArray(nums []int) []int {
    a := make([]int,len(nums))
    for i, _:= range nums{
        a[i] = nums[nums[i]]
    }
    return a
}