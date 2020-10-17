class Url_Helper:
	
	def join(*route_segments):
		route = ""
		for seg in route_segments:
			route += seg + "/"
		return route[:-1]