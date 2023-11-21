from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from Screens.StudentManager.StudentManager import ManageStudent
#from Screens.Attendance.Attendance import Attendance
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window

Builder.load_file("Screens/StudentManager/StudentManager.kv")
#Builder.load_file("Screens/LoginPage/LoginPage.kv")
KV = '''
#<AddStudent>
#	orientation: "vertical"
#	spacing: "10dp"
#	size_hint_y: None
#	#height: "220dp"
#	Label:
#		text: "Wellcome Back"
#		outline_width: "5dp"
#		bold : True
#	MDTextField:
#		hint_text: "Username"
#		mode: "rectangle"
#	MDTextField:
#		hint_text: "Password"
#		mode: "rectangle"
#		password: True


<ContentNavigationDrawer>
	MDList:
		OneLineListItem:
			text: "Manage Student"
			on_press:
				root.nav_drawer.set_state("close")
				root.screen_manager.current = "Manage Student"
		OneLineListItem:
			text: "Student Attendnce"
			on_press:
				root.nav_drawer.set_state("close")
				root.screen_manager.current = "student_attendence"
		OneLineListItem:
			text: "About Developer"
			on_press:
				root.nav_drawer.set_state("close")
				root.screen_manager.current = "scr 3"


								

MDScreen:
	id: main_screen
	MDTopAppBar:
		id: command_selection_bar
		pos_hint: {"top": 1}
		elevation: 4
		title: "Student Attendance Management"
		left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
		# right_action_items: [["menu", lambda x: print("toolbar clicked")]]
	
	MDNavigationLayout:
		MDScreenManager:
			id:screen_manager
			
			Attendance:
				name: "student_attendence"
					
			ManageStudent:
				name: "Manage Student"
				
					
		
		
		MDNavigationDrawer:
			id: nav_drawer
			radius: (0, 16, 16, 0)
			ContentNavigationDrawer:
				screen_manager: screen_manager
				nav_drawer: nav_drawer	
	
'''
Window.softinput_mode = "below_target"
class Attendance(MDScreen):
	pass

class ContentNavigationDrawer(MDScrollView):
	screen_manager = ObjectProperty()
	nav_drawer = ObjectProperty()
	
	
	
class Student_Attendance_MangementApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "LightBlue"
		self.theme_cls.material_style = "M3"
		return Builder.load_string(KV)
		
		
if __name__ == "__main__":
	Student_Attendance_MangementApp().run()