class Solution {
    Map<Integer,Integer> dict = new HashMap<>();
    public int fib(int n) {

        if(dict.containsKey(n)){
            return dict.get(n);
        }
        if (n == 0){
            return 0;
        }
        if(n <= 2){
            return 1;
        }
        int val = fib(n-1)+fib(n-2);
        dict.put(n,val);
        return val;
    }
}