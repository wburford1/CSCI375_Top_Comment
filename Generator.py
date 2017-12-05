import json

with open('category_dict.json') as json_data:
    category_dict = json.load(json_data)
with open('title_dict.json') as json_data:
	title_dict = json.load(json_data)
with open('tags_dict.json') as json_data:
	tags_dict = json.load(json_data)
with open('video_dict.json') as json_data:
    video_dict = json.load(json_data)

category_corpus = []
def category_generator(name = '23'):
	for video in category_dict[name]:
		try:
			category_corpus.append(video_dict[video])
		except KeyError:
			print("no Comment")
	print(category_corpus)
	return category_corpus 

def corpus_processing(category_corpus):
	corpus =[]
	for e in category_corpus:
		for a in e:
			corpus.append(a[0])
	return corpus

if __name__ == '__main__':
	corpus = corpus_processing(category_generator())
	with open('category_corpus.txt', 'w') as f:
		for e in corpus:
			f.write(e)
#print(tags_dict)
#print(title_dict)
#print(category_dict)