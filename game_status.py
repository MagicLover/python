class GameStatus():
	"""跟踪游戏的统计信息"""
	
	def __init__(self,ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_status()
		self.game_active = False
		#任何情况下都不应该重置最高得分
		self.high_score = 0

	def reset_status(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1

