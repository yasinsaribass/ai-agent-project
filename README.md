# AI Agent Study Assistant

## Step 1 – System Design

### System Description
This project aims to develop an AI-based study assistant using Python. The system will receive user input, process it, and generate meaningful responses. It will also use external tools such as a calculator.

### AI / Agent Approach
The system is implemented as a single intelligent agent. The agent analyzes user input and decides whether to respond directly or use a tool.

### Tools Used
- Calculator tool
- Text processing

### Programming Concepts
- Functions
- Classes (OOP)
- Conditionals
- Loops
- Error handling

## Step 3 – Testing and Deployment

### Testing Process
The system was tested continuously during the development phase to ensure that each component works correctly.

The testing focused on verifying the main workflow of the system, including user input handling, agent decision-making, and tool usage. The calculator tool was tested separately to ensure it correctly evaluates mathematical expressions.

Additionally, input validation and error handling were tested to make sure the system does not crash when invalid or unexpected input is provided.

---

### Test Scenarios

Several test scenarios were used to validate the system:

1. Mathematical Calculation  
Input: 5+3  
Expected Output: 8  
Explanation: The agent detects numbers and uses the calculator tool.

2. Text Input  
Input: hello  
Expected Output: I am a simple AI assistant. You said: hello  
Explanation: The agent returns a normal response without using tools.

3. Invalid Calculation  
Input: 5/0  
Expected Output: Error in calculation  
Explanation: The system handles errors safely using try-except.

4. Exit Command  
Input: exit  
Expected Output: Program stops  
Explanation: The loop ends and the program terminates.

---

### Deployment Preparation
The system is prepared to run as a local Python application.

To run the system:
1. Install Python on the computer.
2. Open a terminal in the project directory.
3. Run the command: python main.py

No additional configuration is required, and all dependencies are included in the project.

---

### Data Conversion and Handling
The system processes user input as text.

When the input contains a mathematical expression, it is passed as a string to the calculator tool. The tool evaluates the expression and returns a numerical result.

The system ensures consistency by handling all inputs as strings and converting them only when needed. Error handling is used to manage incorrect or invalid data safely.
