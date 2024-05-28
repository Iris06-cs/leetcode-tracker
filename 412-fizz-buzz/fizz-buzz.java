class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> answer = new ArrayList<String>();
        for(int i = 1; i<= n; i++){
            String ans = getAnswer(i);
            answer.add(ans);
            
        }
        return answer;
        
    }
    private String getAnswer(int idx) {
        boolean isDivisibleBy3 = (idx % 3 == 0);
        boolean isDivisibleBy5 = (idx % 5 == 0);
        
        if(isDivisibleBy3 && isDivisibleBy5) {
            return "FizzBuzz";
        }else if(isDivisibleBy3) {
            return "Fizz";
        }else if(isDivisibleBy5) {
            return "Buzz";
        }else{
            return Integer.toString(idx);
        }
    }
}