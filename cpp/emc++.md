# Prefer const_iterator to iterator
[link to vector reference](http://www.cplusplus.com/reference/vector/vector/insert/)

_There is no simple way to get a const_iterator from a non-const container_ ??
_C++11 vector insert uses const_iterator as the input position_ ??
_how to implement a non-member version of cbegin, cend_ ??

    typedef value_type* iterator;                     
    typedef const value_type* const_iterator;    


    #include <iostream>
    #include <vector
    using namespace std;

    int main() {
      // your code goes here
      vector<int> v = { 1,2,3};
      for(vector<int>::const_iterator it=v.begin();it!=v.end();++it) {
      std::cout<<*it<<std::endl;
      }
      return 0;
    }
