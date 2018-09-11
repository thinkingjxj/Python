from sklearn.feature_extraction.text import CountVectorizer


vectorizer = CountVectorizer()
corputs = ["I come to china to travel",
           'This is a car popular in China',
           'I love tea and Apple',
           'The work is to write some papers in science']

# print(vectorizer.fit_transform(corputs))

print(vectorizer.fit_transform(corputs).toarray())
print(vectorizer.get_feature_names())

