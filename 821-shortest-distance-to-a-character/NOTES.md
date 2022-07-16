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