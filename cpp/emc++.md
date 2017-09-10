# Item 11: Prefer deleted functions to private undefined ones
    special member functions that C++ automatically generates when they are needed:
    * Default constructor
    * Destructor
    * Copy constructor
    * Copy assignment operator
    
    Public delete function VS Private undefined function
    Non-member function
    overload:
      bool isLucky(int number);
      bool isLucky(float number) = delete;
    
    template instantiation
      template<typename T>
      void processPointer<T* ptr>;
      #include <iostream>
      #include <vector>
      using namespace std;
      template<typename T>
      void processPointer(T* ptr) {
      }

      template<typename T>
      void processPointer<void>(void* ptr) = delete;     

      int main() {
         // your code goes here
         void* x;
         processPointer(x);

         return 0;
      }

# Item 12: Declare overriding functions override
    * Base class function must be virtual
    
  

# Item 13: Prefer const_iterator to iterator
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
