/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
     let maxEnding = nums[0]
    let maxSoFar = nums[0]

    for(let i =1; i<nums.length; i++){
        maxEnding = Math.max(maxEnding +nums[i], nums[i])
        maxSoFar = Math.max(maxEnding, maxSoFar)
    }

    return maxSoFar
};