class Solution {
    public int pivotIndex(int[] nums) {
        int sum1 = 0;
        int sum = 0;
        int j = nums.length;
        for(int x = 0; x < j; x++){
            sum += nums[x];
        }
        for(int i = 0; i < nums.length; i++){
            int sum2 = sum - sum1 - nums[i];
            if(sum2 == sum1){
                return i;
            }
            sum1 += nums[i];
        }
        return -1;
    }
}