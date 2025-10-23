class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int maxProd = nums[0];  // max product ending here
        int minProd = nums[0];  // min product ending here
        int result = nums[0];   // global max
        
        for (int i = 1; i < n; i++) {
            int tempMax = maxProd;  // store current max before updating
            
            maxProd = Math.max(nums[i], Math.max(maxProd * nums[i], minProd * nums[i]));
            minProd = Math.min(nums[i], Math.min(tempMax * nums[i], minProd * nums[i]));
            
            result = Math.max(result, maxProd);
        }
        
        return result;
    }
}
