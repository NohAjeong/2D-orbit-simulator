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
    const double dt = 0.05;


    computeAcceleration(x, y, GM, ax, ay);
    double vx_half = vx + ax * (dt/2.0);
    double vy_half = vy + ay * (dt/2.0);
    x = x + vx_half * dt;
    y = y + vy_half * dt;   

    double ax_new;
    double ay_new;
    computeAcceleration(x, y, GM, ax_new, ay_new);
    vx = vx_half + ax_new * (dt/2.0);
    vy = vy_half + ay_new * (dt/2.0);

    std::cout << "x=" << x << ", y=" << y << std::endl;
    std::cout << "vx=" << vx << ", vy=" << vy << std::endl;
    return 0;
}
