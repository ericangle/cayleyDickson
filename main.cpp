// g++ main.cpp -o executable_name

#include "algebra.cpp"
#include <vector>
using namespace std;

int main() {

  vector<double> input1;
  input1.push_back(1.0);
  input1.push_back(2.0);

  vector<double> input2;
  input2.push_back(5.0);
  input2.push_back(1.0);

  // there should be a check in constructor
  // for 2^n elements
  algebra* A1 = new algebra(input1);
  algebra* A2 = new algebra(input2);

  cout << "(1,2):" << endl;
  A1->print();
  cout << "(5,2):" << endl;
  A2->print();
  cout << "(1,2) + (5,1):" << endl;
  A1->add(A2); 
  A1->print();
  return 0;

}
