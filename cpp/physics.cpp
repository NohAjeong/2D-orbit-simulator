#include <iostream>
#include <cmath>

void computeAcceleration(double x,double y,double GM, double& ax, double& ay){

    double r = sqrt(pow(x,2)+ pow(y,2));
    ax = -GM * x / pow(r,3);
    ay = -GM * y / pow(r,3);

}

int main(){

    double x = 1.0;
    double y = 0.0;
    double vx = 0.0;
    double vy = 1.5;
    const double GM = 1.0;
    double ax;
    double ay;

    computeAcceleration(x, y, GM, ax, ay);
    std::cout << "ax=" << ax << std::endl;
    std::cout << "ay=" << ay << std::endl;
    return 0;
}
