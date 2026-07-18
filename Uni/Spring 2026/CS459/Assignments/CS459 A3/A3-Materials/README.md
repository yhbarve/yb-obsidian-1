# Folder Structure

- **Q5/** : Contains the content required for implementation of question 5.
  - **./A3Q5.py**  
    - Template file for Question 5.  
    - Follow the comments within the file:  
      - It is recommended not to modify sections explicitly marked as "Do Not Edit."  
      - You are recommended to only implement the TODO sections as instructed in the skeleton code.  
    - Most of the code is pre-written to guide you through the structure.  
  - **./fraudulent.csv**
    - Sample of fraudulent transactions for (5b)
  - **./transactions.csv**
    - Dataset of transactions
- **Q6/**: Contains the content required for implementation of question 6.
  - **./A3Q6.py**  
    - Template file for Question 6.  
    - Follow the comments within the file:  
      - You are recommended to only implement the sections that are indicated in the assignment instruction PDF.
    - Don't forget to fill in the report `<watiam-id>_approach.txt`
    - Most of the code is pre-written to guide you through the structure.  
  - **./final_dataset_membership.csv**
    - Dataset for Q6
  - **./trained_model.pth**
    - a trained model file


- **README.md**  
  - Provides an overview of the project and setup instructions.

---

# Preparing the Environment

## Installing Python  
The provided templates were created using `Python 3.10.6`, but any relatively recent version of Python 3 should work fine.  

If you don’t have Python 3 installed, make sure to install it before proceeding.  

## Installing Packages  
Ensure **Pandas** and **PyTorch** (for Q6) are installed before running the scripts:  

```bash
pip install pandas torch
```
All other required packages are built-in and do not require installation.  

## Making Scripts Executable  
To grant execution permissions to your scripts, run:  

  ```bash
  chmod +x ./A3Q5.py
  ```
> **Note:** Depending on your operating system, you may need to adjust the permission settings using different methods.  

# Q5 Code Evaluation
- For A3Q5 run the `unit_tests` function with the required input parameters to check if your implementation is correct. This will verify whether your implementation meets the expected outcomes.

> **NOTE:** These tests only validate certain criteria and indicate whether they are satisfied or not. However, passing all these tests does not guarantee that your code is fully functional. Always verify with the `Test Cases` below to ensure correctness.

## Test Cases

This table contains pre-filled values to help you compare your code’s performance with the expected implementation. You should not modify this table.
**Notes:** 
- Number of Blocks Mined does not include the Genesis block
- "First Block" refers to the block after the Genesis block (the Genesis block always has nonce 1)

| Command | # of Blocks Mined | Hash of Last Block | Nonce of First Block |
|---------|-------------------|--------------------|----------------------|
| `A3Q5.py hasher666 ./transactions.csv 5 2000` | 377 | 000da | 2084 |
| `A3Q5.py hasher666 ./transactions.csv 6 9000` | 68 | 00004b | 64174 |
| `A3Q5.py hasher666 ./transactions.csv 7 57000` | 10 | 0000048 | 671048 |
