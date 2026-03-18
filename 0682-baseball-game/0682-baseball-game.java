class Solution {
    public int calPoints(String[] op) {
        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < op.length; i++){
            if(op[i].equals("C")){
                stack.pop();
            }
            else if(op[i].equals("D")){
                stack.push(stack.peek()*2);
            }
            else if(op[i].equals("+")){
                int t = stack.pop();
                int sum = t + stack.peek();
                stack.push(t);
                stack.push(sum);
            }
            else{
                stack.push(Integer.parseInt(op[i]));
            }
        }
        int s = 0;
        for(int i = 0; i < stack.size(); i++){
            s += stack.get(i);
        }
        return s;
    }
}