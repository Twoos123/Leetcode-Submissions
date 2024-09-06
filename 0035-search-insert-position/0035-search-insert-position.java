class Solution {
    public int searchInsert(int[] nums, int target) {
        int beg = 0;
        int end = nums.length - 1;
        int mid = beg + (end - beg) / 2;

        while (beg <= end) {
            mid = beg + (end - beg) / 2;
            if (nums[mid] == target) {
                return mid;
            } // end if
            else if(nums[mid] > target){
                end = mid - 1;
            } // end elseif
            else {
                beg = mid + 1;
            } // end else
        } // end while+
        return beg;
    } // end function
} // end class
