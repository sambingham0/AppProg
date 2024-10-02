#include <iostream>
#include <fstream>   // for file operations
#include <limits>    // for std::numeric_limits
#include <string>    // for std::string

using namespace std;

// Function declarations
void showMenu();
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);
void writeToFile(const string& data);
void showHistory();
double getNumber(const string& prompt); // New function for input validation

int main() {
    double num1, num2, result;
    char operation;
    bool running = true;

    while (running) {
        showMenu();
        cout << "Enter your choice (or 'q' to quit, 'h' to show history): ";
        cin >> operation;

        if (operation == 'q') {
            running = false;
            continue;
        } else if (operation == 'h') {
            showHistory();
            continue;
        }

        // Use the new getNumber function for input validation
        num1 = getNumber("Enter first number: ");
        num2 = getNumber("Enter second number: ");

        string calculation;
        switch (operation) {
            case '+':
                result = add(num1, num2);
                calculation = to_string(num1) + " + " + to_string(num2) + " = " + to_string(result);
                cout << "Result: " << result << endl;
                break;
            case '-':
                result = subtract(num1, num2);
                calculation = to_string(num1) + " - " + to_string(num2) + " = " + to_string(result);
                cout << "Result: " << result << endl;
                break;
            case '*':
                result = multiply(num1, num2);
                calculation = to_string(num1) + " * " + to_string(num2) + " = " + to_string(result);
                cout << "Result: " << result << endl;
                break;
            case '/':
                if (num2 != 0) {
                    result = divide(num1, num2);
                    calculation = to_string(num1) + " / " + to_string(num2) + " = " + to_string(result);
                    cout << "Result: " << result << endl;
                } else {
                    calculation = "Error: Division by zero is a no no!";
                    cout << calculation << endl;
                }
                break;
            default:
                calculation = "Invalid operation.";
                cout << calculation << endl;
                break;
        }

        // Write the calculation or error to the file
        writeToFile(calculation);
    }

    cout << "Goodbye!" << endl;
    return 0;
}

// Function to display the menu
void showMenu() {
    cout << "\nSam's Calculator\n";
    cout << "Choose an operation:\n";
    cout << "+ : Addition\n";
    cout << "- : Subtraction\n";
    cout << "* : Multiplication\n";
    cout << "/ : Division\n";
    cout << "h : Show history\n";
    cout << "q : Quit\n";
}

// Function definitions for arithmetic operations
double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    return a / b;
}

// Function to write data to a file
void writeToFile(const string& data) {
    ofstream file("calculator_history.txt", ios::app);  // Open file in append mode
    if (file.is_open()) {
        file << data << endl;  // Write the calculation result to the file
        file.close();
    } else {
        cout << "Unable to open file for writing." << endl;
    }
}

// Function to display calculation history from the file
void showHistory() {
    ifstream file("calculator_history.txt");
    string line;

    if (file.is_open()) {
        cout << "\nCalculation History:\n";
        while (getline(file, line)) {
            cout << line << endl;  // Print each line from the file
        }
        file.close();
    } else {
        cout << "No history found or unable to open file." << endl;
    }
}

// Function to get a valid number from user input
double getNumber(const string& prompt) {
    double num;
    cout << prompt;
    while (!(cin >> num)) {
        cout << "Invalid input. Please enter a number: ";
        cin.clear();  // clear the error flag
        cin.ignore(numeric_limits<streamsize>::max(), '\n');  // discard invalid input
    }
    return num;
}