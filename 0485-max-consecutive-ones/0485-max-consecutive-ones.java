class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int sum = 0;
        int i = 0;
        int c = 0;
        while(i < nums.length){
            if(nums[i] != 1){
                if(sum < c){
                    sum = c;
                }
                c = 0;
            }else{
                c++;
            }
            i++;
        }
        if(sum < c){
            sum = c;
        }
        return sum;
    }
}