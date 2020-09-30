# similar
A dependency less python library made for finding similar text inspired from [similar](https://pypi.org/project/similar)

# Usage
```py
import similar

match = similar.best_match("apply", ["pickle", "apple", "orange"])
print(match)
> apple
```

# Extras
Also works with

file -

```py
import similar

match = similar.best_match("apply", open("words.txt", "r"))
print(match)
> apple
```

or generator object

```py
import similar

def genwords():
	for word in ["picke", "apple", "orange"]:
		yield word
		
match = similar.best_match("apply", genwords())
print(match)
> apple
```