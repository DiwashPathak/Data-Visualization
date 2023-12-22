#survery.py

class Survey:
    def __init__(self, question):
        self.question = question
        self.results = []
        self.type_opinions = []
        self.num_opinion = 0

    def take_survery(self):
        # Take opinions and store it
        while True:
            # print("Press q to exit! ")
            print(" ")

            # Take opinion
            opinion = input(self.question + " :").lower()
            
            # Break loop if input is q
            if opinion == "q":
                break
            
            # Append unique opinion
            if opinion not in self.type_opinions:
                self.type_opinions.append(opinion)

            # Append opinion to results
            self.num_opinion += 1
            self.results.append(opinion)