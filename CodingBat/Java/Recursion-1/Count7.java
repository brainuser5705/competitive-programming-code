public int count7(int n) {
    return isSeven(n, 0);
}
  
public int isSeven(int n, int count){
    if (n == 0) return count;

    if (n % 10 == 7) count++;

    return isSeven(n / 10, count);
}
  
