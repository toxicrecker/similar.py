from difflib import SequenceMatcher as sm

def best_match(word, words):
    instance = Similarity(word, words)
    return instance.best()

class Similarity(object):
    
    def __init__(self, word, words):
        self.word = word
        self.words = words
        
    def __iter__(self):
        return iter([key for key in self.results().keys()])
        
    def __str__(self):
        return self.best()
        
    def __float__(self):
        return self.best_ratio()[1]
        
    def __int__(self):
        return round(self.best_ratio()[1])
        
    def results(self):
        if isinstance(self.words, str):
            self.words = [self.words]
        similarities = {}
        words = [word.strip() for word in self.words]
        if not words:
            return None
        for x in words:
            ratio = sm(None, self.word, x).ratio()
            similarities[x] = ratio
        results = dict(sorted(similarities.items(), key=lambda x: x[1], reverse=True))
        return results
        
    def best(self):
        results = self.results()
        return list(results.keys())[0]
    
    def best_match(self):
        results = self.results()
        return results.keys()[0]
        
    def best_ratio(self):
        results = self.results()
        return (list(results.keys())[0], results[list(results.keys())[0]])
