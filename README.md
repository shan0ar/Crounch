# crounch

## Usage :
python crounch _keyword_to_generate_

**OR**

python crounch _keyword_to_generate_ --number=_max_of_word_in_wordlist_

**OR**

python crounch _keyword_to_generate_ --number=_max_of_word_in_wordlist_ --output=_output_location_

examples :
python crounch Password123

**OR**

python crounch Password123 --number=10000

**OR**

python crounch Password123 --number=9000000 --output=/tmp/crounch_output.dic


### Options:

#### --number 
> Maximum number of word generated by crounch in the output, by default, crounch generate a maximum of 50 000 000 words but if he can't make as much, he stop at his maximum without duplicates.
 
#### --output
> Allows you to specify the file to write the output to, eg: wordlist.txt.
