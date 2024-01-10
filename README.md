A use case of sentiment analysis LLMs for tracking sentiments in a personal knowledge base like Logseq. 

I came upon this video by Matt D'Avella a while back about systematically tracking your mood and how that helps you cultivate awareness. I'm never quite the person to be able to track--or for that matter even determine--my mood in a given day, but I thought since I have ~300,000 words in my personal knowledge base in [Logseq](https://logseq.com/), a computer might do the job for me! 

I did a similar project with the lexicon-based [Vader](https://pypi.org/project/vaderSentiment/) module but the accuracy was too low. I'm using the [RoBERTa model](https://huggingface.co/SamLowe/roberta-base-go_emotions/tree/main) trained on the [Go Emotions](https://huggingface.co/datasets/go_emotions) dataset which still is limited not least by the labellers who thought "LETS FUCKING GOOOOO" meant anger. By [some estimation](https://www.surgehq.ai/blog/30-percent-of-googles-reddit-emotions-dataset-is-mislabeled) 30% of the Go Emotions dataset is blatantly wrong. Recognizing the limitations, this is probably still the best and most cost-efficient solution we have.

Sample:
<img width="1082" alt="image" src="https://github.com/JoNeedsSleep/sent_analysis_logseq/assets/39445027/62076a38-3294-411f-ba3b-792d1311ae89">
