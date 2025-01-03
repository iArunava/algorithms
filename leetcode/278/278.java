public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int l = 0;
        int r = n;
        while (l < r) {
            final int m = l + (r - l) / 2;
            final boolean check = isBadVersion(m);
            if (!check) {
                l = m+1;
            } else {
                r=m;
            }
         }
         return l;
    }
}
