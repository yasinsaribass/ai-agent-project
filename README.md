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

## Final Submission – Completed System

### Final System Description and Goal
The developed system is a Python-based AI-assisted study assistant designed to process user input and provide meaningful responses. 

The main goal of the system is to simulate a simple intelligent agent capable of decision-making and tool usage. The system identifies different types of input and dynamically selects appropriate actions, such as performing calculations or generating textual responses.

Compared to the initial design, the system has been successfully implemented and validated, demonstrating a working interaction between the agent logic and external tools.

---

### Programming Concepts and Their Usage
The implementation of the system relies on several core programming concepts:

- Object-Oriented Programming: The Agent class encapsulates the system logic and manages decision-making.
- Functions: Used to implement reusable tools, such as the calculator function.
- Conditional Logic: Enables the agent to analyze input and determine appropriate actions.
- Loops: Provide continuous interaction with the user through a command-line interface.
- Modular Design: The system is divided into separate files (agent, tools, main), improving readability and maintainability.
- Error Handling: Implemented using try-except blocks to ensure the system handles invalid input safely.

These concepts were actively applied during development, transforming the initial idea into a functional system.

---

### Tools and Their Role in the System
The system integrates a calculator tool as an external component.

The role of the tool is to perform mathematical computations that the agent detects from user input. The agent acts as a controller, deciding when to call the tool and how to use its output.

This demonstrates a clear separation between decision-making (agent) and execution (tool), which is a fundamental concept in agent-based systems.

---

### Testing Results and Conclusions
The system was tested using multiple input scenarios, including valid calculations, normal text, and invalid expressions.

The results confirm that:
- The agent correctly identifies when to use the calculator tool
- The system produces expected outputs for different input types
- Error handling prevents system crashes and ensures stability

Overall, the system behaves consistently and fulfills its intended purpose as a simple AI-assisted application.

---

### Deployment Preparation Description
The system is prepared for local execution and does not require complex setup.

To run the system:
1. Install Python
2. Open a terminal in the project directory
3. Execute: python main.py

The project structure is organized and ready for use by other users, with clear separation of components.

---

### Deployment Strategy
The current version of the system is designed as a local command-line application.

For future deployment, the system could be extended into:
- A web-based interface for easier user interaction
- An API service for integration with other systems
- A cloud-based application for scalability

A staged deployment strategy is recommended, starting with local testing, followed by limited user testing, and finally full deployment.
