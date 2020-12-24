class Solution:
    def interpret(self, command: str) -> str:
        output = ''

        while command:
            if command[0] == 'G':
                output += 'G'
                command = command[1:]
            elif command[0] == '(' and command[1] == ')':
                output += 'o'
                command = command[2:]
            else:
                output += 'al'
                command = command[4:]
        return output
