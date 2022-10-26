public class SumDigits {
    public int sumDigits(int n) {
  
        return addNums(n, 0);
    
    }
    
    public int addNums(int n, int sum){
    
        if (n == 0) return sum;
        
        return addNums(n / 10, sum + n % 10);
    }
}
