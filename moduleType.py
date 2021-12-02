class moduleType:

	def __init__(self):
		self.course = None
		self.title = None
		self.au = None
		self.course_type =  None
		self.status = None
		self.su_grade = None
		self.index_number = None
		self.class_type = None
		self.day = None
		self.time = None
		self.venue = None
		self.remark = None

	def __str__(self):
		return 'Course: {} \nTitle: {} \nAU: {} \nCourse Type: {} \nStatus: {} \nS/U: {} \nClass Type: {} \nDay: {} \nTime: {} \nVenue: {} \nRemark: {} \n'.format(\
			self.course, self.title, self.au, self.course_type, self.status, self.su_grade, self.class_type, self.day, self.time, self.venue, self.remark)
		



