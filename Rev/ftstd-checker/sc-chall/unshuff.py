def inv_table(transition):
    invTrans = {}
    
    for state in transition.keys():
        invTrans[state] = {}
    
    for state, transitions in transition.items():
        for bit, next_state in transitions.items():
            invTrans[next_state][state] = bit
    
    return invTrans

def unshuffle(encFlag, transition):
    invTrans = inv_table(transition)
    current_state = 0
    decFlag = []
    
    for char in encFlag:
        next_state = int(char)
        original_bit = invTrans[next_state][current_state]
        decFlag.append(str(original_bit))
        current_state = next_state
    
    return ''.join(decFlag)

if __name__ == "__main__":
    transition = {
        0: {0: 4, 1: 1},
        1: {0: 3, 1: 5},
        2: {0: 7, 1: 6},
        3: {0: 2, 1: 8},
        4: {0: 0, 1: 9},
        5: {0: 1, 1: 4},
        6: {0: 9, 1: 3},
        7: {0: 6, 1: 2},
        8: {0: 5, 1: 0},
        9: {0: 8, 1: 7}
    }

    encFlag = "498040151515151326980154013851513851540138015154015401385498015138013263263263804976385138013804015138540151385138549726972769727269769851540132726972769727269854015497638513269726976980497263263854976380401326327272726976385401549769727697638049851515497276385401326972698549851326972638549804985497632697272632726976976385497272632727632638013804049854980154015401327269769854015497638040498015151515404049801380404980154980132763263263851540498515154972726980132632698049763804015132727269727697638015154015404015132763804972727263804976327272726380497638540151327272697638515404976326380138049854015401327272638049769769854985151540497697276385154049804972763272697269854980151515497272632638515401327263851515497272"  # replace this with the actual encrypted flag

    decFlag = unshuffle(encFlag, transition)
    print(f"Binary Flag: {decFlag}")
    try:
        flag = bytes.fromhex(hex(int(decFlag, 2))[2:]).decode('utf-8')
        print(f"Flag: {flag}")
    except ValueError:
        print("Failed to decode flag. Ensure the binary flag is correct and represents valid ASCII.")
