#include<iostream>

using namespace std;

int main()
{
    int I;
    while (true){
        cout<<"\nGuess the number: ";
        cin>>I;
        if (I == 5){
            cout<<"\nYou won!";
        } else {
            cout<<"You Lose!!!!!";
        }
    }
}
