public int powerN(int base, int n) {
  
    return powerNRecursive(base, 1, n);

}

public int powerNRecursive(int base, int total, int n){

    if (n == 0) return total;
    return powerNRecursive(base, total * base, n-1);

}