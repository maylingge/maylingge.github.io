# enum

enum EnumTest {a=1,b=2};

int main() {

	// your code goes here
  
	cout<<sizeof(EnumTest)<<endl;  #4 
  
	cout<<a<<endl;  #1
  
	cout<<sizeof(a)<<endl; #4 
  
	enum EnumTest myenum;
  
	myenum = (EnumTest)1;
  
	cout<<myenum<<endl; #1
  
	cout<<sizeof(myenum)<<endl;  #4
  
	return 0;
  
}

#include <iostream>
using namespace std;

enum Day {One, Two};

int main() {

	// your code goes here
	int i = One;
	cout<<i<<endl;
	
	Day j = Day(2);  // (Day)2  or static_cast<Day>(2)
	cout<<j<<endl;
	return 0;
}



# #define


# const

# virtual & pure virtual
	
	virtual ~abstract() = 0;
	abstract::~abstract() {}
	
	
	Invoked in order:
	Base::Constructor()
	Derived::Constructor()
	
	Derived::Destructor()
	Base::Destructor()
	
	base class's default constructor/destructor is called by default from Derived class
