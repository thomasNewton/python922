import requests
#import webbrowser
import os
clearConsole=lambda: os.system("cls")

myUrl="https://randomnerdtutorials.com/cloud-weather-station-esp32-esp8266/"
keyWord ="<script>"

resp=requests.get(myUrl)
#bro= webbrowser
#bro.open_new(resp.url)
bigS=resp.text
bigL =bigS.split()
size=len(bigL)

#print(f"the list of elements contains {bigL.count("<script>")} number of scripts")
clearConsole()
print(f"the list contains {bigL.count(keyWord)} many elements of the '{keyWord}' keyword")
print(f"the list is {size} elements long and is the parsed content of the return from the original url\n")
print("printing the first 10 elements of the list, elements are delineated by spaces not html tags\n")
for x in range(9):
    print (bigL[x])