#include <iostream>
#include <iomanip>

// Function to check if a year is a leap year
bool isLeapYear(int year) {
    return (year % 400 == 0 || (year % 100 != 0 && year % 4 == 0));
}

// Function to get the number of days in a month
int getDaysInMonth(int month, int year) {
    switch (month) {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            return 31;
        case 4: case 6: case 9: case 11:
            return 30;
        case 2:
            return isLeapYear(year) ? 29 : 28;
        default:
            return 0;  // Invalid month
    }
}

int main() {
    int d, m, y;
    
    // Input date
    std::cout << "Enter the date (DD MM YYYY): ";
    std::cin >> d >> m >> y;
    
    // Validate input
    if (y < 1812 || y > 2012 || m < 1 || m > 12 || d < 1 || d > getDaysInMonth(m, y)) {
        std::cout << "Invalid input\n";
        return 1;  // Exit with an error code
    }

    // Calculate the next day's date
    int nd = d + 1;
    int nm = m;
    int ny = y;
    
    if (nd > getDaysInMonth(m, y)) {
        nd = 1;
        nm++;
        if (nm > 12) {
            nm = 1;
            ny++;
        }
    }
    
    // Output the result
    std::cout << "Given date is " << std::setw(2) << std::setfill('0') << d << "/"
              << std::setw(2) << std::setfill('0') << m << "/"
              << std::setw(4) << y << std::endl;
    std::cout << "Next day's date is " << std::setw(2) << std::setfill('0') << nd << "/"
              << std::setw(2) << std::setfill('0') << nm << "/"
              << std::setw(4) << ny << std::endl;
    
    return 0;  // Exit successfully
}
