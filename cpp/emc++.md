# Item 11: Prefer deleted functions to private undefined ones
    special member functions that C++ automatically generates when they are needed:
    * Default constructor
    * Destructor
    * Copy constructor
    * Copy assignment operator
    
  **Public delete function VS Private undefined function**
    
    Non-member function
    
  **overload:**
      
    #include <iostream>
    using namespace std;

    bool isLucky(int number) {
        std::cout<<number<<std::endl;
        return true;
    }

    bool isLucky(char) = delete;

    int main() {
        // your code goes here
        isLucky('a');

        return 0;
    }
    
   **template instantiation**
      
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
    class Base {
    public:
      virtual void mf1() const ;


    };

    class Derived {
    public:
      void mf1() const override;	

    };
  
    An lvalue (locator value) represents an object that occupies some identifiable location in memory (i.e. has an address).

    rvalues are defined by exclusion, by saying that every expression is either an lvalue or an rvalue. Therefore, from the above  definition of lvalue, an rvalue is an expression that does not represent an object occupying some identifiable location in memory.
    
    Not all lvalues can be assigned to.
    
    rvalue reference VS lvalue reference
    int a = 1;
    int& b = a;
    int& c = 1; //error
    const int& d = 1;
    int&& e = 1;
    
    An expression is an rvalue if it results in a temporary object 
    In C++03, there was a costly and unnecessary deep copies that can happen implicitly when objects are passed by value. We can avoid the performance hit due to deep copy by using a rvalue reference.
    
    A& operator=(A&& other) noexcept
    {
      mData =  other.mData;
      other.mData = nullptr;
      return *this;
    }

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

# Item 31 lambda: Avoid default capture mode
    lambda expression:
    构造闭包：能够捕获作用域中变量的无名函数对象。
    [ captures ] ( params ) { body }
    capture by reference
    capture by value
    [a,&b] 其中 a 以复制捕获而 b 以引用捕获。
    [this] 以引用捕获当前对象（ *this ）
    [&] 以引用捕获所有用于 lambda 体内的自动变量，并以引用捕获当前对象，若存在
    [=] 以复制捕获所有用于 lambda 体内的自动变量，并以引用捕获当前对象，若存在
    [] 不捕获
    
    #include <iostream>
    using namespace std;

    class Widget {
    public:
       Widget(int d): divisor(d) {};

       void compare(int x) ;

    private:
       int divisor;

    };

    void Widget::compare(int x) {
        auto f = [] (int x) {return x > divisor;};
        std::cout<<f(x)<<std::endl;
    }
    int main() {
        // your code goes here
        Widget w(10);
        w.compare(5);
        w.compare(11);

        return 0;
    }
