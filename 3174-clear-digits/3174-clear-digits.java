class Solution {
    public String clearDigits(String s) {
        Stack<Character> stack = new Stack<>();
        String ans = "";
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);

            if(ch>='a' && ch<='z'){
                stack.push(ch);
            }else{
                stack.pop();
            }
        }
        for(int i=0;i<stack.size();i++){
            char c = stack.get(i);
            ans += c;
        }
        return ans;
    }
}