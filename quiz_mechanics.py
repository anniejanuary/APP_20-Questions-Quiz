class QuizMechanics:

    def __init__(self, question_list):
        self.questions_asked = 0
        self.score = 0
        self.questions_list = question_list
        self.question_data_indices = list(range(0, len(question_list)))
        import random
        self.random_dict_index = random.choice(self.question_data_indices)

    def randomize_questions(self):
        # to remove randomly picked questions from the remaining question pool
        import random
        self.random_dict_index = random.choice(self.question_data_indices)
        self.current_question = self.questions_list[self.random_dict_index]
        self.question_data_indices.remove(self.random_dict_index)

    def keep_asking(self):
        return self.questions_asked < 20
                                    # or length of dict list: len(self.questions_list)
                                    # eg if current questions_asked == 10: 10 < 12 == True -> return True
        # alternative longer way:
        # if self.questions_asked < len(self.questions_list):
        #     return True
        # else:
        #     return False

    def welcome(self):
        print("Welcome to the 🔮20 Questions Quiz🤔 !")

    def next_question(self):
        self.randomize_questions()
        self.questions_asked += 1
        choice = input(f"\nQ.{self.questions_asked}: {self.current_question.text} (True/False)?: ")
        if choice.lower() == self.current_question.answer.lower(): # ensuring both eg True and true work
            print("✅ That's correct!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.questions_asked}.")
        elif (choice.lower() == "true" and self.current_question.answer.lower() == "false") or (choice.lower() == "false" and self.current_question.answer.lower() == "true"):
            print("❌ That's incorrect!")
            print(f"Your current score is {self.score}/{self.questions_asked}.")
        else:
            print("❌ Please check your spelling and try again.")
            self.questions_asked -= 1

    def final_score(self):
        print("\n----------------------------------------")
        print("🎉(ノ^ ^)ノ Congratulations! ヘ(^ ^ヘ)🎉")
        print(f"        Your final score is {self.score}/{self.questions_asked}")  # or: {self.score}/{len(question_bank)}")
        print("----------------------------------------")
