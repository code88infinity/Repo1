#import modules that can help in the production of a code that includes timezones date and time and also time itself.

import time


import os


from tkinter import *


import datetime as dt


import pytz

#define a function that will clear the console when the console gets crowded and for the timer to work.

def clear_console():


    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#make the whole thing a loop so that it can be repeated and accessible with out running more than once.

while True:

  #the user interface with options to choose from while also giving the user the option to exit the program.

  print('''welcome to the clock and timer program
        this program is going to have the following features
        1. GMT clock
        2. international clock
        3. timer
        4. exit
        to use the modes please enter the corresponding number of the mode you want to use''')


  mode = input('please enter the mode of the clock you want to use.')

#if mode one is chosen then the program will show the greenwich mean time
  if mode == '1':
    clear_console() #clears the console
    print('you have chosen the GMT clock')
    print('the clock is going to be displayed in the next window')
    app = Tk()#creates a window


    app.title('Clock') #name of the window
    app.geometry('800x200')#resolution of the window

    #the label that will show the time and date in the window.
    one = Label(app,
                  font = ('calibri', 30, 'bold'),
                  background = 'cyan',
                  foreground = 'white')
    one.pack(anchor='center')
    
    #the function that is going to run every second and update the contents in the window.
    
    def count():
      geotime = time.strftime('%a %B %d/%m/%Y %I:%M:%S %p')
      one.config(text = geotime)
      one.after(1000, count)


    count()
    app.mainloop()# this loops to create the final peice of the clock.
    clear_console()# after the window is quitted it goes back to the main menu to choose another mode.

  # 2nd mode with the time zones and the user interface.

  elif mode == '2':
    #iterates till it breaks and gets back to the main menu.
    while True:
      #it clears traces of the main menu and shows new options 
      clear_console()
      countries = {
          'Addis_Ababa': 'Africa',
          'New_York': 'America',
          'London': 'Europe',
          'Paris': 'Europe',
          'Moscow': 'Europe',
          'Tokyo': 'Asia',
          'Sydney': 'Australia',
          'Nairobi': 'Africa',
          'Chicago': 'America',
          'Denver': 'America',
          'Cairo': 'Africa',
          'Dubai': 'Asia'
      }

      #starts the user interface

      print('''welcome to the international clock''')

      city = input('''Enter the number of the city you want to know the time of:
                  1.  Addis_Ababa,
                  2.  New_York,
                  3.  London,
                  4.  Paris,
                  5.  Moscow,
                  6.  Tokyo,
                  7.  Sydney,
                  8.  Nairobi,
                  9. Chicago,
                  10. Denver,  
                  11. Cairo,
                  12. Dubai
          enter the number of the city:
      ''')
      #if the user enters a number that is not in the list then it will ask the user to enter a number and between the range of the options.
      
      while city.isnumeric() == False:
          city = input('please enter a number')
          if city.isnumeric() == True:
              city = int(city)
              break
          else:
              continue
      else:
          city = int(city)


      while city < 1 or city > 12:
          city = input('please enter a number between 1 to 13')
          while city.isnumeric() == False:
              city = input('please enter a number')
          else:
              city = int(city)
              continue

      #takes in the city name and the time zone and then displays it in the console.
      name = list(countries.keys())[city -1]
      continent = countries[name]



      app = Tk()


      app.title('Clock')
      app.geometry('900x200')


      clock = Label(app,
                      font = ('calibri', 40, 'bold'),
                      background = 'cyan',
                      foreground = 'white')
      clock.pack(anchor='center')


      def let():
          date = dt.datetime.now(pytz.timezone(f'{continent}/{name}'))
          time = date.strftime('%Y-%m-%d %I:%M:%S %p')
          clock.config(text = time)
          clock.after(1000, let)
      #gives the user the name of the city and the time in that city.
      Label(app, text = name, font = ('calibri', 18, 'bold')).pack()
      let()
      app.mainloop()

      #asks the user if they want to use another mode or exit the program.
      
      again = input('Do you want to know the time of another city?')
      if again.lower() == 'yes':
          continue
      else:
          clear_console()
          break

  #3rd mode with the timer and the user interface.

  elif mode == '3':

    #iterates till it breaks and gets back to the main menu.
    while True:
      clear_console()
      print(''' based on the time order fill the time slots
      please follow the instructions carefully
      1. please enter the hours with a maximum of 23 and minimum of 0
      2. please enter the minutes with a maximum of 59 and minimum of 0
      3. please enter the seconds with a maximum of 59 and minimum of 1''')

      #takes in the inputs and checks if its the required format if not it iterates and asks the user to insert the number again.
      
      time_hr = input('hours')


      while time_hr.isnumeric() == False:
        time_hr = input('please enter numerical value of the hours.')
        if time_hr.isnumeric() == True:
          time_hr = int(time_hr)
          break
        else:
          continue

      else:
        time_hr = int(time_hr)


      while time_hr < 0 or time_hr > 23:
        time_hr= input('please enter the hours in between 0 to 23')

        while time_hr.isnumeric() == False:
          time_hr = input('please enter numerical value of the hours.')

        else:
          time_hr = int(time_hr)
          continue




      time_min = (input('minutes'))

      while time_min.isnumeric() == False:
        time_min = input('please enter numerical value of the minutes.')
        if time_min.isnumeric() == True:
          time_min = int(time_min)
          break
        else:
          continue


      else:
        time_min = int(time_min)

      
      while time_min < 0 or time_min > 59:
        time_min= input('please enter the minute in between 0 to 59')

        while time_min.isnumeric() == False:
          time_min = input('please enter numerical value of the minutes.')

        else:
          time_min = int(time_min)
          continue




      time_sec = input('seconds')


      while time_sec.isnumeric() == False:
        time_sec = input('please enter numerical value of the seconds.')
        if time_sec.isnumeric() == True:
          time_sec = int(time_sec)
          break
        else:
          continue


      else:
        time_sec = int(time_sec)


      while time_sec < 0 or time_sec > 59:
        time_sec= input('please enter the seconds in between 0 to 59')

        while time_sec.isnumeric() == False:
          time_sec = input('please enter numerical value of the minutes.')

        else:
          time_sec = int(time_sec)
          continue

      #takes in the information and then converts in to seconds and then displays it using the conversion method.
      
      min_min = time_hr * 60 + time_min
      sec_sec = min_min * 60 + time_sec
      clear_console()
      #clears the console to start the timer.
      while sec_sec != -1:
        for i in range(time_hr + 1):
          for j in range(time_min + 1):
            for k in range(time_sec + 1):
              print(f'time is {time_hr:02}:{time_min:02}:{time_sec:02}')
              time.sleep(1)
              clear_console()
              time_sec -= 1
              sec_sec -= 1
            time_min -= 1
            time_sec = 59
          time_hr -= 1
          time_min = 59

      print('your time is up, now do you want to set another timer')

# ask the user if they want to use the program and waits 5 seconds before the input is gathered to make the user read before agreeing or disagreeing.
      time.sleep(5)

      agreement = input('say yes if you want to and no if you do not want to')

      # checks if the user gives the correct information to the program and if not it asks the user to enter the information again.

      if agreement.lower() == 'yes':
        continue
      elif agreement.lower() == 'no':
        break


      while True:
        agreement = input('please insert yes or no.')
        if agreement.lower()=='yes' or agreement.lower()=='no':
          break
        else:
          continue

      if agreement.lower() == 'yes':
        continue
      elif agreement.lower() == 'no':
        break

      clear_console()


    clear_console()

# if the user chooses to exit the program then it will break the loop and exit the program.
  elif mode == '4':
    clear_console()
    print('''thank you for using the clock and timer program
    does this program diserve a 5?
    please rate it on a scale of 1 to 5 or leave a comment''')
    rating = input('insert here here: ')
    print('''thank you for giving your opinion 
            Have a nice day''')
    break 

#this is the error message that will be displayed if the user enters a number that is not in the list.
  
  else:
    print('please enter the correct mode of the clock you want to use.')
    time.sleep(5)
    clear_console()
    continue
