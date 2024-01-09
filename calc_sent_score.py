positive_emotions = [
        'admiration', 'joy', 'approval', 'optimism', 'pride', 'relief', 
        'realization', 'amusement', 'excitement', 'gratitude', 'caring', 'love'
    ]
negative_emotions = [
        'annoyance', 'disapproval', 'disappointment', 'sadness', 
        'grief', 'anger', 'fear', 'disgust', 'remorse'
    ]

def normalize_sent_score(list):
    # Initialize scores
    positive_score = 0.0
    negative_score = 0.0

    # Iterate over the emotions and calculate the scores
    for item in list[0]:
        if item['label'] in positive_emotions:
            positive_score += item['score']
        elif item['label'] in negative_emotions:
            negative_score += item['score']

    # Calculate normalized sentiment score
    normalized_score = (positive_score - negative_score) / (positive_score + negative_score)
    return normalized_score

#testing!
'''
test = normalize_sent_score([[{'label': 'neutral', 'score': 0.8345432281494141}, {'label': 'approval', 'score': 0.16803598403930664}, {'label': 'realization', 'score': 0.038962215185165405}, {'label': 'optimism', 'score': 0.0178600512444973}, {'label': 'disapproval', 'score': 0.015419571660459042}, {'label': 'annoyance', 'score': 0.013705995865166187}, {'label': 'admiration', 'score': 0.007412726990878582}, {'label': 'caring', 'score': 0.005830458831042051}, {'label': 'disappointment', 'score': 0.005338154733181}, {'label': 'amusement', 'score': 0.004917615093290806}, {'label': 'joy', 'score': 0.004108110908418894}, {'label': 'relief', 'score': 0.002797325374558568}, {'label': 'desire', 'score': 0.0025996495969593525}, {'label': 'excitement', 'score': 0.001484735170379281}, {'label': 'confusion', 'score': 0.0013670171611011028}, {'label': 'pride', 'score': 0.0013447668170556426}, {'label': 'disgust', 'score': 0.0013434975408017635}, {'label': 'sadness', 'score': 0.001284155179746449}, {'label': 'anger', 'score': 0.0007865192019380629}, {'label': 'love', 'score': 0.0007642144919373095}, {'label': 'gratitude', 'score': 0.0007250889902934432}, {'label': 'fear', 'score': 0.0007001436897553504}, {'label': 'embarrassment', 'score': 0.0006145141087472439}, {'label': 'nervousness', 'score': 0.0005530228954739869}, {'label': 'curiosity', 'score': 0.00048472409253008664}, {'label': 'remorse', 'score': 0.00038348991074599326}, {'label': 'surprise', 'score': 0.0003135013685096055}, {'label': 'grief', 'score': 0.0003036816488020122}]])

print(test)
'''