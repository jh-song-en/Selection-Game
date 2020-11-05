
class game():
    def __init__(self):
        self.life = 10
        self.money = 0
        self.mental = 10
        self.life_limit = 10
        self.mental_limit = 10
        self.item = {}
        self.secret_status = []

    def get_answer(self):
        answer = input()
        if answer == "0":
            self.see_item()
        else:
            self.consequences(answer)
    def see_item(self):
        print(self.item)

    def event_holder(prob, succes_item_list, fail_item_list, succes_reward, fail_reward):
        pass

    def consequences(self):
        pass

    def show_event(self, event_string):

        print("################################")
        print("life:", self.life, "money:",self.money, "mental:", self.mental)
        print(event_string)
        print("################################")
        pass

    def show_choices(self, choices_list):
        for i in range(len(choices_list)):
            print("%d. %s"%((i + 1), choices_list[i]))
        pass


if __name__ == '__main__':
    game = game()
    game.show_event(
    """
    Welcome to the game.
    What do you want to do?    
    """
    )
    game.show_choices([
    "leave",
    "stay"
    ])
    game.get_answer()
