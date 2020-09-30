def test_get_all_menus(self):
		""" Test API can get all menus."""
		self.menu = {
			"name": "KFC Special",
			"description": "Finger lickin chicken"
		}
		response = self.app.post("/api/v1/menus", data = self.menu)
		self.assertEqual(response.status_code, 201)
		response = self.app.get("/api/v1/menus")
		self.assertEqual(response.status_code, 200)
		self.assertIn(self.menu["name"], str(response.data))
		self.assertIn('Finger lickin', str(response.data))

	def test_update_a_menu(self):
		""" Test API can update a menu. """
		self.menu = {
			"name": "KFC Special",
			"description": "Finger lickin chicken"
		}
		response = self.app.post("/api/v1/menus", data = self.menu)
		self.assertEqual(response.status_code, 201)
		self.menu = {
			"name": "KFC Special 3",
			"description": "Just Eat Finger lickin chicken..."
		}
		response = self.app.put("/api/v1/menus/1", data = self.menu)
		self.assertEqual(response.status_code, 201)