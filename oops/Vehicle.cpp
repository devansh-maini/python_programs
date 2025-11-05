#include<iostream>
using namespace std;
class vehicle
{
    private:
    char brand;
    int year;

    public:
    void input()
    {
      
        cout<<"\n Enter The Brand of Vehicle";
        cin>> brand;
        cout<< "\n Enter the manufacturing year";
        cin>> year;  
     }

     void output()
     {
     cout<< brand;
     cout<< year;
     }
       

};

int main()
{
    vehicle v1;
    v1.input();
    v1.output();
    return 0;
}