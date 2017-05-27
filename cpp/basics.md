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

# #define


# const
