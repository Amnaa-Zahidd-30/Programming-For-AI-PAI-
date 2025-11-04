allPosts = [{'id':1,'text':'Using #Gulphone % was a crazy experience. it$$ was so good that it cured my cornea and now I can walk again'},
 {'id':2,'text':'@gulphone has to be the best in market like seriously, when &i walked in the store i could feel its aura'},
 {'id':3,'text':"Even if you paid me a million ++dollars to leave a decent review; I'd never take it.thats how bad this phone is! #disgusting"},
 {'id':4,'text':'my daughter bought this for her 9th ----birthday and now its her 50th. lasted for decades ^-^! amazing phone ngl'},
 {'id':5,'text':'@GulAli The quality was  =disastrous! never buying again :('},
 {'id':6,'text':"@Mishoo I got mine from a secondhand source it was ,,,the worst phone% i've *ever had"}]

punctuationChar = "!$%^&*()_+-=,./][:]{};'`~|"
stopWords = {'i','a','me','my','this','that','an','is','am','was','and','but','if','or','to','of','at','by','for','with','this','that'}
posWords = {'good','best','amazing','cool'}
negWords = {'bad','disastrous','horrible','worst'}

def preprocessText(text, punctuationList, stopWordsSet):
    text = text.lower() 
    for p in punctuationList: 
        text = text.replace(p, "")
    words = text.split()  
    cleanwords = [word for word in words if word not in stopWordsSet]
    return cleanwords

def analyzePosts(postList, punctuation, stopWords, positive, negative):
    processed = map(
        lambda p: {
            'id': p['id'],
            'original_text': p['text'],
            'processed_text': preprocessText(p['text'], punctuation, stopWords)
        },
        postList
    )
    scoredposts = []
    for post in processed:
        score = 0
        for word in post['processed_text']:
            if word in positive:
                score += 1
            elif word in negative:
                score -= 1
        post['score'] = score
        scoredposts.append(post)
    return scoredposts

def getFlaggedPosts(scoredPosts, sentimentThreshold=-1):
    return [post for post in scoredPosts if post['score'] <= sentimentThreshold]

def findNegativeTopics(flaggedPosts):
    topicCounts = {}
    for post in flaggedPosts:
        for word in post['processed_text']:
            if word.startswith("#") or word.startswith("@"):
                topicCounts[word] = topicCounts.get(word, 0) + 1
    return topicCounts

scored = analyzePosts(allPosts, punctuationChar, stopWords, posWords, negWords)
flagged = getFlaggedPosts(scored)
topics = findNegativeTopics(flagged)

print("Flagged Negative Posts (score ≤ -1):")
for f in flagged:
    print(f"Post ID: {f['id']} | Score: {f['score']} | Text: {f['original_text']}")

print("\nTrending Negative Topics:")
for topic, count in topics.items():
    print(f"{topic}: {count}")
