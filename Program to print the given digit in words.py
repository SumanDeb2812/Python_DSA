# Given a number N, the task is to convert every digit of the number into words.

def convertIntoWord(n):
    dist = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    s = str(n)
    for i in s:
        print(dist[i], end=" ")

convertIntoWord(1234507890)