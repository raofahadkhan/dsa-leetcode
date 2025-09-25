class StudentScores:
    
    def __init__(self, size = 10):
        self.size = size
        self.scores = [None] * size
        
    def hash_function(self, key):
        return hash(key) % self.size
    
    def add_score(self, student_name, score):
        index = self.hash_function(student_name)
        self.scores[index] = (student_name, score)
        
    def get_score(self, student_name):
        index = self.hash_function(student_name)
        return self.scores[index]
    
    def __repr__(self):
        # Provide a readable representation of the object
        return f"StudentScores({self.scores})"
    
score_list = StudentScores()
print(score_list)
score_list.add_score("fahad", 50)
print(score_list)
score_list.add_score("faizan", 100)
print(score_list)

faizan_score = score_list.get_score("faizan")
print(faizan_score)

fahad_score = score_list.get_score("fahad")
print(fahad_score)
