"""
Main file which should Ultimately represent 'Ticket-To-Ride' and provide an agent with responses to queries about the state of the game to facilitate
decision making via minimax
"""


from algo import search


cities = {}
cities['vancouver']={'seattle':('grey',1),'calgary':('grey',3)}
cities['calgary']={'vancouver':('grey',1),'seattle':('grey',4),'helena':('grey',4),'winnipeg':('white',6)}
cities['winnipeg']={'calgary':('white',6),'helena':('blue',4),'duluth':('black',4),'sault st marie':('grey',6)}
cities['sault st marie']={'winnipeg':('grey',6),'duluth':('grey',3),'toronto':('grey',2),'montreal':('black',5)}
cities['montreal']={'sault st marie':('black',5),'toronto':('grey',3),'new york':('blue',3),'boston':[('grey',2),('grey',2)]}

cities['seattle']={'portland':('grey,1'),'helena':('yellow',6),'calgary':('grey',4)}
cities['helena']={'seattle':('yellow',6),'salt lake city':('pink',3),'denver':('green',4),'omaha':('red',5),'duluth':('orange',6)}
cities['duluth']={'helena':('orange',6),'omaha':[('grey',2),('grey',2)],'chicago':('red',3),'toronto':('pink',6)}
cities['toronto']={'duluth':('pink',6),'chicago':('white',4),'pittsburgh':('grey',2),'montreal':('grey',3),'sault st marie':('grey',2)}
cities['boston']={'montreal':[('grey',2),('grey',2)],'new york':[('yellow',2),('red',2)]}

cities['portland']={'san francisco':[('green',6),('pink',6)],'salt lake city':('blue',6),'seattle':('grey',1)}
cities['omaha']={'helena':('red',5),'denver':('pink',4),'kansas city':[('grey',2),('grey',2)],'chicago':('blue',4),'duluth':[('grey',2),('grey',2)]}
cities['chicago']={'duluth':('red',3),'omaha':('blue',4),'saint loius':[('green',2),('white',2)],'pittsburgh':[('orange',3),('black'),3],'toronto':('white',4)}
cities['pittsburgh']={'chicago':[('orange',3),('black',3)],'saint loius':('green',5),'nashville':('yellow',4),'raleigh':('grey',2),'washington':('grey',2),'new york':[('green',2),('white',2)],'toronto':('grey',2)}
cities['new york']={'pittsburgh':[('green',2),('white',2)],'washington':[('orange',2),('black',2)],'boston':[('yellow',2),('red',2)],'montreal':('blue',3)}

cities['san francisco']={'los angeles':[('pink',3),('yellow',3)],'salt lake city':[('red',5),('orange',5)],'portland':[('green',6),('pink',6)]}
cities['salt lake city']={'san francisco':[('red',5),('orange',5)],'las vegas':('orange',3),'denver':[('red',3),('yellow',3)],'helena':('pink',3),'portland':('blue',6)}
cities['denver']={'salt lake city':[('red',3),('yellow',3)],'phoenix':('white',5),'santa fe':('grey',2),'oklahoma city':('red',4),'kansas city':[('black',4),('orange',4)],'omaha':('pink',4),'helena':('green',4)}
cities['kansas city']={'denver':[('black',4),('orange',4)],'oklahoma city':[('grey',2),('grey',2)],'saint loius':[('blue',2),('pink',2)],'omaha':[('grey',1),('grey',1)]}
cities['saint loius']={'kansas city':[('blue',2),('pink',2)],'little rock':('grey',2),'nashville':('grey',2),'pittsburgh':('green',5),'chicago':[('green',2),('white',2)]}
cities['washington']={'pittsburgh':('grey',2),'raleigh':[('grey',2),('grey',2)],'new york':[('orange',2),('black',2)]}

cities['los angeles']={'san francisco':[('pink',3),('yellow',3)],'el paso':('black',6),'phoenix':('grey',3),'las vegas':('grey',2)}
cities['las vegas']={'los angeles':('grey',2),'salt lake city':('orange',3)}
cities['santa fe']={'phoenix':('grey',3),'el paso':('grey',2),'oklahoma city':('blue',3),'denver':('grey',2)}
cities['oklahoma city']={'denver':('red',4),'santa fe':('blue',3),'el paso':('yellow',5),'dallas':[('grey',2),('grey',2)],'little rock':('grey',2),'kansas city':[('grey',2),('grey',2)]}
cities['little rock']={'oklahoma city':('grey',2),'dallas':('grey',2),'new orleans':('green',3),'nashville':('white',3),'saint loius':('grey',2)}
cities['nashville']={'saint loius':('grey',2),'little rock':('white',3),'atlanta':('grey',1),'raleigh':('black',3),'pittsburgh':('yellow',4)}
cities['raleigh']={'nashville':('black',3),'atlanta':[('grey',2),('grey',2)],'charleston':('grey',2),'washington':[('grey',2),('grey',2)],'pittsburgh':('grey',2)}

cities['phoenix']={'los angeles':('grey',3),'el paso':('grey',3),'santa fe':('grey',3),'denver':('white',5)}
cities['el paso']={'phoenix':('grey',3),'los angeles':('black',6),'houston':('green',6),'dallas':('red',4),'oklahoma city':('yellow',5),'santa fe':('grey',2)}
cities['dallas']={'el paso':('red',4),'houston':('grey',1),'little rock':('grey',2),'oklahoma city':[('grey',2),('grey',2)]}
cities['atlanta']={'new orleans':[('yellow',4),('orange',4)],'miami':('blue',5),'charleston':('grey',2),'raleigh':[('grey',2),('grey',2)],'nashville':('grey',1)}
cities['charleston']={'atlanta':('grey',2),'miami':('pink',4),'raleigh':('grey',2)}

cities['houston']={'el paso':('green',6),'new orleans':('grey',2),'dallas':[('grey',2),('grey',2)]}
cities['new orleans']={'houston':('grey',2),'miami':('red',6),'atlanta':[('orange',4),('yellow',4)],'little rock':('green',3)}
cities['miami']={'new orleans':('red',6),'charleston':('pink',4),'atlanta':('blue',5)}





class GameBoard(search.Problem):
	"""docstring for GameBoard"""
	def __init__(self, arg):
		self.cities=arg
		self.takenRoutes=[]


	def actions(self,state):
		
		possibilites=[x for x in self.cities[state].keys() if not self.routeTaken(state,x)]
		return possibilites

	def result(self, state, action): 
		return action
	
	def routeTaken(self,cityA,cityB):
		
		if (cityA,cityB) in self.takenRoutes or (cityB,cityA) in self.takenRoutes:
			return True
		else:
			return False

	def takeRoute(self,cityA,cityB):
		self.takenRoutes.append((cityA,cityB))

	def minRoute(self,cityA,cityB):
		self.goal=cityB
		self.initial=cityA
		return search.breadth_first_search(self)

		
if __name__ == '__main__':
	
	game = GameBoard(cities)
	# game.takeRoute('miami','charleston')
	path = game.minRoute('miami','seattle')
	print path.path()

