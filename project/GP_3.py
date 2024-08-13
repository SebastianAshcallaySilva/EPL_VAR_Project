import requests
import html2text
import matplotlib.pyplot as plt

team_legend = {
    "B'mouth": 'AFC Bournemouth',
    'Nottm Forest': 'Nottingham Forest' ,
    'Newcastle': 'Newcastle United',
    'Wolves': 'Wolverhampton Wanderers',
    'West Ham': 'West Ham United',
    'Leeds': 'Leeds United',
    'Spurs': 'Tottenham Hotspur',
    'Man City': 'Manchester City',
    'Man Utd': 'Manchester United',
    'Brighton': 'Brighton & Hove Albion',
    'C. Palace': 'Crystal Palace',
    'Leicester': 'Leicester City',
    'Sheffield': 'Sheffield United',
    'Norwich': 'Norwich City',
    'Soton': 'Southampton',
}
def printGraph(teamSet, scoreSet, xlabel, ylabel, title):
  # Clear previous graph
  plt.cla()
  # Create the bar chart for season
  plt.bar(teamSet, scoreSet)

  # Add labels and title
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)

  # Rotate x-axis labels for readability
  plt.xticks(rotation=90)
  plt.subplots_adjust(bottom=.25)

  # Display the chart
  plt.show()

def sign(stringNum):
  if '-' in stringNum:
    return int(stringNum)
  elif '0' in stringNum:
    return int(0)
  else:
    return int(stringNum[1:])

def getSeason(html):
  title_start = html.find('<title>')
  season_start = html.find('20', title_start + 1)
  season_end = html.find('-', season_start) + 3
  season = html[season_start: season_end]
  return season

def getTeams(html):
  teams = []
  start = html.find('VAR overturns')
  br = html.find('<br>', start)
  h2 = html.find('<h2>', br)
  for i in range(20):
    href_start = h2
    name_start = html.find('class="">', href_start)
    name_end = html.find('</a>', name_start + 9)
    name = html[name_start + 9:name_end]
    if name in team_legend.values():
      name = [k for k, v in team_legend.items() if v == name][0]
    teams.append(name)
    h2 = html.find('<h2>', name_end)
  
  return teams

def getNetScores(html):
  net = []
  start = html.find('VAR overturns')
  br = html.find('<br>', start)
  h2 = html.find('<h2>', br)
  for i in range(20):
    href_start = h2
    name_start = html.find('class="">', href_start)
    name_end = html.find('</a>', name_start + 9)
    netPts_start = html.find(' ', name_end)
    h2_end = html.find('</h2>', name_end)
    netPts = html[netPts_start + 1:h2_end]
    net.append(sign(netPts))

    h2 = html.find('<h2>', name_end)
  
  return net

def getHTML_txt_season(season):
  links = {'2021/22': ('https://www.espn.com/soccer/english-premier-league/story/4452736/how-var-decisions-have-affected-every-premier-league-club-in-2021-22',
                       'htmls/html[21_22].html'),
           '2020/21': ('https://www.espn.com/soccer/english-premier-league/story/4182135/how-var-decisions-affected-every-premier-league-club-in-2020-21',
                       'htmls/html[20_21].html'),
           '2019/20': ('https://www.espn.com/soccer/english-premier-league/story/3929823/how-var-decisions-have-affected-every-premier-league-club',
                       'htmls/html[19_20].html')}

  link_tup = links.get(season)
  if link_tup is None:
    raise Exception('ERROR: [Season Out of Bounds]')

  try:
    pageN = requests.get(link_tup[0])
    if pageN.status_code != 200:
      raise Exception("WEB SCRAPING ERROR. Turning to HTML file...")
    else:
      return pageN.text
  except Exception as ex:
    with open(link_tup[1], 'r') as file:  # r to open file in READ mode
      return file.read()




try:
  print()
  answer = input('Which season do you want to graph?\n* 2019/20\n* 2020/21\n* 2021/22\n--> ')
  htmlN = getHTML_txt_season(answer)
  print('HTML handled...')
  seasonN = getSeason(htmlN)
  print('Season handled...')
  teamsN = getTeams(htmlN)
  print('Teams handled...')
  netN = getNetScores(htmlN)
  print('Net scores handled...')
  printGraph(teamsN, netN, "Team", "Net Score", f"Premier League VAR overturns - Net Scores: Season {seasonN}")
  print()

except Exception as ex:
  print(f'Error: [{str(ex)}]')
