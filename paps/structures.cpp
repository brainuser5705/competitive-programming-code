#include <iostream>

using namespace std;

struct Point{
    double x;
    double y;
};

struct PointWithConstructor{
    double x;
    double y;

    PointWithConstructor(double theX, double theY){
        x = theX;
        y = theY; // can't use `this`
    }

    // const keyword because we are not modifying the member variables
    PointWithConstructor mirror() const{
        return PointWithConstructor(x, -y);
    }

};

int main(){
    Point origin; // create an instance wit its out copy of member variables
    origin.x = 0;
    origin.y = 0;

    PointWithConstructor p(4,2);
    // can also be constructed ourside of a variable declaratoin
    p = PointWithConstructor(4,2);

}
