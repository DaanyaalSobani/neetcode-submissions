impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        if nums.len()==0 {
            return 0;
        }
        if nums.len()==1 {
            return 1;
        };
        let num_set: HashSet<i32> = nums.iter().cloned().collect();
        let mut longest = 0;

        for &num in &num_set {
            if !num_set.contains(&(num - 1)) {
                let mut length = 1;
                while num_set.contains(&(num + length)) {
                    length += 1;
                }
                longest = longest.max(length);
            }
        }
        longest
    }
}