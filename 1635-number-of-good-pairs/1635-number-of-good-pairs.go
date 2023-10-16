func numIdenticalPairs(nums []int) int {
    out:=0

    for i, v:= range nums{
        for j, k := range nums{
            if i >= j{
                continue
            }
            if v == k{
                out++
            }
        }
    }

    return out
}