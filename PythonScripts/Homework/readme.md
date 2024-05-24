# Homework Scripts

This directory contains various Python scripts for different assignments and exercises.

## Files

> [!WARNING]
> The script descriptions are written by AI and have a high chance of containing errors. Please read them with a grain of salt.

1. **Secret Key from M (kth).py**
   - **Description:**  Generates a secret code based on a secret key and a string manipulation formula.
      ```markdown
      # Secret Code Generator
      
      This Python script generates a secret code based on user input.
      
      ## Description
      
      The script takes a secret key as input and generates a secret code using a mathematical formula. It then extracts two characters from the generated string and combines them to form the secret code.
      
      ## Usage
      
      1. Run the script.
      2. Input your secret key when prompted.
      3. The script will calculate the secret code based on the input key and display it.

      ```

2. **altsum.py**
   - **Short Description:** Computes the alternating sum of a list, with user input to build the list.
      ```markdown
      # Alternate Sum Script
      
      This Python script calculates the alternate sum of a list of integers. 
      
      ## Description
      
      The `altsum` function takes a list of integers as input and returns the sum of the list with alternating signs. For example, given the input `[1, 2, 3, 4, 5]`, the function would calculate `1 + 2 - 3 + 4 - 5`.
      
      The script prompts the user to input a series of numbers until the user types 'Done'. It then applies the `altsum` function to the input list and prints the result.
      
      ## Usage
      
      1. Run the script.
      2. Input integers when prompted.
      3. Type 'Done' when finished entering numbers.
      4. The script will display the alternate sum of the entered numbers.
      
      ## Example
      
      ```python
      Type a number (or 'Done' to stop): 1
      Type a number (or 'Done' to stop): 2
      Type a number (or 'Done' to stop): 3
      Type a number (or 'Done' to stop): 4
      Type a number (or 'Done' to stop): 5
      Type a number (or 'Done' to stop): Done
      Output: -1

      ```

3. **digit.py**
   - **Description:** Computes the kth digit of a number in a specified base, utilizing only if statements
      ```markdown
      # Kth Digit Calculator
      
      This Python script calculates the kth digit of a number in a given base.
      
      ## Description
      
      The script defines a function `kthDigit(x, b, k)` that calculates the kth digit of a number 'x' in base 'b' at 'k' location. 
      
      ## Usage
      
      1. Run the script.
      2. Input the values for 'x', 'b', and 'k' when prompted.
      3. The script will calculate and display the kth digit of the number 'x' in base 'b'.

      ```

4. **happy.py**
   - **Description:** A script to find the k-th happy number, check if a number is a happy number, or quit the script based on user input.
      ```markdown
      # Happy Number Checker
      
      This Python script allows users to find happy numbers and check if a given number is happy.
      
      ## Description
      
      The script defines several functions:
      - `sumOfDigitsSquared(n)`: Calculates the sum of the squared digits of a number 'n'.
      - `isHappy(n)`: Checks if a number 'n' is happy by repeatedly calculating the sum of the squared digits until the result is 1 (happy) or 4 (unhappy).
      - `listOfHappy(index)`: Generates a list of happy numbers up to a given index.
      
      The script prompts users to choose from the following options:
      - Find the kth happy number.
      - Check if a number is a happy number.
      - Quit the script.
      
      ## Usage
      
      1. Run the script.
      2. Choose an option by typing 'K' to find the kth happy number, 'H' to check if a number is happy, or 'Q' to quit.
      3. Follow the prompts to input values or numbers as required.
      4. The script will display the result accordingly.
      ```
     
5. **isItNegetive.py**
   - **Description:** Evaluates if either input numbers are negative based on user-defined conditions.
      ```markdown
      # Negative Number Checker
      
      This Python script checks if at least one of two numbers is negative based on user input.
      
      ## Description
      
      The script takes two integers 'a' and 'b' as input and checks if at least one of them is negative. It also allows users to specify whether they want to consider zero as a negative number.
      
      ## Usage
      
      1. Run the script.
      2. Input two integers 'a' and 'b'.
      3. Specify whether to consider zero as a negative number by typing 'True' or 'False' when prompted.
      4. The script will determine if at least one of the input numbers is negative and display the result.

      ```

6. **meow.py**
   - **Description:** Detects if there might be trouble based on the hour, minute, and whether there is meowing, according to predefined conditions.
      ```markdown
      # Cat Trouble Checker
      
      This Python script checks if a cat is causing trouble based on the time and whether it's meowing.
      
      ## Description
      
      The script takes input for the hour, minute, and whether the cat is meowing. It then determines if the cat is causing trouble based on the following conditions:
      - If it's past 9 PM and the cat is meowing.
      - If it's before 6:30 AM and the cat is meowing.
      
      ## Usage
      
      1. Run the script.
      2. Input the hour and minute.
      3. Specify whether the cat is meowing by typing 'True' or 'False' when prompted.
      4. The script will determine if the cat is causing trouble and display the result.

      ```

7. **sansprimes.py**
   - **Description:** A script to check for prime numbers in a list of user-provided numbers and return both the remaining unchecked numbers and their prime status.
      ```markdown
      # Prime Number Checker
      
      This Python script checks for prime numbers in a list of integers provided by the user.
      
      ## Description
      
      The script includes two functions:
      - `fuc_is_prime(unchecked)`: Checks for prime numbers in a list of integers and returns the list of remaining unchecked numbers along with their prime status.
      - `collect_Input()`: Collects user input for the list of numbers to check for prime.
      
      ## Usage
      
      1. Run the script.
      2. Type as many numbers as desired to check for prime.
      3. Type 'DONE' when finished entering numbers.
      4. The script will display the remaining unchecked numbers and their prime status.

      ```

8. **triangle.py**
   - **Description:** Generates triangle or diamond patterns based on user input, with loading animation.
      ```markdown
      # Triangle Pattern Generator

      This Python script provides functions to generate triangle patterns based on user input.
      
      ## Description
      
      The script defines two functions:
      - `star(k)`: Generates the top part of a triangle pattern with a specified height 'k'.
      - `upside_down_star(k)`: Generates the bottom part of a triangle pattern with a specified height 'k'.
      
      Users can input a positive integer 'k' to generate the top part of the triangle, a negative integer 'k' to generate the bottom part, or 'dia' to generate a diamond  pattern combining both parts.
      
      ## Usage
      
      1. Import the script into your Python environment.
      2. Call the `star(k)` function with a positive integer 'k' to generate the top part of the triangle.
      3. Call the `upside_down_star(k)` function with a negative integer 'k' to generate the bottom part of the triangle.
      4. For a diamond pattern, call both functions with the same positive integer 'k'.
         

      ```

2. **altsum.py**
   - idk
      ```markdown
      # Multiples Checker
      
      This Python script checks if all elements in a user-provided list are multiples of a specified integer `k`.
      
      ## Description
      
      The script defines a function `allMultiplesOfK(k, lst)` that checks if all elements in the list `lst` are multiples of `k`. It then collects user input to build the list and checks the condition using the function.
      
      ## Usage
      
      1. Run the script.
      2. Input the integer `k` when prompted.
      3. Input multiple numbers to build the list `lst`. Type 'Done' when finished.
      4. The script will check if all elements in the list are multiples of `k` and display the result.
      ```

## Usage
To run any of these scripts, use the following command:

```bash
python filename.py
