import random

class MarkovChain:
    def __init__(self, n=2):
        self.n = n
        self.model = {}

    def train(self, text):
        words = text.split()
        for i in range(len(words) - self.n):
            gram = tuple(words[i:i+self.n])
            next_word = words[i+self.n]
            if gram in self.model:
                self.model[gram].append(next_word)
            else:
                self.model[gram] = [next_word]

    def generate(self, start, num_words=100):
        sentence = start
        start_words = start.split()
        word_list = start_words
        for i in range(num_words):
            gram = tuple(word_list[-self.n:])
            if gram in self.model:
                next_word = random.choice(self.model[gram])
                sentence += ' ' + next_word
                word_list.append(next_word)
            else:
                break
        return sentence

# Sample usage
if __name__ == '__main__':
    text = "This is a simple Markov chain example. This is fun. This is cool."
    markov = MarkovChain(n=2)
    markov.train(text)
    generated_text = markov.generate("This is", 10)
    print(generated_text)
