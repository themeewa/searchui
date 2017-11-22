from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob
training_corpus = [
					('how fan works','Class_B'),
					('playing football', 'Class_B'),
					('swimming', 'Class_B'),
					('cooking food', 'Class_B'),
					('How to cook food', 'Class_B'),
					('How to draw', 'Class_B'),
					('How to fight', 'Class_B'),
					('how to talk to a person', 'Class_B'),
					('how to remove screw from cycle', 'Class_B'),
					('how to eat apple', 'Class_B'),
					('the proper way for swimming', 'Class_B'),
					('stemming in nlp', 'Class_B'),
					('how to drink water', 'Class_B'),
					('what is currency of england', 'Class_A'),
					('what is a wrist watch', 'Class_A'),
					('Football', 'Class_A'),
					('Water', 'Class_A'),
					('Apple', 'Class_A'),
					('Fan', 'Class_A'),
					('Screwdriver', 'Class_A'),
					('what is a flower', 'Class_A'),
					('what is wormwhole', 'Class_A'),
					('what is google', 'Class_A'),
					('what is computer software', 'Class_A'),
					('what is a fan', 'Class_A'),
					('what is sketch', 'Class_A'),
					('what is ponytail', 'Class_A'),
					('Why days and night happen', 'Class_C'),
					('why karnataka is hot', 'Class_C'),
					('why people fight', 'Class_C'),
					('why thor killed hella', 'Class_C'),
					('why sky is blue', 'Class_C')
				]
test_corpus = [
                ("I am not feeling well today.", 'Class_B'), 
                ("I feel brilliant!", 'Class_A'), 
                ('Gary is a friend of mine.', 'Class_A'), 
                ("I can't believe I'm doing this.", 'Class_B'), 
                ('The date was good.', 'Class_A'), ('I do not enjoy my job', 'Class_B')]

model = NBC(training_corpus) 
print(model.classify("why she fell down"))
print(model.classify("rainy season"))
