impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut count = HashMap::new();
        let mut buckets: Vec<Vec<i32>> = vec![Vec::new(); nums.len()+1];
        for num in nums{
            *count.entry(num).or_insert(0) += 1
        }
        for (num,freq) in count {
            println!("{:?},{:?}",num,freq);
            buckets[freq].push(num);
        }
        println!("{:?}",buckets);

        let mut result: Vec<i32>= Vec::new();
        for f_list in buckets.into_iter().rev() {
            for num in f_list {
                result.push(num);
                if result.len() == k as usize{
                    return result;
                }
            }
        }

        return result;
    }
}
