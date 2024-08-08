#include <iostream>
using namespace std;

int main() {
    int locks, stocks, barrels, t_sales;
    float commission;
    
    cout << "Locks: ";
    cin >> locks;
    
    cout << "Stocks: ";
    cin >> stocks;
    
    cout << "Barrels: ";
    cin >> barrels;
    
    if ((locks < 0 || locks > 70) || (stocks < 0 || stocks > 80) || (barrels < 0 || barrels > 90)) {
        if (locks == -1) {
            cout << "Terminate program" << endl;
        } else {
            cout << "Invalid input" << endl;
        }
    } else {
        t_sales = (locks * 45) + (stocks * 30) + (barrels * 25);
        
        if (t_sales <= 1000) {
            commission = 0.10 * t_sales;
        } else if (t_sales <= 1800) {
            commission = 0.10 * 1000;
            commission += 0.15 * (t_sales - 1000);
        } else {
            commission = 0.10 * 1000;
            commission += 0.15 * 800;
            commission += 0.20 * (t_sales - 1800);
        }
        
        cout << "The total sales is " << t_sales << endl;
        cout << "The commission is " << commission << endl;
    }
    
    return 0;
}
