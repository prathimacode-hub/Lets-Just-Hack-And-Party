// Happy Birthday MLH //

//Starter Codes for C++ Language//

//Hello World//

#include "stdio.h"

using namespace std;

int main()
{

	cout << "Hello World" << endl;

	system("PAUSE");

	return(0);
}


//Data Types//

#include "stdio.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{

	string hW = "Hello World";

	const string FIRST_NAME = "James";
	const string LAST_NAME = "Patterson";

	char myMiddleInitial = 'E';

	bool isEmployed = true;

	int myAge = 32;

	float myPi = 3.141592;

	const double PI = 3.1415926535;


	//Additional Data Types
		//short int : 16 bits//
		//long int  : 32 bits//
		//long long int : 64 bits//
	//*///

	cout << "Name: " << FIRST_NAME << " " << myMiddleInitial << " " << LAST_NAME << " \n" << endl;
	cout << "I am " << myAge << " years old. \n" << endl;
	if (isEmployed == 1)
	{
		cout << "It is true that I am employed. \n" << endl;
	}
	else {
		cout << "HELP ME" << endl;
	}
	cout << "One of my favorite numbers is PI: " << PI << ".\n" << endl;

	// If we need to find the size of a value
	cout << "Size of string: " << sizeof(hW) << endl;
	cout << "Size of string-first-name: " << sizeof(FIRST_NAME) << endl;
	cout << "Size of string-last-name: " << sizeof(LAST_NAME) << endl;
	cout << "Size of boolean: " << sizeof(isEmployed) << endl;
	cout << "Size of int: " << sizeof(myAge) << endl;
	cout << "Size of float: " << sizeof(myPi) << endl;
	cout << "Size of constant double: " << sizeof(PI) << endl;

	system("PAUSE");

	return(0);
}


//Array Operations//

#include "stdio.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int even[5];

	int odd[5] = { 1, 3, 5, 7, 9 };

	cout << "The first odd number: " << odd[0] << endl;

	string names[3] = { "Prathima", "Kadari", "Whatelse" };

	cout << "My name is " << names[0] << " " << names[1] << " " << names[2] << endl;

	char myCar[4][7] = { {'F', 'O', 'R', 'D'}, {'M', 'U', 'S', 'T', 'A', 'N', 'G'} };

	cout << "I am an " << myCar[0][1] << myCar[1][6] << endl;

	cout << "The old value in myCar[0][2] is " << myCar[0][2] << endl;

	myCar[0][2] = 'r';

	cout << "The new value in myCar[0][2] is " << myCar[0][2] << endl;

	system("PAUSE");

	return(0);
}

// Conditional Statements//

#include "stdio.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int largestNumber = (5 > 2) ? 5 : 2;

	cout << "Which is the largest number; 5 or 2?    " << largestNumber << endl;

	cout << "\n" << endl;

	int gradeA = 98;
	int gradeB = 90;

	int ans = (gradeA < gradeB) ? 1 : 0;

	cout << "Is the first grade higher than the second? (1 for yes, and 0 for no) " << ans << endl;

	system("PAUSE");

	return(0);
}


// IF-Else Statement//

#include "stdio.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	/*
		==	Equal to
		!=	Not Equal to
		>	Greater than
		<	Less than
		>=	Greater than or equal to
		<=	Less than or equal to
		&&	AND
		||	OR
		!	NOT
	*/

	int age = 70;
	int ageAtLastExam = 16;
	bool isNotIntoxicated = true;

	if ((age >= 1) && (age < 16))
	{
		cout << "You can't drive, mate.";
	}
	else if (!isNotIntoxicated)
	{
		cout << "You definitely cannot drive, mate." << endl;
	}
	else if (age >= 80 && ((age > 100) || ((age - ageAtLastExam) > 5)))
		cout << "You cannot drive until you take a new exam, mate." << endl;
	}
	else
	{
		cout << "You can drive, mate." << endl;
	}

	system("PAUSE");

	return(0);
}


// Functions //

#include "stdio.h"
#include <iostream>
#include <fstream>
#include <string>
//
#include <vector>

using namespace std;

void helloWorld()
{
	cout << "Hello World" << endl;
}

int addNumbers(int a = 4, int b = 21)
{
	int c = a + b;
	cout << c << endl;
	return c;
}

int addNumbers(int a, int b, int c)
{
	int d = a + b *c;
	cout << d << endl;
	return d;
}

// Here is an example of recursion within c++
int getFactorial(int a)
{
	int sum;
	if (a == 1) { sum = 1; }
	else { sum = getFactorial(a - 1)*a; }
	return sum;
}

void space()
{
	cout << "====================================" << endl;
}

void callMathFunctions()
{
	addNumbers();

	addNumbers(1, 2, 4);
}

void yourName()
{
	string response;

	cout << "what is your name? " << endl;

	getline(cin, response);

	cout << "Hello, " << response << endl;
}

int main()
{
	space();

	helloWorld();

	space();

	addNumbers();

	addNumbers(1, 2, 4);

	space();

	cout << getFactorial(3) << endl;

	space();

	callMathFunctions();

	space();

	yourName();

	system("PAUSE");

	return(0);
}



// Hope this C++ Source File helped you in getting the key concepts of basic C++ programming//

