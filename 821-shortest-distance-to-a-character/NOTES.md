7.15
class Solution:
def shortestToChar(self, s: str, c: str) -> List[int]:
chars = list(s)
res = []
last_c = 0
for i in range(0, len(chars)):
res.append(len(chars))
for i in range(0, len(chars)):
if chars[i] == c:
for j in range (last_c, i):
res[j] = min(res[j], i-j)
last_c = i
for j in range (i, len(chars)):
res[j] = j - i
return res
//Claire's solution 9.23.2019
​
class Solution {
public int[] shortestToChar(String S, char C) {
int[] dists = new int[S.length()];
Arrays.fill(dists, Integer.MAX_VALUE);
for (int i = 0; i < S.length(); i++){
if(S.charAt(i) == C){
for (int j = i; j >= 0; j--){
if (dists[j] > i-j)
dists[j] = i-j;
else
break;
}
for (int k = i; k< dists.length; k++){
dists[k] = k - i;
}
}
}
return dists;
}
}