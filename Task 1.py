#Task 1
############################
#Q1.1:
even=[]
odd=[]
def even_odd (x,y):
    for n in range (1,10):
        if n %2 == 0:
            x= even.append(n)
        else:
            y=odd.append(n)
    print(even,odd)
even_odd (5,2)

#///////////////////////////
#Q2.1
def func_py (x,y):
  for n in range (0,10):
    if n %2 == 0:
      x=[n]
    else:
      y=[n]
    print(x,y)
func_py([0], [5])

#///////////////////////////
#Q3.1
def mult (x,y):
    result=x*y
    print(result)
    return result 
mult(5,8)

#///////////////////////////
#Q4.1
def no_duplicats(sentence):
    s=sentence.split(' ')
    new_s=[]
    for w in s:
        if w not in new_s:
            new_s.append(w)
            print(new_s)
   
no_duplicats('iphone 15 has has the 3 nanometer chip chip')

#///////////////////////////
#Q5.1
#-------------------------------------------------------
#make sentence 
#split words for sentence
#count how many words in a sentence (with out spaces)
#-------------------------------------------------------

#definfing the function count_words which takes the sentences
def count_words(sentence):
    #spliting the sentneces into words and storing them in variable words
   words=sentence.split()
   #new splited words is stored in new_words variable to determine its length
   new_words=(len(words))
   print(f"new_words: {new_words}")

#passing over the string to the function
count_words('Hello, world !')

#///////////////////////////
#Q6.1
#creating a function that takes sentences and words
def fun_sent(sentence):
    #split the sentence into words and storing them into new
    words=sentence.split()
    new_word='____'
    print(f"{new_word}, World !")
#passing the sentence to the function
sentence = 'Hello, World !'
fun_sent(sentence)

#///////////////////////////
#Q7.1
def word_count(sentence, word):
    w=sentence.split()
    counter = w.count(word)
    return counter

sentence='Amazon WEB WEB services'
word="WEB"
result = word_count(sentence,word)
print(f" The number {word} apperance is: {result} times")

#///////////////////////////
#Q8.1

def div (x,y):
    for nums in range(x,101):
        if nums%y == 0:
            print(nums)
div(10,5)
###############################################