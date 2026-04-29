from tools.calculator import calculate

class Agent:

    def process_input(self, user_input):

        # if input contains math
        if any(char.isdigit() for char in user_input):
            try:
                return calculate(user_input)
            except:
                return "Calculation error"

        # normal text
        return "I am a simple AI assistant. You said: " + user_input