

# python 
```
movie_dict = {
  "movies": [
    {
      "title": "Inception",
      "director": "Christopher Nolan",
      "year": 2010
    },
    {
      "title": "The Lord of the Rings: The Fellowship of the Ring",
      "director": "Peter Jackson",
      "year": 2001
    },
    {
      "title": "Parasite",
      "director": "Bong Joon Ho",
      "year": 2019
    }
  ]
}
```
Here's how we can save it to the JSON file movies.json:
```
import json
 
 
with open("movies.json", "w") as json_file:
    json.dump(movie_dict, json_file)
```
Two arguments: the data and the file-like object that you can write to. 

you'll create a JSON file with the data about movies.
```
json_str = json.dumps(movie_dict)
print(json_str)
```


The basic of unitted test
```
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
```
