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

        buckets
            .into_iter()           // consume buckets
            .rev()                 // go from highest freq to lowest
            .flat_map(|v| v.into_iter()) // flatten Vec<Vec<i32>> -> Vec<i32>
            .take(k as usize)      // only keep top k
            .collect()             // collect into Vec<i32>
    }
}
