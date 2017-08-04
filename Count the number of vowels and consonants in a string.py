#string of vowels
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

#take input from the user
ip_str = raw_input("Enter a string :")

#make it suitable for caseless comparisons
ip_str = ip_str.lower()

#make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

#count the vowels
for char in ip_str:
    if char in count:
        count[char] += 1
#count number of vowels
nov = sum(ip_str.count(c) for c in vowels)
#count number of consonants
noc = sum(ip_str.count(c)for c in consonants)

print
print(count)
print
print "Number of Vowels in a string : ", nov
print
print"Number of Consonants in a string : ",noc