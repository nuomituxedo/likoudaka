int[] origin = new int[]{0,0};
int[] cur = origin.clone();
​
.equals compares reference!!!
for String, if two strings are the same, Java reuses the string object. so two same strings will always have the same references
=======
Claire's solution using HashMap
Runtime: 17 ms, faster than 7.50%
Memory Usage: 37.7 MB, less than 99.52%
​
class Solution {
public boolean judgeCircle(String moves) {
Map<Character, Integer> map = new HashMap<>();
for (char c : moves.toCharArray()){
map.put(c, map.getOrDefault(c, 0)+1);
}
//must use .equals! we are comparing Integer objects, not int!!
if (map.getOrDefault('U', 0).equals(map.getOrDefault('D',0)) && map.getOrDefault('L', 0).equals(map.getOrDefault('R', 0)))
return true;
else
return false;
}
}
========