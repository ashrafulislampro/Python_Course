class Exam:
      exam_type = "class test"
      def __init__(self, highest_mark,lowest_mark ):
          self.highest_mark = highest_mark
          self.lowest_mark = lowest_mark
          
      def get_result(self, mark):
            if mark > self.highest_mark:
                print(f"Invalid Mark! {mark}")
            elif mark >= 80 and mark <= 100:
                print(f"Your result is A+")
            elif mark >= 60 and mark <= 79:
                print(f"Your result is A")
            elif mark >= 50 and mark <= 59:
                print(f"Your result is A-")
            elif mark >= 40 and mark <= 49:
                print(f"Your result is B")
            elif mark >= self.lowest_mark and mark <= 39:
                print(f"Your result is C")
            else:
                print(f"Your are Failed")
      def attend_to_exam(self):
          print("Thanks for attending to the exam")
          

exm = Exam(100, 33)
exm.get_result(32)
exm.attend_to_exam()