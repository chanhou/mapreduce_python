

all: map_inverted_index.py
	cat test.csv | ./map_inverted_index.py

file:
	head -30000 forum_node.tsv > test.csv

test:
	# cat test.csv | ./map_inverted_index.py | ./reduce_inverted_index.py
	cat forum_node.tsv | ./map_inverted_index.py | ./reduce_inverted_index.py