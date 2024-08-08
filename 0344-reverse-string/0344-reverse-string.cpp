class Solution {
public:
    void reverseString(vector<char>& s) {
        int slow = 0;
        int fast = s.size() - 1;
        
        
        while(slow < fast){
            char temp = s[slow];
            s[slow] = s[fast];
            s[fast] = temp;
            
            slow++;
            fast--;
        }
    }
};