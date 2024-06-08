from random_word_generator import pick_random_word

def change_current_word_state(selected_word, current_word_state, character):
    modified_word_state=""

    for i in range(len(selected_word)):
        if current_word_state[i]=="_" and selected_word[i]==character:
            modified_word_state+=character
        else:
            modified_word_state+=current_word_state[i]

    return modified_word_state

def input_character_in_word(selected_word, input_char, current_word_state,attempts_remaining)


def play_game(attempts=5):
    selected_words= pick_random_word()

    current_word_state=""

    for i in selected_word:
        if i==' ' or i=='a' or i=='e' or i=='o' or i=='i' or i=='u' 
        current_word_state+=i
        else:
            current_word_state+="_"

    attempts_remaining = attempts

    print_current_state(current_word_state,attempts)

if __name__=="__main__":
    play_game()