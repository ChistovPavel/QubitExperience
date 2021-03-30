import Test

lineSeparator = '\n====================================================\n'

while(True):
    inputValue = input("\
1) Get Bell's state\n\
2) Quantum Teleportation\n\
3) Exit\n\
your input: "
);
    if inputValue == '1':
        Test.bellsStateTest()
    elif inputValue == '2':
        Test.quantumTeleportationTest()
    elif inputValue == '3':
        break
    print(lineSeparator)