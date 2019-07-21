    while True:
        input_choice = ''
        while input_choice not in ['n', 'r', 'e']:
            input_choice = input(
                'Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            if input_choice not in ['n', 'r', 'e']:
                print('Invalid command.')
        if input_choice == 'e':
            break
        input_second_choice = ''
        while input_second_choice not in ['u', 'c']:
            input_second_choice = input(
                'Enter u to have yourself play, c to have the computer play: ')
            if input_second_choice not in ['c', 'u']:
                print('Invalid command.')
        if input_second_choice == 'u':
            if input_choice == 'n':
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
            elif input_choice == 'r':
                try:
                    playHand(hand, wordList, HAND_SIZE)
                except:
                    print(
                        'You have not played a hand yet. Please play a new hand first!')
            else:
                print('Input is invalid!')
        elif input_second_choice == 'c':
            if input_choice == 'r':
                try:
                    compPlayHand(hand, wordList, HAND_SIZE)
                except:
                    print(
                        'You have not played a hand yet. Please play a new hand first!')
            elif input_choice == 'n':
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)
