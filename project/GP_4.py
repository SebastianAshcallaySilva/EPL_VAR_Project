# -*- coding: utf-8 -*-

import requests
import pandas as pd

team_legend = {
    'Bournemouth': 'AFC Bournemouth',
    'Nottm Forest': 'Nottingham Forest' ,
    'Newcastle': 'Newcastle United',
    'Wolves': 'Wolverhampton Wanderers',
    'West Ham': 'West Ham United',
    'Leeds': 'Leeds United',
    'Tottenham': 'Tottenham Hotspur'
}

# Retrieve information for 2022/23 season via URL
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
  start = html.find('net score')
  br = html.find('<br>', start)
  h2 = html.find('<h2>', br)
  for i in range(20):
    href_start = h2
    name_start = html.find('class="">', href_start)
    name_end = html.find('</a>', name_start + 9)
    name = html[name_start + 9:name_end]
    teams.append(name)
    h2 = html.find('<h2>', name_end)
  
  return teams

def getNetScores(html):
  net = []
  start = html.find('net score')
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

def getDecisionsAgainst(html):
  against = []
  teams = []
  start = html.find('- decisions')
  br = html.find('<br>', start)
  name_start = html.find('class="">', br)
  for i in range(20):
    name_end = html.find('</a>', name_start + 9)
    name = html[name_start + 9: name_end]
    teams.append(name)
    ag_start = html.find(' ', name_end)
    h2_end = html.find('</h2>', name_end)
    ag = html[ag_start + 1:h2_end]
    against.append(int(ag))

    name_start = html.find('class="">', h2_end)
  
  teamAgainst = {teams[i]: against[i] for i in range(len(teams))}

  return teamAgainst

def getDecisionsFor(html):
  favor = []
  teams = []
  i = html.find('- decisions')
  start = html.find('- decisions', i + 30)
  br = html.find('<br>', start + 10)
  name_start = html.find('class="">', br)
  for i in range(20):
    name_end = html.find('</a>', name_start + 9)
    name = html[name_start + 9: name_end]
    teams.append(name)
    fv_start = html.find(' ', name_end)
    h2_end = html.find('</h2>', name_end)
    fv = html[fv_start + 1:h2_end]
    favor.append(int(fv))

    name_start = html.find('class="">', h2_end)
  
  teamAgainst = {teams[i]: favor[i] for i in range(len(teams))}

  return teamAgainst

def getTeams_Placed(html):
  teamsP = []
  name_start = html.find('<abbr style="text-decoration:none" title="')
  for i in range(20):
    name_end = html.find('"', name_start + 43)
    name = html[name_start + 42: name_end]
    if '&amp;' in name: # ampersand
      name  = name[:name.find('&')] + '&' + name[name.find(';') + 1:]
    if name in team_legend.values():
      name = [k for k, v in team_legend.items() if v == name][0]
    teamsP.append(name)
    name_start = html.find('<abbr style="text-decoration:none" title="', name_end)

  return teamsP 

def getStats(html, stat):
  games = []
  wins = []
  draws = []
  losses = []
  goalsF = []
  goalsA = []
  goalDiff = []
  pts = []

  lenTD = '<td class="Table__TD"><span class="stat-cell">'
  data_start = html.find(lenTD) + len(lenTD)
  for i in range(20):
    # append games
    game_end = html.find('<', data_start + 1)
    game = (html[data_start: game_end]).strip()
    games.append(game)

    # append wins
    win_start = html.find(lenTD, game_end) + len(lenTD)
    win_end = html.find('<', win_start + 1)
    win = int((html[win_start: win_end]).strip())
    wins.append(win)

    # append draws
    draw_start = html.find(lenTD, win_end) + len(lenTD)
    draw_end = html.find('<', draw_start + 1)
    draw = int((html[draw_start: draw_end]).strip())
    draws.append(draw)

    # append losses
    loss_start = html.find(lenTD, draw_end) + len(lenTD)
    loss_end = html.find('<', loss_start + 1)
    loss = int((html[loss_start: loss_end]).strip())
    losses.append(loss)

    # append goals in favor
    gf_start = html.find(lenTD, loss_end) + len(lenTD)
    gf_end = html.find('<', gf_start + 1)
    gf = int((html[gf_start: gf_end]).strip())
    goalsF.append(gf)

    # append goals against
    ga_start = html.find(lenTD, gf_end) + len(lenTD)
    ga_end = html.find('<', ga_start + 1)
    ga = int((html[ga_start: ga_end]).strip())
    goalsA.append(ga)

    # append goal difference
    lenTD_pos = '<span class="stat-cell clr-'
    gdiff_start = html.find(lenTD_pos, ga_end) + len(lenTD_pos) + 10
    gdiff_end = html.find('<', gdiff_start + 1)
    gdiff = sign((html[gdiff_start: gdiff_end]).strip())
    goalDiff.append(gdiff)

    # append pts
    pt_start = html.find(lenTD, gdiff_end) + len(lenTD)
    pt_end = html.find('<', pt_start + 1)
    pt = int((html[pt_start: pt_end]).strip())
    pts.append(pt)

    # restarts
    data_start = html.find(lenTD, pt_end) + len(lenTD)
  
  if stat.lower() == 'games':
    return games
  elif stat.lower() == 'wins':
    return wins
  elif stat.lower() == 'losses':
    return losses
  elif stat.lower() == 'draws':
    return draws
  elif stat.lower() == 'goals_f':
    return goalsF
  elif stat.lower() == 'goals_a':
    return goalsA
  elif stat.lower() == 'goal_diff':
    return goalDiff
  elif stat.lower() == 'points':
    return pts
  else:
    print('Error: [Option chosen is not compatible with list of options]')

