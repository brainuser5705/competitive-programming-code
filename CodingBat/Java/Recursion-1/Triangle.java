package CodingBat;

public class Triangle {
    

    public int triangle(int rows) {
  
        int count = 0;
        for (int i = 1; i <= rows; i++){
          count += i;
        }
        return count;
        
    }

    public int triangleRecursive(int rows) {
  
        if (rows == 0){
          return 0;
        }else{
          return rows + triangle(rows-1);
        }
        
    }
      

}
