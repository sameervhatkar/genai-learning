#Indexing and substring

name = "Sameer Vhatkar"  
# S  --> 0
# a  --> 1
# m  --> 2
# e  --> 3
# e  --> 4
# r  --> 5
# (space) --> 6
# V  --> 7
# h  --> 8
# a  --> 9
# t  --> 10
# k  --> 11
# a  --> 12
# r  --> 13   
print(f"First word: {name[0:6]}")
print(f"Last Word: {name[7:]}")
print(f"All the letter but alternate: {name[0:13:2]}")

#Reversing the string
print(f"Reversed String: {name[::-1]}")

#Encoded string Sàmeer, over here 'a' is not in simple english letter its in diff language or symbol
name2 = "Sàmeer"
print(name2) #over here it is working fine but if the language is not english but let say chinese, hindi etc then it will be mess, so we have to encode it
encode_name2 = name2.encode("utf-8")
print(f"Encoded string: {encode_name2}")