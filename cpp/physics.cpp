#include <iostream>
#include <cmath>

int main(){

    double x = 1.0;
    double y = 0.0;
    double vx = 0.0;
    double vy = 1.5;
    const double GM = 1.0;

    double r = sqrt(pow(x,2)+ pow(y,2));
    double ax = -GM * x / pow(r,3);
    double ay = -GM * y / pow(r,3);

    std::cout << "ax=" << ax << std::endl;
    std::cout << "ay=" << ay << std::endl;

    return 0;
}
