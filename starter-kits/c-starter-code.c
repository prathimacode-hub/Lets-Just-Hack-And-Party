// Happy Birthday MLH //

//Starter Codes for C Language//

//Hello World"

#include <stdio.h>
int main() {
   printf("Hello, World!");
   return 0;
}


//Basic Concepts//

#include <stdio.h>

int main() {
    char str[100];
    double i;

    printf("Enter a value: ");
    scanf("%lf %s", &i, str);
    printf("\nYou entered: %lf %s\n", i, str);
    return 0;
}

//Basic Data Types//

#include <stdbool.h>

int main() {
    float jason = 23.333f;
    long double jason2 = 55.55555555555l;
    _Bool boolVariable = 1;
    // with C99
    bool boolean = true;

    enum primaryColor {
        red, green, blue
    };

    enum direction {
        up, // 0
        down, // 1
        left = 10, // 10
        right // 11
    };

    enum primaryColor g = red;
    char six = '6';

    bool isRed = g == red;

    return 0;
}

//Basic Operators

#include <stdio.h>

int main() {
    printf("Byte size of 'int': %lu\n"
           "Byte size of 'char': %lu\n"
           "Byte size of 'long': %lu\n"
           "Byte size of 'long long': %lu\n"
           "Byte size of 'double': %lu\n"
           "Byte size of 'long double': %lu\n",
           sizeof(int), sizeof(char), sizeof(long), sizeof(long long), sizeof(double), sizeof(long double));

    return 0;
}


//Factorial of a Number//

#include <stdio.h>

//complete the function below
int findFactorial(int number)
{

}

int main()
{
  int number;
  scanf("%d",&number);
  printf("%d",findFactorial(number));
  return 0;
}



//Generate Prime Numbers//

#include <stdio.h>
#include <stdbool.h>

int main() {
    int primes[50] = {2, 3};
    int primeIndex = 2;

    bool isPrime;

    for (int i = 5; i <= 100; i += 2) {
        isPrime = true;
        for (int j = 1; isPrime && i / primes[j] >= primes[j]; j++) {
            if (i % primes[j] == 0) {
                isPrime = false;
            }
        }
        if (isPrime) {
            primes[primeIndex++] = i;
        }
    }

//    const int limit = sizeof primes / sizeof(int); // limit in loops
    int spaceLimit = primeIndex - 1;
    for (int i = 0; i < primeIndex; i++) {
        printf("%d%s", primes[i], i != spaceLimit ? ", " : "\n");
    }

    return 0;
}



//Weather Program//

#include <stdio.h>

#define MONTHS 12
#define YEARS 5

int main() {
    const float rainfall[YEARS][MONTHS] = {
            {4.3f, 4.3f, 4.3f, 3.0f, 2.0f, 1.2f, 0.2f, 0.2f, 0.4f, 2.4f, 3.5f, 6.6f},
            {8.5f, 8.2f, 1.2f, 1.6f, 2.4f, 0.0f, 5.2f, 0.9f, 0.3f, 0.9f, 1.4f, 7.3f},
            {9.1f, 8.5f, 6.7f, 4.3f, 2.1f, 0.8f, 0.2f, 0.2f, 1.1f, 2.3f, 6.1f, 8.4f},
            {7.2f, 9.9f, 8.4f, 3.3f, 1.2f, 0.8f, 0.4f, 0.0f, 0.6f, 1.7f, 4.3f, 6.2f},
            {7.6f, 5.6f, 3.8f, 2.8f, 3.8f, 0.2f, 0.0f, 0.0f, 0.0f, 1.3f, 2.6f, 5.2f}
    };

    int year, month;
    float subtotal, total;

    printf(" YEAR\t\tRAINFALL  (inches)\n");

    for (year = 0, total = 0; year < YEARS; year++) {
        for (month = 0, subtotal = 0; month < MONTHS; month++) {
            subtotal += rainfall[year][month];
        }
        printf("%5d \t%15.1f\n", 2010 + year, subtotal);
        total += subtotal;
    }

    printf("\nThe yearly average is %.1f inches.\n\n"
           "MONTHLY AVERAGES:\n\n"
           " Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec\n", total / YEARS);

    for (month = 0; month < MONTHS; month++) {
        for (year = 0, subtotal = 0; year < YEARS; year++) {
            subtotal += rainfall[year][month];
        }
        printf("%4.1f ", subtotal / YEARS);
    }
    printf("\n");

    return 0;
}

//Functions//

void foo() {

}

int main() {
    foo();

    return 0;
}


//Practicing Functions

void foo() {

}

int main() {
    foo();

    return 0;
}


//String Functions//


#include <stdio.h>

#define MONTHS 12
#define YEARS 5

int main() {
    const float rainfall[YEARS][MONTHS] = {
            {4.3f, 4.3f, 4.3f, 3.0f, 2.0f, 1.2f, 0.2f, 0.2f, 0.4f, 2.4f, 3.5f, 6.6f},
            {8.5f, 8.2f, 1.2f, 1.6f, 2.4f, 0.0f, 5.2f, 0.9f, 0.3f, 0.9f, 1.4f, 7.3f},
            {9.1f, 8.5f, 6.7f, 4.3f, 2.1f, 0.8f, 0.2f, 0.2f, 1.1f, 2.3f, 6.1f, 8.4f},
            {7.2f, 9.9f, 8.4f, 3.3f, 1.2f, 0.8f, 0.4f, 0.0f, 0.6f, 1.7f, 4.3f, 6.2f},
            {7.6f, 5.6f, 3.8f, 2.8f, 3.8f, 0.2f, 0.0f, 0.0f, 0.0f, 1.3f, 2.6f, 5.2f}
    };

    int year, month;
    float subtotal, total;

    printf(" YEAR\t\tRAINFALL  (inches)\n");

    for (year = 0, total = 0; year < YEARS; year++) {
        for (month = 0, subtotal = 0; month < MONTHS; month++) {
            subtotal += rainfall[year][month];
        }
        printf("%5d \t%15.1f\n", 2010 + year, subtotal);
        total += subtotal;
    }

    printf("\nThe yearly average is %.1f inches.\n\n"
           "MONTHLY AVERAGES:\n\n"
           " Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec\n", total / YEARS);

    for (month = 0; month < MONTHS; month++) {
        for (year = 0, subtotal = 0; year < YEARS; year++) {
            subtotal += rainfall[year][month];
        }
        printf("%4.1f ", subtotal / YEARS);
    }
    printf("\n");

    return 0;
}


// Hope this C Source File helped you in getting the key concepts of basic C programming//

