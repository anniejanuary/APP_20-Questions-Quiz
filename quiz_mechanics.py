class QuizMechanics:

    def __init__(self, question_list):
        self.questions_asked = 0
        self.score = 0
        self.questions_list = question_list
        self.question_data_indices = list(range(0, len(question_list)))
        import random
        self.random_dict_index = random.choice(self.question_data_indices)
        self.repeat_question = False

    def welcome(self):
      print("Welcome to 🔮 The 20 Questions Quiz 🤔 !")

    def randomize_questions(self):
        '''Randomly picks questions and removes them from the remaining question pool'''
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

    def next_question(self):
        self.questions_asked += 1
        if self.repeat_question is False:
          self.randomize_questions()
        choice = input(f"\nQ.{self.questions_asked}: {self.current_question.text} (True/False)?: ")
        if choice.lower() == self.current_question.answer.lower(): # ensuring both eg True and true work
            print("✅ That's correct!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.questions_asked}.")
            self.repeat_question = False
        elif (choice.lower() == "true" and self.current_question.answer.lower() == "false") or (choice.lower() == "false" and self.current_question.answer.lower() == "true"):
            print("❌ That's incorrect!")
            print(f"Your current score is {self.score}/{self.questions_asked}.")
            self.repeat_question = False
        else:
            print("❌ Please check your spelling and try again.")
            self.questions_asked -= 1
            self.repeat_question = True

    def final_score(self):
        print("\n--------------------------------------------------------")
        print("       🎉(ノ^ ^)ノ Congratulations! ヘ(^ ^ヘ)🎉")
        print(f"              Your final score is {self.score}/{self.questions_asked}")  # or: {self.score}/{len(question_bank)}")
        if int(self.score) > 16:
          print("  You're a rockstar in a top hat *rips a guitar solo*")
        elif self.score > 12:
          print("      Good job! Here's your hard earned cookie 🍪")
        elif self.score > 7:
          print(" You've showed up and tried, that's a win in my book! 🌟")
        else:
          print("      'Success is not final, failure is not fatal: \n       it is the courage to continue that counts.'\n               - Winston S. Churchill")
        print("--------------------------------------------------------")
