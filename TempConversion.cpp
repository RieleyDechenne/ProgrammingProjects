#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double temp;
    char unit;

    cout << "****** Temperature Conversion ******" << endl;
    cout << "F = Fahrenheit" << endl;
    cout << "C = Celsius" << endl;
    cout << "What unit would you like to convert to: " << endl;
    cin >> unit;

    if (unit == 'F' || unit == 'f') {
        cout << "enter the temperature in celsius: " << endl;
        cin >> temp;

        temp = (1.8 * temp) + 32.0;
        cout << fixed << setprecision(2) << "Temperature is: " << temp << " F°" << endl;
    }
    else if (unit == 'C' || unit == 'c') {
        cout << "Enter the temperature in fahrenheit: " << endl;
        cin >> temp;

        temp = (temp - 32) / 1.8;
        cout << fixed << setprecision(2) << "Temperature is: " << temp << " C°" << endl;
    }
    else{
        cout << "Please enter only C or F" << endl;
    }

    cout << "*************************************" << endl;
    return 0;
}