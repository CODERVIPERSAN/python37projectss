class QuizBrain:
    def __init__(self, q_lis):
        self.question_number = 0
        self.question_list = q_lis
        self.score = 0

    def check_answer(self, user_input, particular_question):
        if user_input == particular_question:
            print("you ar correct lets move ")
            self.score += 1
            print(f"you score ,{self.score}")

            return True
        print(f"your score ,{self.score}")
        return False

    def next_question(self):
        item = self.question_list[self.question_number]
        user_input = input(f"Q>>{self.question_number + 1}>>{item.question} say true or false:")
        return self.check_answer(user_input, item.answer)
