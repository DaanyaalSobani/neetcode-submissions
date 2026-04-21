impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        
        let mut s_map = HashMap::new();
        let mut t_map = HashMap::new();
        
        for (sc, tc) in s.chars().zip(t.chars()) {
            *s_map.entry(sc).or_insert(0) += 1;
            *t_map.entry(tc).or_insert(0) += 1;
        }
        
        return s_map == t_map;
    }

}
