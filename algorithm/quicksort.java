public static void quickSort(int[] nums){
    quickSortRecursive(nums, 0, nums.length - 1);
}

public static quickSortRecursive(int[] nums, int left, int right){
    if (left >= right){
        return;
    }

    int pivotPos = partition(nums, left, right);

    quickSortRecursive(nums, left, pivotPos - 1);
    quickSortRecursive(nums, pivotPos + 1, right);
    
}

public static int partition(int[] nums, int left, int right){
    int pivot = nums[right];
    int i = (left - 1);
    for (int j = left; j<right; ++j){
        if(nums[j] < pivot){
            ++i;
            swap(nums, i, j);
        }
    }
    int pivotPos = i + 1;
    swap(nums, pivotPos, right);

    return pivotPos;
}