def getHTML_html_season(season):
  links = {'2022/23': ('https://www.espn.com/soccer/story/_/id/37631044/how-var-decisions-affected-every-premier-league-club-2022-23',
                       'htmls/html[22_23].html'),
           '2021/22': ('https://www.espn.com/soccer/english-premier-league/story/4452736/how-var-decisions-have-affected-every-premier-league-club-in-2021-22',
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

def getHTML_table_season(season):
  links = {'2022/23': ('https://www.espn.com/soccer/story/_/id/37631044/how-var-decisions-affected-every-premier-league-club-2022-23',
                       'tables/table[22_23].html'),
           '2021/22': ('https://www.espn.com/soccer/english-premier-league/story/4452736/how-var-decisions-have-affected-every-premier-league-club-in-2021-22',
                       'tables/table[21_22].html'),
           '2020/21': ('https://www.espn.com/soccer/english-premier-league/story/4182135/how-var-decisions-affected-every-premier-league-club-in-2020-21',
                       'tables/table[20_21].html'),
           '2019/20': ('https://www.espn.com/soccer/english-premier-league/story/3929823/how-var-decisions-have-affected-every-premier-league-club',
                       'tables/table[19_20].html')}
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

def program():
  try:
    print()
    htmlN = getHTML_html_season('2022/23')
    seasonN = getSeason(htmlN)
    teamsN = getTeams(htmlN)
    netN = getNetScores(htmlN)
    teams_against = getDecisionsAgainst(htmlN)
    teams_for = getDecisionsFor(htmlN)

    teamNet = {teamsN[i]: netN[i] for i in range(len(teamsN))}

    htmlStd = getHTML_table_season('2022/23')
    teamsStd = getTeams_Placed(htmlStd)
    pts_VAR = getStats(htmlStd, 'points')
    goalDifference = getStats(htmlStd, 'goal_diff')
    winStd = getStats(htmlStd, 'wins')
    drawStd = getStats(htmlStd, 'draws')
    lossStd = getStats(htmlStd, 'losses')


    # Sort VAR calls against
    teams_against_sorted = []
    for i in range(len(teamsStd)):
      teams_against_sorted.append(teams_against[teamsStd[i]])

    # Sort VAR calls for
    teams_for_sorted = []
    for i in range(len(teamsStd)):
      teams_for_sorted.append(teams_for[teamsStd[i]])

    # Sort Net Scores
    netN_sorted = []
    for i in range(len(teamsStd)):
      netN_sorted.append(teamNet[teamsStd[i]])

    #  Create csv
    position = []
    for i in range(20):
      position.append(i + 1)

    cols = {'Position': position, f'Teams': teamsStd, 'Pts': pts_VAR,
            'GD': goalDifference, 'Wins': winStd, 'Draws': drawStd, 'Losses': lossStd,
            'Net (VAR)': netN_sorted, 'Against (VAR)': teams_against_sorted,
            'For (VAR)': teams_for_sorted}

    df = pd.DataFrame(cols)
    df.to_csv(f'SampleTable{seasonN}.csv')

    print(f"Wrote SampleTable{seasonN}.csv")

  except Exception as ex:
    print(f'Error: [{str(ex)}]')

def main():
  program()

main()