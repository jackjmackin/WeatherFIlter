#READ ME: when prompt to pick a file, choosen a photo

import urllib
import simplejson as json
import gui
from gui import *

global temp, picture

# this function is pulls the API data for Bouder, sets the current temperture to temp, changes the color of our gui based on temp, has the user choose a picture, and decided if a warm or cool filter should be applied based on temperture
#this function as returns the current temperture as temp, then also lets user choose a picture to be carried out by the program
#agruements: none
#returns: temperature
def setUp():
  global picture, temp
  url = "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20%3D%202367231&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
  response = urllib.urlopen(url)
  data = json.loads(response.read())

  #this pulls the current temperature in boulder
  temp = data["query"]["results"]["channel"]["item"]["condition"]["temp"]

  #comment the temp above and uncomment the temp below to test a different temp - 90 could be changed to any degree  
  #temp = 90

  
  #changes background color of GUI window based on current temp
  if (int(temp)) >= 50:
    d = Display("Boulder Weather Filter", 280, 265, 0, 0, Color ((int(temp)*2), 155, 0))
    
  else:
    d = Display("Boulder Weather Filter", 280, 265, 0, 0, Color(50, int(temp)+40, (255-(int(temp)*3))))
  

  #tells GUI window to say its freezing, chilly, hot, or warm, based on the current temp
  if (int(temp)) >= 50:
    text5 = d.drawLabel('Warm', 90, 60, Color.white, Font("Helvetica", Font.BOLD, 35))
  
  if (int(temp)) >= 70:
    text7 = d.drawLabel('Hot', 110, 60, Color.white, Font("Helvetica", Font.BOLD, 35))
    d.remove(text5)
    
  if (int(temp)) <= 49:
    text6 = d.drawLabel('Chilly', 90, 60, Color.white, Font("Helvetica", Font.BOLD, 35))
    
  if (int(temp)) <= 32:
    text7 = d.drawLabel('Freezing', 65, 60, Color.white, Font("Helvetica", Font.BOLD, 35))
    d.remove(text6)
    
   #text 1- 4 draws main text on gui window
  text1 = d.drawLabel('It is currently:', 20, 20, Color.white, Font("Helvetica", Font.BOLD, 35))
  text2 = d.drawLabel('In Boulder, CO', 20, 215, Color.white, Font("Helvetica", Font.BOLD, 35))

  #text3 below puts the current temp on the gui window
  text3 = d.drawLabel(data["query"]["results"]["channel"]["item"]["condition"]["temp"], 45, 95, Color.white, Font("Helvetica", Font.BOLD, 135))

  #if you need to test a different temperture, replace the "90" string with the desried temperture
  #text3 = d.drawLabel("90", 45, 95, Color.white, Font("Helvetica", Font.BOLD, 135))

  text4 = d.drawLabel('F', 200, 100, Color.white, Font("Helvetica", Font.BOLD, 65))
  
  #lets user pick a file (picture), then makes it into a picture that can be explored
  picture = makePicture(pickAFile())
  
  #applies warmFIlter function if the temp is 50 or above, and applies a cool filter if temp is below 50
  if (int(temp)) > 50:
    warmFilter(picture)
    
  else:
    coolFilter(picture)
  
  #return the temperture    
  return temp
  
#this function add a warmer red color filter on photo, changes based on current temp
#agruements: a picture
#returns: a picture with filter applied
def warmFilter(picture):
  global temp
  for p in getPixels(picture): 
    redP = getRed(p)
    greenP = getGreen(p)
    blueP = getBlue(p)
    newRed = redP + (int(temp) - 50) * 2
    newGreen = greenP
    newBlue = blueP
    newColor = makeColor(newRed,newGreen,newBlue)
    setColor(p,newColor)
    
#this function add a cooler/blue color filter on photo, changes based on current temp
#agruements: a picture
#returns: a picture with filter applied  
def coolFilter(picture):
  global temp
  for p in getPixels(picture): 
    redP = getRed(p)
    greenP = getGreen(p)
    blueP = getBlue(p)
    newRed = redP
    newGreen = greenP
    newBlue = blueP + (50 - int(temp)) * 2
    newColor = makeColor(newRed,newGreen,newBlue)
    setColor(p,newColor)
    

setUp()
explore(picture)