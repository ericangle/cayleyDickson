#include<vector>
#include<iostream>
using namespace std;

class algebra {

  private:

    algebra* a1;
    algebra* a2;
    int rank;
    double real;

  public:

    algebra(vector<double> input) {
      rank = input.size();
      if (rank == 1) {
        real = input.at(0);
      }
      else {
        vector<double> tempA1(input.begin(),input.begin()+input.size()/2);
        vector<double> tempA2(input.begin()+input.size()/2,input.end());
        a1 = new algebra(tempA1);
        a2 = new algebra(tempA2);
      }
    }

    algebra* getA1() {return a1;}
    algebra* getA2() {return a2;}
  
    void print() {
      if (rank == 1) {
        cout << real << endl;
      }
      else {
        a1->print();
        a2->print();
      }
    }

    // For now, we are going to assume that we will perform
    // these operations between numbers of the same rank, as
    // we are calling it. We will change this later.

/*
    // Conjugation
    // (a,b)* = (a*,-b)
    void conj() {
      if (rank != 1) {
        a1->conj();
        vector<double> minusOne;
        minusOne.push_back(-1.0);
        for (int i = 1; i < rank; i++) {
          minusOne.push_back(0.0);
        }
        a2->mult(new algebra(minusOne));
      }
    }

    // Multiplication
    // (a,b)(c,d) = (ac-db*,a*d+bc)
    void mult(algebra* a) {

      if (rank != 1) {
        a1->conj();
        vector<double> minusOne;
        minusOne.push_back(-1.0);
        for (int i = 1; i < rank; i++) {
          minusOne.push_back(0.0);
        }
        a2->mult(new algebra(minusOne));
      }
    }
*/
    // Addition
    // (a,b) + (c,d) = (a+c,b+d)
    void add(algebra* in) {
      if (rank == 1) {
        real = real + in->real;
      }
      else {
        a1->add(in->getA1());
        a2->add(in->getA2());
      }
    }

};
