impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut s_map = HashMap::new();
        let mut t_map = HashMap::new();
        for i in 0..s.len() {
            *s_map.entry(s.as_bytes()[i]).or_insert(0) += 1;
            *t_map.entry(t.as_bytes()[i]).or_insert(0) += 1;
        }
        
        return s_map == t_map;
    }
}
