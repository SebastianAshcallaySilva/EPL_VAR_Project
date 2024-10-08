from pandas import *
import re
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib import animation
from matplotlib.animation import FuncAnimation

# This program display an animated plot graph to compare points per season for a specific team
# with and without VAR. The generated graph will be saved in a GIF file.

# ----------------- ANIMATION ----------------------------
# To generate no loop gif
from PIL import Image
import io

def convert(old_filename, new_filename, duration):
    images = []
    with Image.open(old_filename) as im:
        for i in range(im.n_frames):
            im.seek(i)
            buf = io.BytesIO()
            im.save(buf, format='png')
            buf.seek(0)
            images.append(Image.open(buf))
    images[0].save(new_filename, save_all=True, append_images=images[1:], optimize=False, duration=duration)
# ---------------------------------------------------------

def printList(aList):
  for elements in aList:
    print(f'* {elements}')

def lowest10(n):
  if n % 10 == 0:
    n -= 1
  if n % 2 != 0:
    n -= 1
  while n % 10 != 0:
    n -= 2
  return n

def highest10(n):
    if n % 10 == 0:
        n += 1
    if n % 2 != 0:
        n += 1
    while n % 10 != 0:
        n += 2
    return n

def returnElements(elements, idxs):
    subElements = []
    for i in range(idxs + 1):
        subElements.append(elements[i])
    return subElements

def returnElementsRange(elements, start, end):
    subElements = []
    for start in range(end + 1):
        subElements.append(elements[i])
    return subElements

try:
    teamList = ['Man City', 'Man Utd', 'Tottenham', 'Liverpool', 'Chelsea', 'Arsenal', 'Burnley', 'Everton', 'Leicester City', 'Newcastle Utd',
                  'Crystal Palace', 'West Ham', 'Brighton', 'Southampton']

    data = read_csv('https://raw.githubusercontent.com/SebastianAshcallaySilva/EPL_VAR_Project/main/VAR_PythonProject/PL_Table[seasons].csv')
    print('Which Premier League team would you like to see points for?')
    printList(teamList)
    team = input('\n--> ')

    if team not in teamList:
      raise Exception('Invalid team! Please try entering a team from the list')

    pts = []
    pts_title = []
    ptsNoVar = []
    pts_titleNoVar = []
    pts_MIN = 0
    pts_MAX = 0

    # Experiment: Seeing how many seasons are recorded in CSV file. Automatically updates with CSV file
    column_names = list(data.columns)
    season_cnt = 0
    for cols in column_names:
      if re.match(r"20\d\d/\d\d", cols):
        season_cnt += 1
    # print(season_cnt)

    
    for i in range(season_cnt):
      ptsList = data[f'Pts (20{i + 17}/{i + 18})'].tolist() # Get points for every season
      teamsList = data[f'20{i + 17}/{i + 18}'].tolist() # Get teams for every season
      pts.append(ptsList[teamsList.index(team)])
      pts_title.append(f'20{i + 17}/{i + 18}')

      # Find min and max pts of team between these past seasons
      if i == 0:
        pts_MIN = ptsList[teamsList.index(team)]
        pts_MAX = ptsList[teamsList.index(team)]
      if i != 0:
        if pts_MIN > ptsList[teamsList.index(team)]:
          pts_MIN = ptsList[teamsList.index(team)]
        if pts_MAX < ptsList[teamsList.index(team)]:
          pts_MAX = ptsList[teamsList.index(team)]
      if i >= 2:
        ptsNoVarList = data[f'Pts (No VAR)(20{i + 17}/{i + 18})'].tolist()
        ptsNoVar.append(ptsNoVarList[teamsList.index(team)])
        pts_titleNoVar.append (f'20{i + 17}/{i + 18}')

    pts_LIMITS = (lowest10(pts_MIN), highest10(pts_MAX)) 


    count = 0
    def animate(i):
      global count
      x = returnElements(pts_title, count) # Sets extent of seasons (x-axis)
      y = returnElements(pts, count) # Sets trajectory of line plot (y-axis)
      
      plt.cla() # clear axis after plotting individual lines
      plt.plot(x, y, label = 'Actual Pts (VAR since 2019/20)') # selecting the x and y variables to plot

      # VAR introduction in 2019/20 season: Introduce new line
      if count >= 3:
        x_1 = returnElements(pts_titleNoVar, count - 2)
        x_1.insert(0, pts_title[1])
        y_1 = returnElements(ptsNoVar, count - 2)
        y_1.insert(0, pts[1])
        plt.plot(x_1, y_1, label = 'Pts (Excluding VAR since 2019/20)')
        
      plt.xlabel('Seasons') # label x axis
      plt.ylim((pts_LIMITS[0], pts_LIMITS[1])) # Set limits according to point interval between seasons
      plt.ylabel('Pts') # label y axis
      plt.legend()
      plt.title(f'Premier League Pts (2017-22): {team}')

      count += 1

    ani = FuncAnimation(plt.figure(), animate, interval = 500, frames = (season_cnt - 1), repeat = False)
    
    # Use when matplotlib works: plt.show()
    # Use to save gif:
    team_title = ''
    match team:
       case "Man City": team_title = 'man-city'
       case "Man Utd": team_title = 'man-utd'
       case "Tottenham": team_title = 'spurs'
       case "Liverpool": team_title = 'liverpool'
       case "Chelsea": team_title = 'chelsea'
       case "Arsenal": team_title = 'arsenal'
       case "Burnley": team_title = 'burnley'
       case "Everton": team_title = 'everton'
       case "Leicester City": team_title = 'leicester'
       case "Newcastle Utd": team_title = 'newcastle'
       case "Crystal Palace": team_title = 'crystal-palace'
       case "West Ham": team_title = 'west-ham'
       case "Brighton": team_title = 'brighton'
       case "Southampton": team_title = 'soton'
       case _: team_title = 'test'
    
    ani.save(f'preAnimation_{team_title}.gif', writer='pillow', fps=1)
    convert(f'preAnimation_{team_title}.gif', f'GP2_{team_title}.gif', 500) # no loop
    
except Exception as ex:
    print(f'Error: [{str(ex)}]')
