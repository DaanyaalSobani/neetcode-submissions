impl Solution {
    fn clear_count(count :&mut [u8;26]) {
        for i in (0..count.len()){
            count[i]=0;
        }
    }
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut res: HashMap<[u8;26],Vec<String>> = HashMap::new();
        let mut count = [0u8;26];
        for s in &strs {
            Solution::clear_count(&mut count);
            for c in s.bytes(){
                count[(c-b'a') as usize] += 1;
            }
            res.entry(count).or_default().push(s.clone());
        }
        res.into_values().collect()
    }
}
