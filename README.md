# Secure ATM System (Python):
A console-based ATM simulation built with Python that demonstrates core banking operations, authentication, transaction management, and account security features.

# Features:
Authentication:
Account number and PIN verification
Account lock after 3 failed login attempts
Exit option from login screen

# Banking Operations:
Check account balance
Deposit funds
Withdraw cash
Fund transfers between accounts
Mini statement (last 5 transactions)

# Security Features:
PIN-based authentication
Failed login tracking
Automatic account locking
Daily withdrawal limits

# Transaction Logging:
Every transaction is timestamped
Deposit history
Withdrawal history
Transfer history

# Project Structure:
atm.py
README.md
requirements.txt

# Sample Accounts:
Account	PIN	Balance
1001	1234	5000
1002	4321	10000
1003	4321	15000 (Locked)

# How to Run:
Clone Repository
git clone https://github.com/yourusername/secure-atm-system.git
cd secure-atm-system
Run Application
python atm.py

# Example Usage:
🏧 Welcome to Secure ATM System

Account number: 1001
Enter PIN: 1234

1. Balance
2. Deposit
3. Withdraw
4. Mini statement
5. Fund transfer
6. Logout
   
Security Controls:

Account Locking:
After 3 invalid PIN attempts:
Account locked due to multiple failed attempts
Daily Withdrawal Limit:
Maximum daily withdrawal:

3000

Attempting to exceed the limit:

Daily withdraw limit exceeded

Transaction History Example:
2026-11-25 11:30:14 | Deposit 500
2026-11-25 11:35:22 | Withdraw 300
2026-11-25 11:40:51 | Transferred 1000 to 1002

# Concepts Demonstrated:
Python Dictionaries
Functions
Loops
OOPS
Conditional Statements
Input Validation
Exception Prevention
State Management
Transaction Logging
Simple Banking Logic

# Future Enhancements:
SQL Database Integration
CSV Export
Admin Dashboard
Interest Calculation
Password Encryption
OTP Verification
Power BI Reporting
Account Creation Module
Persistent Transaction Storage

# Author:
Chandramohan Pokuru
Python Banking Simulation Project
