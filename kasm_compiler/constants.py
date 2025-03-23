INSTRUCTION_SET = {
    "NoOp": "0000",
    "Data": "0001", 
}

ALU_INSTRUCTION_SET = {
    "Add": "0000",      #0
    "Add!A": "0001",    #1
    "Add!B": "0010",    #2
    "Add!A!B": "0011",  #3
    "AddC": "0100",     #4
    "Sub": "0101",      #5
    "RSub": "0110",     #6
    "Sub_!A": "0111",   #7
    "AB": "1000",       #8
    "A!B": "1001",      #9
    "A|B": "1010",      #A
    "A|!B": "1011",     #B
    "Xor": "1100",      #c
    "Xor!B": "1101",    #D
    "Mov": "1110",      #E
    "nMov": "1111",     #F
}