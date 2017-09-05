#Javier Pardo Diaz. Silencing Lab - Elena Caro
#TRABAJO FIN DE GRADO
##Program

import ttk
from ttk import *

import Tkinter
from Tkinter import *
import datetime
from datetime import date

import mysql.connector
from mysql.connector import errorcode
global name
global pwd
global level
global fields_added
global fields_tuple
global fields_selected_tuple
global combobox_tuple
global control
global control2
global control_add
global user_name
global InsertScreen
global action
global SelectConstructionScreen
global OtherScreen
global OtherScreen2


#-------------------------------- FRAME 1 --------------------------------

class Application1(Frame): #Welcome Screen where identification in checked
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		
		self.lbl_intro=Label(text="Welcome to the silencing lab Data Base")
		self.lbl_intro.grid(row=0)

		self.lbl_name=Label(text="Name:").grid(row=1,sticky=W)
		#self.grid()
		self.lbl_pwd=Label(text="Password:").grid(row=2,sticky=W)
		
		self.ent_name=Entry(master) #Entry where writting the user name
		self.ent_name.grid(row=1,column=1)

		self.ent_pwd=Entry(master) #Entry where writting the user password
		self.ent_pwd.config(show = "*") #"Hide" the password
		self.ent_pwd.grid(row=2,column=1)

		self.btn_submit=Button(text="Submit")
		self.btn_submit.grid()
		self.btn_submit["command"]=self.check_identity
	
	def check_identity(self):
                global db
                global user_name
		user_name=self.ent_name.get() #get user's name
		self.pwd=self.ent_pwd.get() #get user's password
		config = {
			'user':user_name,
			'passwd':self.pwd,
			'host':'138.4.138.24', #Server IP
			'database':'constructions'
		}
		global control
		try:
			db=mysql.connector.connect(**config)
			db.autocommit=False
			control=True #Allow access to the next screen; only where user and password are ok
			WelcomeScreen.destroy()
			
		except: #Name or password are wrong
			control=False 
		
#------------------------------------ FRAME 2 --------------------------------------------------
			
class Application2(Frame): #Search panel. Access to other options
	global fields_added
	global level
	global selection

	selection=()

	def __init__(self, master):
		Frame.__init__(self, master)
		self.create_widgets()
		
	def create_widgets(self):
		global fields_added
		global fields_selected_tuple
		global level

		self.lst_lookingfor = Listbox(self) #Listbox to choose which type of construction (Level) is looked for
		self.lst_lookingfor.config(height=5)
		self.lst_lookingfor.grid(row=0, column=0) 
		self.lst_lookingfor.insert(0,"Construction Level 0")
		self.lst_lookingfor.insert(1,"Construction Level 1")
		self.lst_lookingfor.insert(2,"Construction Level 2")
		self.lst_lookingfor.insert(3,"Construction Level M")
		self.lst_lookingfor.insert(4,"Construction Level P")

		self.btn_other=Button(text="Other options")
		self.btn_other.grid(row=0, column=1)
		self.btn_other["command"]=self.other_options

		self.btn_new=Button(text="New Construction")
		self.btn_new.grid(row=0, column=2)
		self.btn_new["command"]=self.new_item

		self.btn_user=Button(text="Users management")
		self.btn_user.grid(row=0, column=3)
		self.btn_user["command"]=self.users

		self.btn_addfield=Button(text="Add Field")
		self.btn_addfield.grid(row=1, column=0)
		self.btn_addfield["command"]=self.add_field
		
		self.btn_cancel=Button(text="Cancel")
		self.btn_cancel.grid(row=1, column=1)
		self.btn_cancel["command"]=self.cancel
		self.btn_cancel.config( state = DISABLED )

		self.btn_search=Button(text="Search")
		self.btn_search.grid(row=1, column=2)
		self.btn_search["command"]=self.search

		self.btn_exit=Button(text="Exit")
		self.btn_exit.grid(row=1, column=3)
		self.btn_exit["command"]=self.exit

		self.grid()
		
		global fields_0 #Listboxes that can be added. There can be selected de field that is wanted to add for searching
		global fields_1
		global fields_2
		global fields_3
		global fields_4
		global fields_5
		global fields_6
		global fields_7
		global fields_8

		fields_selected_tuple=[] #Tuple where the listbox selections are stored

		global fields_0_1 #Comboboxes that appears when pressing "Options". There appear all the possible values for the field selected at Listboxes (fields_X)
		global fields_1_1
		global fields_2_1
		global fields_3_1
		global fields_4_1
		global fields_5_1
		global fields_6_1
		global fields_7_1
		global fields_8_1

		fields_0=Listbox(self)
		fields_1=Listbox(self)
		fields_2=Listbox(self)
		fields_3=Listbox(self)
		fields_4=Listbox(self)
		fields_5=Listbox(self)
		fields_6=Listbox(self)
		fields_7=Listbox(self)
		fields_8=Listbox(self)

		fields_0_1=ttk.Combobox(self.master, state="normal")
		fields_1_1=ttk.Combobox(self.master, state="normal")
		fields_2_1=ttk.Combobox(self.master, state="normal")
		fields_3_1=ttk.Combobox(self.master, state="normal")
		fields_4_1=ttk.Combobox(self.master, state="normal")
		fields_5_1=ttk.Combobox(self.master, state="normal")
		fields_6_1=ttk.Combobox(self.master, state="normal")
		fields_7_1=ttk.Combobox(self.master, state="normal")
		fields_8_1=ttk.Combobox(self.master, state="normal")
                
                level={(0,):"0", #Level 0
                       (1,):"1", #Level 1
                       (2,):"2", #Level 2
                       (3,):"M", #Level M
                       (4,):"P"} #Level P


        def other_options(self):
                
                global OtherScreen
                

                SearchScreen.wm_state('iconic') #hide ResultScreen
                OtherScreen=Tk()
                OtherScreen.title("Other Options")
                OtherScreen.geometry("600x500")
                Application7(OtherScreen) #Show ConstrutionScreen

                OtherScreen.mainloop()

        def users(self):

                global UserScreen

                SearchScreen.wm_state('iconic') #hide ResultScreen
                UserScreen=Tk()
                UserScreen.title("Users Management")
                UserScreen.geometry("600x500")
                Application10(UserScreen) #Show ConstrutionScreen

                UserScreen.mainloop()

        

                
	def new_item(self):
                
                global selection
                global level
                global control_add
                global InsertScreen
                
                selection=self.lst_lookingfor.curselection()

                if selection !=():
                        SearchScreen.wm_state('iconic') #hide ResultScreen
                        InsertScreen=Tk()
                        InsertScreen.title("Insert new item - Construction Level "+level[selection])
                        InsertScreen.geometry("600x500")
                        control_add=False
                        Application5(InsertScreen) #Show ConstrutionScreen

                        InsertScreen.mainloop()

                
                
	
	def add_field(self): #Add a new fields-Listbox (fields_X) to the Search pannel

		global fields_added #Number of field-Listboxes (fields_X) that have been added
		global fields_tuple
		global combobox_tuple
		global selection #Construction level (0 - Level 0; 1 - Level 1; 2 - Level 2; 3 - Level M; 4 - Level P) that is loooked for
		global fields_0
		global fields_1
		global fields_2
		global fields_3
		global fields_4
		global fields_5
		global fields_6
		global fields_7
		global fields_8
		
	
		fields_tuple=[fields_0,fields_1,fields_2,fields_3,fields_4,fields_5,fields_6,fields_7,fields_8] #Tuple that contains all the field - listboxes
		combobox_tuple=[fields_0_1,fields_1_1,fields_2_1,fields_3_1,fields_4_1,fields_5_1,fields_6_1,fields_7_1,fields_8_1] #Tuple that contains all the values- comboboxes

		try:
                        if fields_added >= 0: 
				fields_added = fields_added+1
				if fields_added==8:
                                        self.btn_addfield.config( state = DISABLED ) #There can't be added more listboxes
                                        
		except: #This block is executed when adding the 1st listbox (fields_added is not defined)
			selection=self.lst_lookingfor.curselection() #Check which type (level) of construction is looked for
			self.lst_lookingfor.config( state = DISABLED ) #Disable the listbox where the type of construction is selected
			fields_added=0

		
		if selection == ():
			fields_added="a" #If there's no selection -> When pressing again "Add field" button the "except block" will be executed
			self.lst_lookingfor.config( state = NORMAL ) #Enable the listbox where the type of construction is selected

                #Populate the new list box with different fields for each construction-level by calling a function
			
		else:
                        options={(0,):["DNA type","DNA name", "Construction name","Start position","End position", "Vector", "Resistance", "Domesticated for", "Glycerol"], #Level 0
                                 (1,):["Construction name","DNA name","Vector","Resistance","Position", "Orientation","Organism", "Glycerol", "Level 0 Construction"], #Level 1
                                 (2,):["Construction name","DNA name","Vector","Resistance","First Position","Last Position", "Organism", "Glycerol","Level 0 Construction","Level 1 Construction","Level M Construction","Level P Construction"], #Level 2
                                 (3,):["Construction name","DNA name","Vector","Resistance","First Position","Last Position", "Organism", "Glycerol","Level 0 Construction","Level 1 Construction","Level M Construction","Level P Construction"], #Level M
                                 (4,):["Construction name","DNA name","Vector","Resistance","First Position","Last Position", "Organism", "Glycerol","Level 0 Construction","Level 1 Construction","Level M Construction","Level P Construction"]} #Level P

                        options_to_add=options[selection]
                        campo=self.Field(fields_tuple[fields_added],options_to_add)


		if fields_added == 0: #If it is the 1st time a listbox is added, create "Options" button
                        self.btn_options=Button(text="Options")
                        self.btn_options.grid()
                        self.btn_cancel.config( state = NORMAL )
                        self.btn_options["command"]=self.options
                
		return
                        
	class Field(): #Function that creates Listbox objects. Arguments: Object name and tuple with options to add
                global fields_added
		name=Listbox
		options=[]
		def __init__(self,Name,Op):
			self.name=Name
			self.options=Op
			self.name.grid(row=fields_added+3)
			self.name.config(height=1)
			for index in range(len(self.options)):
                                self.name.insert(index,self.options[index])

        def options(self): #Function that is called by pressing "Option" button. Gets the values for comboboxes by querying the DB. Calls to another function that creates the comboboxes

                global selection
                global fields_tuple
                global fields_selected_tuple
                global level
               
                self.btn_options.grid_forget() #Hide "Option" and "Add field" buttons
                self.btn_addfield.grid_forget()
                self.lst_lookingfor.grid_forget() #Hide the listbox for selecting the type (level) construction
                
                self.grid_forget()

                #The options (values) shown are different depending on the type (level) of construction chosen and the field selected on the listbox (fields_X)


                querys_0={0:"SELECT type from DNA group by type order by name", #DNA type
                          1:"SELECT code, name from DNA order by name", #DNA name
                          2:"SELECT code, name from construction_level_0 order by name", #Construction name
                          3:"SELECT number,left_code from pieces where number not LIKE 'P%' and not LIKE 'EL'" , #Start code
                          4:"SELECT number,right_code from pieces where number not LIKE 'P%' and not LIKE 'EL'" , #End code
                          5:"SELECT code, name from vector where level=0 order by name", #Vector
                          6:"SELECT code, name from antibiotic order by name", #Resistance
                          7:"SELECT code, name from enzymes order by name", #Domesticated
                          8:"SELECT id from glycerol where type='level0' order by id"} #Glycerol


                
                querys_other={0:"SELECT code, name from construction_level_"+level[selection]+" order by name", #Constrution name
                              1:"SELECT code, name from DNA order by name", #DNA name
                              2:"SELECT code, name from vector where level="+level[selection]+" order by name", #Vector
                              3:"SELECT code, name from antibiotic order by name", #Resitance
                              4:"SELECT number from pieces where number LIKE 'P%' or number LIKE 'EL'", #End/start position
                              5:"SELECT orientation from vector where orientation IS NOT NULL group by orientation", #Orientation
                              #6:"SELECT code, name from enzymes order by name", #Domesticated
                              6:"SELECT code, name from organisms order by name", #Used
                              7:"SELECT id from glycerol where type='level"+level[selection]+"' order by id", #Glycerol
                              8:"SELECT code, name from construction_level_0 order by name", #Construction Level 0
                              9:"SELECT code, name from construction_level_1 order by name", #Construction Level 1
                              10:"SELECT code, name from construction_level_M order by name", #Construction Level M
                              11:"SELECT code, name from construction_level_P order by name"} #Construction Level P
                
                querys={(0,):querys_0, #Level 0
                        (1,):querys_other, #Level 1
                        (2,):querys_other, #Level 2
                        (3,):querys_other, #Level M
                        (4,):querys_other} #Level P
                        
                 
                for i in range(0, len(fields_tuple)): #Check each element in fields_tuple
                        field_selected=fields_tuple[i].nearest(1) #Check which field in the Listbox (fields_X) has been chosen (the nearest option to the position 1)
                        if field_selected != -1:

                                fields_selected_tuple=fields_selected_tuple+[field_selected] #Tuple where the "fields" selected are stored

                                if (selection!=(1,) and selection != (0,)) and field_selected==5:
                                        query_search=4
                                else:
                                        query_search=field_selected
                                        
                                query=querys[selection][query_search]
                                data=self.execute_query(query) #Execute the query to get the values (this values will appear in the comboboxes)
                                self.show_combobox(data,i,field_selected)
                                       
                
        def show_combobox(self,data,i,field_selected): #Function that creates comboboxes (fields_1_X)

                global fields_tuple
                global combobox_tuple
                global fields_added

                string_field_selected=fields_tuple[i].get(field_selected) #Get the "title" for the combobox from listbox (fields_X)
                fields_tuple[i].grid_forget() #Hide listbox (fields_X)
                combo_options=[]
                for row in data: #Each option is added to the tuple combo_options
                        try:
                                combo_options=combo_options+[row[0]+" - "+row[1]]
                        except:
                                combo_options=combo_options+[row[0]]
                                
                combo_options=[string_field_selected]+combo_options
                combobox_tuple[i]["values"]=combo_options
                combobox_tuple[i].current(0)
                combobox_tuple[i].grid()
                return
                
        def search(self): #Function that with all the options selected before "choose" which tables should be used. Creates the query and executes it.

                global control
                global control2
                global selection
                global fields_selected_tuple
                global combobox_tuple
                global db
                global level
                global search_result
                

  
                selection2=self.lst_lookingfor.curselection()
                if selection2 !=():
                        selection=selection2
                
                if selection != (): #check if at least a type of construction has been selected
                        control=False #search panel wont be shown again
                        control2=True #result panel will be shown

                        
                        tables="construction_level_"+level[selection]+", vector" #concatenation of tables that will be used in the search (from...). The first table is the table that contains the level selected-tables
                        conditions=" construction_level_"+level[selection]+".vector=vector.code and " #concatenation of conditions that will be used in the search (where... clauses)
                        params=[] #parameters that are given when the query is executed


                        #foreach level, 2 dictionaries are created: the 1st one contains the tables that must be considered (it depends on the option chosen in the comboboxes)
                        #the 2nd one contains


                        tables_0={0:["DNA","level0_DNA"], #DNA type
                                  1:["level0_DNA"], #DNA name
                                  2:[], #Construction name
                                  3:[], #Start code
                                  4:[], #Left code
                                  5:[], #Vector
                                  6:["resistance"], #Resistance
                                  7:["domesticated"], #Domesticated
                                  8:[]} #Glycerol

                        tables_1={0:[], #Cons name
                                  1:["contains_01","level0_DNA","DNA"], #DNA name
                                  2:[], #Vector
                                  3:["resistance"], #Resistance
                                  4:[], #Position
                                  5:[], #Orientation
                                  6:["used"], #Organism
                                  7:[], #Glycerol
                                  8:["contains_01"]} #Level 0

                        tables_2={0:[], #Cons name
                                  1:["contains_01","level0_DNA","DNA"], #DNA name
                                  2:[], #Vector
                                  3:["resistance"], #Resistance
                                  4:["contains_12","contains_M2","construction_level_1"], #Position 1st
                                  5:[], #last
                                  6:["used","contains_12"], #Organism
                                  7:[], #Glycerol
                                  8:["contains_01"],#Level 0
                                  9:["contains_1"+level[selection]],
                                  10:["contains_M"+level[selection]],
                                  11:["contains_M2","contains_PM"]}

                        tables_M={0:[], #Cons name
                                  1:["contains_01","level0_DNA","DNA"], #DNA name
                                  2:[], #Vector
                                  3:["resistance"], #Resistance
                                  4:[], #Position 1st
                                  5:[], #last
                                  6:["used"], #Organism
                                  7:[], #Glycerol
                                  8:["contains_01"],#Level 0
                                  9:["contains_1"+level[selection]],
                                  10:["contains_M1","contains_1M"],
                                  11:["contains_P"+level[selection]]}
                        
                        tables_P={0:[], #Cons name
                                  1:["contains_01","level0_DNA","DNA"], #DNA name
                                  2:[], #Vector
                                  3:["resistance"], #Resistance
                                  4:[], #Position 1st
                                  5:[], #last
                                  6:["used"], #Organism
                                  7:[], #Glycerol
                                  8:["contains_01"],#Level 0
                                  9:["contains_1M","contains_MP"],
                                  10:["contains_M"+level[selection]],
                                  11:["contains_PM","contains_MP"]} 

                        where_0={0:"construction_level_0.code=level0_DNA.construction_0 and level0_DNA.DNA_inserted_code=DNA.code and DNA.type= %s", #DNA type
                                 1:"construction_level_0.code=level0_DNA.construction_0 and level0_DNA.DNA_inserted_code= %s", #DNA name
                                 2:"construction_level_0.code= %s", #Construction name
                                 3:"construction_level_0.5_end= %s", #Start code
                                 4:"construction_level_0.3_end= %s", #Left code
                                 5:"construction_level_0.vector= %s", #Vector
                                 6:"construction_level_0.vector=resistance.vector_code and resistance.antibiotic_code= %s and resistance.position='OUT'", #Resistance
                                 7:"cconstruction_level_0.code=domesticated.construction_code and domesticated.enzyme= %s", #Domesticated
                                 8:"construction_level_0.code= %s"} #Glycerol

                        where_1={0:"construction_level_"+level[selection]+".code= %s", #Construction name
                                 1:"construction_level_"+level[selection]+".code=contains_01.construction_1_code and contains_01.construction_0_code=level0_DNA.construction_0 and level0_DNA.DNA_inserted_code = %s", #DNA name
                                 2:"construction_level_"+level[selection]+".vector= %s", #Vector
                                 3:"construction_level_"+level[selection]+".vector=resistance.vector_code and resistance.antibiotic_code= %s and resistance.position='OUT'", #Resistance
                                 4:"construction_level_"+level[selection]+".is_a= %s", #Position
                                 5:"construction_level_"+level[selection]+".vector=vector.code and vector.orientation= %s",#Orientation
                                 6:"construction_level_"+level[selection]+".code=used.construction_1_code and used.organismdomesticated.construction_code and domesticated.enzyme= %s", #Organism
                                 7:"construction_level_"+level[selection]+".code= %s", #Glycerol
                                 8:"construction_level_"+level[selection]+".code=contains_01.construction_1_code and contains_01.construction_0_code= %s"} #Level 0

                        #In these dictionarys some of the "options" are the same that in "where_1". In that cases, where_1 dictionary is referenced
                        where_2={0:where_1[0], #Construction name
                                 1:"", #DNA name
                                 2:where_1[2], #Vector
                                 3:where_1[3], #Resistance
                                 4:"construction_level_"+level[selection]+".code=contains_12.construction_2_code and contains_12.construction_1_code=construction_level_1.code and contains_12.position='1' and construction_level_1.is_a= %s" , #1st Position
                                 5:"", #last position
                                 6:"", #Organism
                                 7:where_1[8], #Glycerol
                                 8:"", #Level 0
                                 9:"construction_level_"+level[selection]+".code=contains_1"+level[selection]+".construction_"+level[selection]+"_code and contains_1"+level[selection]+".construction_1_code= %s"  ,#Level 1
                                 10:"construction_level_"+level[selection]+".code=contains_M"+level[selection]+".construction_"+level[selection]+"_code and contains_M"+level[selection]+".construction_M_code= %s"  ,#Level M
                                 11:"construction_level_2.code=contains_M2.construction_2_code and contains_M2.construction_M_code=contains_PM.construction_M_code and contains_PM.construction_P_code %s"}#Level P

                        where_M={0:where_1[0], #Construction name
                                 1:"", #DNA name
                                 2:where_1[2], #Vector
                                 3:where_1[3], #Resistance
                                 4:"", #1st Position
                                 5:"", #last position
                                 6:"", #Organism
                                 7:where_1[8], #Glycerol
                                 8:"", #Level 0
                                 9:where_2[9],#Level 1
                                 10:"construction_level_M.code=contains_1M.construction_M_code and contains_1M.construction_1_code=contains_M1.construction_1_code and construction_M1.construction_M_code= %s"  ,#Level M
                                 11:"construction_level_"+level[selection]+".code=contains_P"+level[selection]+".construction_"+level[selection]+"_code and contains_P"+level[selection]+".construction_P_code= %s"}#Level P

                        where_P={0:where_1[0], #Construction name
                                 1:"", #DNA name
                                 2:where_1[2], #Vector
                                 3:where_1[3], #Resistance
                                 4:"", #1st Position
                                 5:"", #last position
                                 6:"", #Organism
                                 7:where_1[8], #Glycerol
                                 8:"", #Level 0
                                 9:"construction_level_P.code=contains_MP.construction_P_code and contains_MP.construction_M_code=contains_1M.construction_M_code and contains_1M.construction_1_code =%s" ,#Level 1
                                 10:where_2[10],#Level M
                                 11:"construction_level_P.code=contains_MP.construction_P_code and contains_MP.construction_M_code=contains_PM.construction_M_code and construction_PM.construction_P_code= %s"}#Level P

                        
                        tables_dictionary={(0,):tables_0, #Level 0
                                           (1,):tables_1, #Level 1
                                           (2,):tables_2, #Level 2
                                           (3,):tables_M, #Level M
                                           (4,):tables_P} #Level P

                        conditions_dictionary={(0,):where_0, #Level 0
                                               (1,):where_1, #Level 1
                                               (2,):where_2, #Level 2
                                               (3,):where_M, #Level M
                                               (4,):where_P} #Level P
                                       
                        for i in range(0, len(fields_selected_tuple)): #check the value that have been chosen in each combobox
                                index=combobox_tuple[i].current()
                                if index != 0:  #check that some possible value has been chosen

                                        value=combobox_tuple[i].get()
                                        code=value.split(' - ') #get the code
                                        tables_needed=tables_dictionary[selection][fields_selected_tuple[i]] #tables needed for that search

                                        for table in tables_needed:
                                                if tables.find(" "+table)== -1 and tables.find(table+",")== -1:
                                                        tables=tables+", "+table #each table is added only if it has not been added yet (can't be duplicated tables)
                                       
                                        params=params+[code[0]] #the code of the option chosen is stored. it will be used in the query
                                        conditions=conditions+conditions_dictionary[selection][fields_selected_tuple[i]]+" and " #the "condition" clause is added

                        conditions=conditions[:-5] #when all conditions have been added, the last " and " is removed
                        
                        #create the query (adding tables and conditions)

                        query="SELECT DISTINCT construction_level_"+level[selection]+".code, construction_level_"+level[selection]+".name, vector.name, construction_level_"+level[selection]+".comment from "+tables+" where "+conditions

                        #cursor.execute(query,params)
                        cursor=db.cursor()
                        cursor.execute(query,params)
                        search_result=cursor.fetchall()
                                                                              
                        self.cancel()
                
        
        def cancel(self):
                global selection
                global fields_added

                fields_added="a" #When the search panel re-appears, the except block in the add_field function will be executed

                if control2==False:
                        selection=()
                SearchScreen.eval('::ttk::CancelRepeat')
                SearchScreen.destroy()
                
	def exit(self):
                global control
                control=False #search panel wont be shown again
                SearchScreen.destroy()

        def execute_query(self,query): #fuction that access to the DB and execute a query (argument). Returns all the rows obtined
                
                global db
                cursor=db.cursor()
                cursor.execute(query)
                data=cursor.fetchall()
                return data
		
#------------------------------------ FRAME 3 --------------------------------------------------
			
class Application3(Frame): #Result Panel
	global fields_added

	def __init__(self, master):
		Frame.__init__(self, master)
		self.create_widgets()
		
	def create_widgets(self):
		global fields_added
		global search_result

		
		if len(search_result)>0: #There are constructions that match with the selection
                        

                        global v #Variable where selection is stored
                        self.lbl_result_title=Label(text="CONSTRUCTIONS FOUND AFTER LOOKING FOR",font=('Helvetica',20))
                        self.lbl_result_title.grid(columnspan=4)

                        self.lbl_result_header1=Label(text="Glycerol")
                        self.lbl_result_header2=Label(text="Name")
                        self.lbl_result_header3=Label(text="Vector")
                        self.lbl_result_header4=Label(text="Comment")
                        self.lbl_result_header1.grid(row=1,column=0)
                        self.lbl_result_header2.grid(row=1,column=1)
                        self.lbl_result_header3.grid(row=1,column=2)
                        self.lbl_result_header4.grid(row=1,column=3)
                        
                        v = StringVar()


                        for i in range (0, len(search_result)): #Show the information of each result
                                
                                self.lbl_result1=Label(text=search_result[i][0])
                                self.lbl_result2=Label(text=search_result[i][1])
                                self.lbl_result3=Label(text=search_result[i][2])
                                self.lbl_result4=Label(text=search_result[i][3])

                                #Associate a radiobutton to each result. The value associated is the construction code
                                self.rbt_result=Radiobutton (variable=v, value=search_result[i][0], command=self.active_button) 
                                
                                self.lbl_result1.grid(row=2+i,column=0,sticky='W')
                                self.lbl_result2.grid(row=2+i,column=1,sticky='W')
                                self.lbl_result3.grid(row=2+i,column=2,sticky='W')
                                self.lbl_result4.grid(row=2+i,column=3,sticky='W')
                                self.rbt_result.grid(row=2+i,column=4,sticky="E")

                                

                        self.btn_result=Button(text="Show")                                       
                        self.btn_result.grid(columnspan=4)
                        self.btn_result["command"]=self.show_result_panel
                        self.btn_result["state"]='disabled'#Until an option is chosen, it is impossible to show construction information
                        
                        

     
                else:
                        self.lbl_result_title=Label(text="NO RESULTS",font=('Helvetica',20))
                        self.lbl_result_title.grid()



		self.btn_newsearch=Button(text="New Search")
		self.btn_newsearch.grid(columnspan=4)
		self.btn_newsearch["command"]=self.new_search

        def active_button(self): #It takes place when some radiobutton option is selected

                self.btn_result["state"]='normal' #Now it is possible to show the information of the construction selected

		
	def show_result_panel(self):

                global v #It contains the code of the seleted construction
                #global show_construction
                code=v.get() #get the code from the radiobutton 
                ResultScreen.wm_state('iconic') #hide ResultScreen

                ConstructionScreen=Tk()
                ConstructionScreen.title(code)
                ConstructionScreen.attributes('-fullscreen',True)
                Application4(ConstructionScreen,code) #Show ConstrutionScreen
                ResultScreen.mainloop()
                
		
	def new_search(self):
                global control
                global control2

                control=True #Search panel is shown
                control2=False #Result panel is not shown
                
                ResultScreen.destroy()


#------------------------------------ FRAME 4 --------------------------------------------------
			
class Application4(Frame): #Construction Panel
        

	def __init__(self, master,code):
		Frame.__init__(self, master)
		self.lbl_glycerol=Label(master,text="Glycerol number: "+code,font="Helvetica 20 bold")
		self.lbl_glycerol.grid(row=0,column=0,columnspan=6)
		self.look_for_info(master,code)

	def look_for_info(self,master,code):

                global db
                global selection
                global level
                
                #depending on the construction level, some addiotional information is looked for
                add_query={(0,):", construction_level_0.5_end, construction_level_0.3_end, construction_level_0.forward_primer, construction_level_0.reverse_primer",#Level 0
                           (1,):", construction_level_1.is_a, vector.orientation, construction_level_1.marker", #Level 1
                           (2,):"",
                           (3,):"",
                           (4,):""}

                query="SELECT glycerol.comment, glycerol.date, construction_level_"+level[selection]+".name, construction_level_"+level[selection]+".comment, construction_level_"+level[selection]+".sequence, vector.name, vector.code, enzymes.name"+add_query[selection]+" FROM enzymes, glycerol, construction_level_"+level[selection]+", vector WHERE enzymes.code=construction_level_"+level[selection]+".restriction_sites_"+level[selection]+" and glycerol.id= %s and glycerol.id=construction_level_"+level[selection]+".code and construction_level_"+level[selection]+".vector=vector.code"  

                cursor=db.cursor()
                cursor.execute(query,(code,),) #get all the information of the construction (common to all levels)
                row=cursor.fetchone()
                                                        
                
                self.lbl_glycerol_comment=Label(master,text=row[0])
                self.lbl_glycerol_date=Label(master,text="Date: "+str(row[1]))
                self.lbl_construction_name=Label(master,text="Construction name: "+row[2], font="Helvetica 14 bold")
                self.lbl_construction_comment=Label(master,text=row[3])
                self.btn_construction_sequence=Button(master,text="Show Sequence",command=lambda:self.display_sequence(row[4]))
                self.lbl_vector=Label(master,text="Vector: "+row[5]+" ("+row[6]+")")
                self.lbl_restriction=Label(master,text="Restriction site: "+row[7])

                self.lbl_glycerol_comment.grid(row=1, column=0, columnspan=2, sticky='W')
                self.lbl_glycerol_date.grid(row=1, column=2, sticky='W')
                self.lbl_construction_name.grid(row=2, column=0, columnspan=2, sticky='W')
                self.lbl_construction_comment.grid(row=2, column=2, columnspan=3, sticky='W')
                self.btn_construction_sequence.grid(row=2, column=5, columnspan=2, sticky='W')
                self.lbl_vector.grid(row=3, column=0, columnspan=2, sticky='W')
                self.lbl_restriction.grid(row=3, column=2, columnspan=2, sticky='W')

                
                
                if selection == (0,):
                        #add information about DNA_inserted, enzymes, primers and overhangs

                        query="SELECT left_code FROM pieces where number=%s"

                        cursor=db.cursor()
                        cursor.execute(query,(row[8],),)
                        left_code=cursor.fetchone()

                        query="SELECT right_code FROM pieces where number=%s"

                        cursor=db.cursor()
                        cursor.execute(query,(row[9],),)
                        right_code=cursor.fetchone()
                        
                        self.lbl_construction_5_end=Label(master,text="5'end: "+row[8]+" - "+left_code[0])
                        self.lbl_construction_3_end=Label(master,text="3'end: "+row[9]+" - "+right_code[0])
                        self.lbl_construction_5_end.grid(row=4, column=0, columnspan=2, sticky='W')
                        self.lbl_construction_3_end.grid(row=4, column=2, columnspan=2, sticky='W')

                        if row[10] == "0":
                                self.lbl_construction_Fw=Label(master,text="Primer Fw: Unknown")
                                self.lbl_construction_Fw.grid(row=5, column=0, columnspan=2, sticky='W')
                        else:
                                self.lbl_construction_Fw=Label(master,text="Primer Fw: "+row[9]) #HACER UN LINKKKK
                                self.lbl_construction_Fw.grid(row=5, column=0, columnspan=2, sticky='W')
                                
                        if row[11] == "0":
                                self.lbl_construction_Rv=Label(master,text="Primer Rv: Unknown")
                                self.lbl_construction_Rv.grid(row=5, column=2, columnspan=2, sticky='W')
                        else:
                                self.lbl_construction_Rv=Label(master,text="Primer Rv: "+row[10])
                                self.lbl_construction_Rv.grid(row=5, column=2, columnspan=2, sticky='W')


                        query="SELECT enzymes.name from enzymes, domesticated where enzymes.code = domesticated.enzyme_code and domesticated.construction_code=%s"

                        cursor=db.cursor()
                        cursor.execute(query,(code,),)
                        enzymes=cursor.fetchall()

                        all_enz=""

                        for enz in enzymes:
                                all_enz=all_enz+" "+enz[0]
                                
                        if all_enz != "":

                                self.lbl_construction_enz=Label(master,text="Domesticated for: "+all_enz)
                                self.lbl_construction_enz.grid(row=6, column=0, columnspan=3, sticky='W')


                        query="SELECT DNA_inserted.DNA_code, DNA_inserted.copy, DNA.name, DNA.description, DNA.type, DNA.sequence, DNA_inserted.comment, level0_DNA.position from level0_DNA, DNA, DNA_inserted where level0_DNA.construction_0=%s and level0_DNA.DNA_inserted_code=DNA_inserted.DNA_code and level0_DNA.DNA_inserted_copy=DNA_inserted.copy and DNA_inserted.DNA_code=DNA.code order by level0_DNA.position"

                        cursor=db.cursor()
                        cursor.execute(query,(code,),)
                        DNA_in_level0=cursor.fetchall()

                        self.lbl_construction_DNA1=Label(master,text="Position", font="Helvetica 14 bold")
                        self.lbl_construction_DNA2=Label(master,text="DNA name",font="Helvetica 14 bold")
                        self.lbl_construction_DNA3=Label(master,text="DNA type", font="Helvetica 14 bold")
                        self.lbl_construction_DNA4=Label(master,text="DNA description", font="Helvetica 14 bold")
                        self.lbl_construction_DNA5=Label(master,text="DNA copy", font="Helvetica 14 bold")
                        self.lbl_construction_DNA6=Label(master,text="DNA copy comment", font="Helvetica 14 bold")
                        

                        self.lbl_construction_DNA1.grid(row=7, column=0)
                        self.lbl_construction_DNA2.grid(row=7, column=1)
                        self.lbl_construction_DNA3.grid(row=7, column=2)
                        self.lbl_construction_DNA4.grid(row=7, column=3)
                        self.lbl_construction_DNA5.grid(row=7, column=4)
                        self.lbl_construction_DNA6.grid(row=7, column=5)
                        

                        for i in range (0,len(DNA_in_level0)):

                                self.lbl_construction_DNA_1=Label(master,text=DNA_in_level0[i][7])
                                self.lbl_construction_DNA_2=Label(master,text=DNA_in_level0[i][2])
                                self.lbl_construction_DNA_3=Label(master,text=DNA_in_level0[i][4])
                                self.lbl_construction_DNA_4=Label(master,text=DNA_in_level0[i][3])
                                self.lbl_construction_DNA_5=Label(master,text=DNA_in_level0[i][1])
                                self.lbl_construction_DNA_6=Label(master,text=DNA_in_level0[i][6])

                                        
                                self.lbl_construction_DNA_1.grid(row=8+i, column=0)
                                self.lbl_construction_DNA_2.grid(row=8+i, column=1)
                                self.lbl_construction_DNA_3.grid(row=8+i, column=2)
                                self.lbl_construction_DNA_4.grid(row=8+i, column=3)
                                self.lbl_construction_DNA_5.grid(row=8+i, column=4)
                                self.lbl_construction_DNA_6.grid(row=8+i, column=5)
                                
                
                elif selection == (1,):
                        ##add information about position, orientation, marker and level 0 constructions

                        query="SELECT left_code, right_code FROM pieces where number=%s"
                        cursor=db.cursor()
                        cursor.execute(query,(row[8],),)
                        end_codes=cursor.fetchone()
                        
                        self.lbl_construction_postion=Label(master,text="Position: "+row[8])
                        self.lbl_construction_orientation=Label(master,text="Orientation: "+str(row[9]))
                        self.lbl_construction_5end=Label(master,text="5' end: "+end_codes[0])                               
                        self.lbl_construction_3end=Label(master,text="3' end: "+end_codes[1]) 
                        self.lbl_construction_postion.grid(row=4, column=0, columnspan=2, sticky='W')                               
                        self.lbl_construction_orientation.grid(row=4, column=2, columnspan=2, sticky='W')
                        self.lbl_construction_5end.grid(row=5, column=0, columnspan=2, sticky='W')                               
                        self.lbl_construction_3end.grid(row=5, column=2, columnspan=2, sticky='W') 
                        #self.lbl_construction_3_end.grid(row=7, column=0)

                        query="SELECT organisms.name from organisms, used where organisms.code = used.organism_code and used.construction_1_code=%s"

                        cursor=db.cursor()
                        cursor.execute(query,(code,),)
                        organisims=cursor.fetchall()

                        all_organisims=""

                        for org in organisims:
                                all_organisims=all_organisims+" "+org[0]
                                
                        if all_organisims != "":

                                self.lbl_construction_org=Label(master,text="Can be used in: "+all_organisims)
                                self.lbl_construction_org.grid(row=6, column=0, columnspan=3, sticky='W')
                                
                        query="SELECT name FROM marker where code=%s"
                        cursor=db.cursor()
                        cursor.execute(query,(row[10],),)
                        marker=cursor.fetchall()

                        if len (marker) > 0:
                                all_markers=""
                                for mark in marker:
                                        all_markers=all_markers+" "+mark[0]
                                
                                self.lbl_construction_marker=Label(master,text="Markers: "+all_markers)
                                self.lbl_construction_marker.grid(row=7, column=0, columnspan=2, sticky='W')

                        query="SELECT construction_level_0.code, construction_level_0.name, construction_level_0.comment, construction_level_0.5_end, construction_level_0.3_end, contains_01.position from construction_level_0, contains_01 where contains_01.construction_1_code=%s and contains_01.construction_0_code=construction_level_0.code order by contains_01.position"

                        cursor=db.cursor()
                        cursor.execute(query,(code,),)
                        level0_in_level1=cursor.fetchall()


                        self.lbl_construction_L01=Label(master,text="Position", font="Helvetica 14 bold")
                        self.lbl_construction_L02=Label(master,text="C. Level 0 code",font="Helvetica 14 bold")
                        self.lbl_construction_L03=Label(master,text="C. Level 0 name", font="Helvetica 14 bold")
                        self.lbl_construction_L04=Label(master,text="C. Level 0 description", font="Helvetica 14 bold")
                        self.lbl_construction_L05=Label(master,text="End codes", font="Helvetica 14 bold")
                        

                        self.lbl_construction_L01.grid(row=8, column=0)
                        self.lbl_construction_L02.grid(row=8, column=1)
                        self.lbl_construction_L03.grid(row=8, column=2)
                        self.lbl_construction_L04.grid(row=8, column=3)
                        self.lbl_construction_L05.grid(row=8, column=4)
                        

                        for i in range (0,len(level0_in_level1)):

                                self.lbl_construction01_1=Label(master,text=level0_in_level1[i][5])
                                self.lbl_construction01_2=Label(master,text=level0_in_level1[i][0])
                                self.lbl_construction01_3=Label(master,text=level0_in_level1[i][1])
                                self.lbl_construction01_4=Label(master,text=level0_in_level1[i][2])
                                self.lbl_construction01_5=Label(master,text=level0_in_level1[i][3]+"-"+level0_in_level1[i][4])

                                        
                                self.lbl_construction01_1.grid(row=9+i, column=0)
                                self.lbl_construction01_2.grid(row=9+i, column=1)
                                self.lbl_construction01_3.grid(row=9+i, column=2)
                                self.lbl_construction01_4.grid(row=9+i, column=3)
                                self.lbl_construction01_5.grid(row=9+i, column=4)

                 
                elif selection == (2,):
                        
                        allpositions=[]
                        

                        self.lbl_construction_L11=Label(master,text="Position", font="Helvetica 14 bold")
                        self.lbl_construction_L12=Label(master,text="C. Level 1 code",font="Helvetica 14 bold")
                        self.lbl_construction_L13=Label(master,text="C. Level 1 name", font="Helvetica 14 bold")
                        self.lbl_construction_L14=Label(master,text="C. Level 1 description", font="Helvetica 14 bold")
                        self.lbl_construction_L15=Label(master,text="C. Level 1 position", font="Helvetica 14 bold")
                        self.lbl_construction_L16=Label(master,text="Orientation", font="Helvetica 14 bold")


                        self.lbl_construction_L11.grid(row=6, column=0)
                        self.lbl_construction_L12.grid(row=6, column=1)
                        self.lbl_construction_L13.grid(row=6, column=2)
                        self.lbl_construction_L14.grid(row=6, column=3)
                        self.lbl_construction_L15.grid(row=6, column=4)
                        self.lbl_construction_L16.grid(row=6, column=5)

                        contained={}

                        query="SELECT construction_level_1.code, construction_level_1.name, construction_level_1.comment, contains_12.position, construction_level_1.is_a, vector.orientation from vector, construction_level_1, contains_12 where contains_12.construction_2_code=%s and vector.code=construction_level_1.vector and contains_12.construction_1_code=construction_level_1.code order by contains_12.position"
                        
                        cursor=db.cursor()
                        cursor.execute(query,(code,),)
                        level1_in_level2=cursor.fetchall()
                        constructions_inserted=len(level1_in_level2)
                        
                        for construction_1 in level1_in_level2:
                                
                                contained[str(construction_1[3])]=construction_1

                        query="SELECT construction_level_M.code, construction_level_M.name, construction_level_M.comment, contains_M2.position from vector, construction_level_M, contains_M2 where contains_M2.construction_2_code=%s and contains_M2.construction_M_code=construction_level_M.code order by contains_M2.position"
                        
                        cursor=db.cursor()
                        cursor.execute(query,(code,),)
                        levelM_in_level2=cursor.fetchall()
                        
                        constructions_inserted=constructions_inserted+len(levelM_in_level2)
                        
                        for construction_M in levelM_in_level2:
                                
                                contained[str(construction_M[3])]=construction_1+[" "," "]
                        
                        for i in range (1, constructions_inserted+1):
                                
                                self.lbl_construction12_1=Label(master,text=contained[str(i)][3])
                                self.lbl_construction12_2=Label(master,text=contained[str(i)][0])
                                self.lbl_construction12_3=Label(master,text=contained[str(i)][1])
                                self.lbl_construction12_4=Label(master,text=contained[str(i)][2])
                                self.lbl_construction12_5=Label(master,text=contained[str(i)][4])
                                self.lbl_construction12_6=Label(master,text=contained[str(i)][5])
                                        
                                self.lbl_construction12_1.grid(row=7+i, column=0)
                                self.lbl_construction12_2.grid(row=7+i, column=1)
                                self.lbl_construction12_3.grid(row=7+i, column=2)
                                self.lbl_construction12_4.grid(row=7+i, column=3)
                                self.lbl_construction12_5.grid(row=7+i, column=4)
                                self.lbl_construction12_6.grid(row=7+i, column=5)
                                                
                
        def display_sequence(self,sequence): 
                print sequence
                
#------------------------------------ FRAME 5 --------------------------------------------------
			
class Application5(Frame): #Insert Panel
        

	def __init__(self, master):
		Frame.__init__(self, master)
		self.create_widgets(master)
		
	def create_widgets(self,master):
		global selection
		global selection3
		global level
		global db
		selection3=selection

		self.lbl_title=Label(master,text="Complete this basic information about the new level "+level[selection3]+" construction", font="Helvetica 14 bold")
		self.lbl_title.grid(column=0, row=0, columnspan=4)

                self.lbl_collection=Label(master, text="Collection: ")
                self.lbl_name=Label(master, text="Name: ")
                self.lbl_comment=Label(master, text="Comment: ")
                self.lbl_sequence=Label(master, text="Sequence: ")
                self.lbl_vector=Label(master, text="Vector: ")
                self.lbl_restriction=Label(master, text="Restriction sites: ")
                self.lbl_numberparts=Label(master, text="Number of parts inserted: ")

                self.lbl_collection2=Label(master, text="Ej: 'EC', 'LR'")
                self.lbl_name2=Label(master, text="Max. 45 chr.")
                self.lbl_comment2=Label(master, text="Max. 200 chr. Not mandatory")
                self.lbl_restriction2=Label(master, text="Not mandatory")
                self.lbl_numberparts2=Label(master, text="DNA fragments in case of Level 0 constructions")

                self.ent_collection=Entry(master)
                self.ent_name=Entry(master)
                self.ent_comment=Entry(master)
                self.ent_sequence=Entry(master)
                self.cbox_vector=ttk.Combobox(self.master, state="readonly")
                self.cbox_restriction=ttk.Combobox(self.master, state="readonly")
                self.ent_numberparts=Entry(master)

                self.lbl_collection.grid(row=1, column=0,sticky='W')
                self.lbl_name.grid(row=2, column=0,sticky='W')
                self.lbl_comment.grid(row=3, column=0,sticky='W')
                self.lbl_sequence.grid(row=4, column=0,sticky='W')
                self.lbl_vector.grid(row=5, column=0,sticky='W')
                self.lbl_restriction.grid(row=6, column=0,sticky='W')
                self.lbl_numberparts.grid(row=7, column=0,sticky='W')

                self.ent_collection.grid(row=1, column=1,sticky='W')
                self.ent_name.grid(row=2, column=1,sticky='W')
                self.ent_comment.grid(row=3, column=1,sticky='W')
                self.ent_sequence.grid(row=4, column=1,sticky='W')
                
                self.lbl_collection2.grid(row=1, column=2,sticky='W')
                self.lbl_name2.grid(row=2, column=2,sticky='W')
                self.lbl_comment2.grid(row=3, column=2,sticky='W')
                self.lbl_restriction2.grid(row=6, column=2,sticky='W')
                self.lbl_numberparts2.grid(row=7, column=2,sticky='W')

                query="SELECT name, code FROM vector WHERE vector.level=%s order by name"
                cursor=db.cursor()
                cursor.execute(query,(level[selection3],),)
                rows=cursor.fetchall()
                vectors=[]
                for vector in rows:
                        vectors=vectors+[vector[0]+"-"+vector[1]]
                self.cbox_vector["values"]=vectors
                self.cbox_vector.grid(row=5, column=1, sticky='W')

                query="SELECT name, code FROM enzymes order by code"
                cursor=db.cursor()
                cursor.execute(query,)
                rows=cursor.fetchall()
                enzymes=[]
                for enzyme in rows:
                        enzymes=enzymes+[enzyme[1]+" - "+enzyme[0]]
                self.cbox_restriction["values"]=enzymes
                self.cbox_restriction.grid(row=6, column=1, sticky='W')

                self.ent_numberparts.grid(row=7, column=1,sticky='W')

              

                
		if selection3 == (0,):

                        self.lbl_fwd=Label(master, text="Forward primer: ")
                        self.lbl_rvs=Label(master, text="Reverse primer: ")
                        self.lbl_fwd.grid(row=8, column=0, sticky='W')
                        self.lbl_rvs.grid(row=9, column=0, sticky='W')
                        self.cbox_fwd=ttk.Combobox(self.master, state="readonly")
                        self.cbox_rvs=ttk.Combobox(self.master, state="readonly")
                        
                        query="SELECT code, locator FROM primers order by locator"
                        cursor=db.cursor()
                        cursor.execute(query,)
                        rows=cursor.fetchall()
                        primers=[]
                        for primer in rows:
                                primers=primers+[primer[1]+" - "+primer[0]]
                        self.cbox_fwd["values"]=primers
                        self.cbox_rvs["values"]=primers
                        self.cbox_fwd.grid(row=8, column=1, sticky='W')
                        self.cbox_rvs.grid(row=9, column=1, sticky='W')
                        
                        self.lbl_5end=Label(master, text="5' end: ")
                        self.lbl_3end=Label(master, text="3' end: ")
                        self.lbl_5end.grid(row=10, column=0, sticky='W')
                        self.lbl_3end.grid(row=11, column=0, sticky='W')
                        self.cbox_5end=ttk.Combobox(self.master, state="readonly")
                        self.cbox_3end=ttk.Combobox(self.master, state="readonly")
                        
                        query="SELECT number, left_code, right_code FROM pieces where number not like 'P%' order by number"
                        cursor=db.cursor()
                        cursor.execute(query,)
                        rows=cursor.fetchall()
                        pieces5=[]
                        pieces3=[]
                        for piece in rows:
                                pieces5=pieces5+[piece[0]+" - "+piece[1]]
                                pieces3=pieces3+[piece[0]+" - "+piece[2]]
                        self.cbox_5end["values"]=pieces5
                        self.cbox_3end["values"]=pieces3
                        self.cbox_5end.grid(row=10, column=1, sticky='W')
                        self.cbox_3end.grid(row=11, column=1, sticky='W')
                        
                elif selection3== (1,):
                        self.lbl_Position=Label(master, text="Position: ")
                        self.lbl_Position.grid(row=8, column=0, sticky='W')
                        self.cbox_Position=ttk.Combobox(self.master, state="readonly")
                        
                        query="SELECT number, left_code, right_code FROM pieces where number like 'P%' order by number"
                        cursor=db.cursor()
                        cursor.execute(query,)
                        rows=cursor.fetchall()
                        positions=[]
                
                        for position in rows:
                                positions=positions+[position[0]+" - ("+position[1]+"-"+position[2]+")"]
                        self.cbox_Position["values"]=positions
                        self.cbox_Position.grid(row=8, column=1, sticky='W')
                        
		self.btn_check_all_complete=Button(master, text="Continue")
		self.btn_check_all_complete.grid()
		self.btn_check_all_complete["command"]=lambda:self.check_all_complete(master)
                        
	def check_all_complete(self,master):
                
                global selection3
                global level
                global db
                global user_name
                global SelectConstructionScreen
                global InsertScreen

                control_insert=True #Allows continue

                values2=()


                collection=self.ent_collection.get()
                name=self.ent_name.get()
                comment=self.ent_comment.get()
                sequence=self.ent_sequence.get()
                vector=self.cbox_vector.get()
                numberparts=self.ent_numberparts.get()

                if selection3 == (0,):
                        end5=self.cbox_5end.get()
                        end3=self.cbox_3end.get()
                        fwd=self.cbox_fwd.get()
                        rvs=self.cbox_rvs.get()

                        if (end5=="") or (end3=="") or (fwd=="") or (rvs==""):
                                control_insert=False

                        else:
                                end5=end5.split(" - ")
                                end3=end3.split(" - ")
                                fwd=fwd.split(" - ")
                                rvs=rvs.split(" - ")
                                
                                values2=(end5[0], end3[0], fwd[1], rvs[1],)

                elif selection3 == (1,):
                        position=self.cbox_Position.get()
                        if (position != ""):
                                position=position.split(" - ")

                        values2=(position[0],)
                                
                

                if len(name)>45:
                        control_insert=False
                        print ("Name is too long. It has "+str(name)+"characters") #poner en msgbox
                        
                if len(comment)>200:
                        control_insert=False
                        print ("Comment is too long. It has "+str(comment)+"characters") #poner en msgbox
                try:
                        numberparts=int(numberparts)
                        if numberparts <= 0:
                                control=False
                                print ("Number of parts must be greater than 0")
                except:
                        control_insert=False
                        print ("Number of parts must be a number")

                if (collection == "") or (name == "") or (sequence == "") or (vector == ""):
                        control_insert=False
                        print ("Mandatory fields are not completed")


                if control_insert == True:
                        
                        coll=len(collection)+1
                        query="SELECT SUBSTRING(id,"+str(coll)+") from glycerol where id like '"+ collection +"%'"
                        cursor=db.cursor()
                        cursor.execute(query,)
                        rows=cursor.fetchall()
                        maxim=0
                        if len (rows) != 0:
                                for sample in rows:
                                        num=int(sample[0])
                                        if num > maxim:
                                                maxim=num

                                code=collection+str(maxim+1)
                        else:
                                print ("Start a new collection?")
                                code=collection+"1"
                        vector=vector.split('-')
                        
                        if self.cbox_restriction.current() != -1:

                                restriction=self.cbox_restriction.get()
                                restriction=restriction.split(" - ")
                                values2=values2+(restriction[0],)
                                rest=", restriction_sites_"+level[selection]
                                rest2=", %s"
                        else:
                                rest=""
                                rest2=""

                

                        add_glycerol="INSERT INTO glycerol (id, type, comment, date) VALUES (%s, %s, %s, %s)"
                        data_glycerol=(code, "level"+level[selection3], collection+" collection "+user_name, datetime.date.today())
                        cursor.execute(add_glycerol, data_glycerol)

                        fields={(0,):", construction_level_0.5_end, construction_level_0.3_end, construction_level_0.forward_primer, construction_level_0.reverse_primer",#Level 0
                                (1,):", construction_level_1.is_a", #Level 1
                                (2,):"",
                                (3,):"",
                                (4,):""}

                        values={(0,):", %s, %s, %s, %s",#Level 0
                                (1,):", %s", #Level 1
                                (2,):"",
                                (3,):"",
                                (4,):""}

                        

                        add_construction="INSERT INTO construction_level_"+level[selection3]+"(code, name, sequence, vector, comment "+fields[selection3]+rest+") VALUES (%s,%s, %s, %s, %s"+values[selection3]+rest2+")"
                        data_construction=(code, name, sequence, vector[1], comment)+values2

                        cursor.execute(add_construction, data_construction)

                        self.btn_check_all_complete.grid_forget()

                        position=1

                        

                        control_add=True

                     
                        InsertScreen.destroy()
                        
                        SelectConstructionScreen=Tk()
                        SelectConstructionScreen.title("Select Constructions Inserted")
                        SelectConstructionScreen.geometry("600x500")
                        Application6(SelectConstructionScreen, numberparts, position, code, name) #Show ConstrutionScreen

                        SelectConstructionScreen.mainloop()



#------------------------------------ FRAME 6 --------------------------------------------------
			
class Application6(Frame): #Construction_inserted Panel
        
	def __init__(self, master,numberparts, position, code, name):
		Frame.__init__(self, master)
		self.lbl_title=Label(master, text="Construction "+ name +" // Glycerol id: "+code, font="Helvetica 14 bold")
		self.lbl_title.grid(row=0,column=0,columnspan=3)
		self.btn_nextposition=Button(master,text="Continue")
		self.lbl_subtitle=Label(master, text="Choose the piece placed at "+str(position)+" position")
		self.lbl_subtitle.grid()
		self.cbox_constructions=Combobox(self.master, state="readonly")
		if selection3==(0,):
                        #poner DNAs y copys
                        query="SELECT DNA_inserted.DNA_code, DNA_inserted.copy, DNA.name FROM DNA_inserted, DNA where DNA.code = DNA_inserted.DNA_code order by DNA.name"
                elif selection3==(1,):
                        #poner levels 0
                        query="SELECT code, name FROM construction_level_0 order by name"
                elif selection3==(2,):
                        #poner levels 1 y M
                        query="SELECT code, name FROM construction_level_1 order by name"
                        query2="SELECT code, name FROM construction_level_M order by name"
                        
                elif selection3==(3,):
                        #poner levels 1 y P
                        query="SELECT code, name FROM construction_level_1 order by name"
                        query2="SELECT code, name FROM construction_level_P order by name"
                else:
                        #poner levels M
                        query="SELECT code, name FROM construction_level_M order by name"

                cursor=db.cursor()
                cursor.execute(query,)
                rows=cursor.fetchall()
                        
                try:
                        cursor=db.cursor()
                        cursor.execute(query2,)
                        rows=rows+cursor.fetchall()
                except:
                        pass

                possible_constructions=[]
                
                for construction in rows:
                        if selection3 != (0,):
                                possible_constructions=possible_constructions+[construction[1]+" - "+construction[0]]
                        else:
                                possible_constructions=possible_constructions+[construction[2]+" ("+construction[0]+" - "+construction[1]+")"]
                        
                self.cbox_constructions["values"]=possible_constructions
                self.cbox_constructions.width=100
                self.cbox_constructions.grid(columnspan=3)
                self.btn_nextposition.grid()

                self.btn_nextposition["command"]=lambda:self.add_position(master, numberparts, position, code, name)
                
	
        def add_position(self, master, numberparts, position, code, name):
                global SelectConstructionScreen
                construction_added=self.cbox_constructions.get()
                
                if construction_added != "":
                        if selection3 != (0,):
                                construction_added=construction_added.split(" - ")

                                
                                control_insert = False

                                query="SELECT type from glycerol where id=%s"
                                cursor=db.cursor()
                                cursor.execute(query,(construction_added[1],),)
                                cons_level=cursor.fetchone()
                                
                                if "level" in cons_level[0]:
                                        cons_level=cons_level[0][5:]
                                else:
                                        if "P" in cons_level[0]: #EL P (End-linker P)
                                                cons_level="M"
                                        else:
                                                cons_level="1"
                               
                        
                                add_cons_inserted="INSERT INTO contains_"+cons_level+level[selection3]+" (construction_"+cons_level+"_code, construction_"+level[selection3]+"_code, position) VALUES (%s, %s, %s)"
                                data_cons_inserted=(construction_added[1], code, position)
                        else:
                                construction_added=construction_added.split(" (")
                                construction_added=construction_added[1].split(" - ")
                                add_cons_inserted="INSERT INTO level0_DNA (position, DNA_inserted_code, DNA_inserted_copy, construction_0) VALUES (%s, %s, %s, %s)"
                                data_cons_inserted=(position, construction_added[0], construction_added[1][:-1], code)
                                

                        cursor=db.cursor()
                        cursor.execute(add_cons_inserted, data_cons_inserted)                                
        

                        if position==numberparts:

                                db.commit()
                                SelectConstructionScreen.destroy()

                        else:
                                        
                                position=position+1
                                SelectConstructionScreen.destroy()
                                SelectConstructionScreen=Tk()
                                SelectConstructionScreen.title("Select Constructions Inserted")
                                SelectConstructionScreen.geometry("600x500")
                                Application6(SelectConstructionScreen, numberparts, position, code, name) #Show ConstrutionScreen
                                SelectConstructionScreen.mainloop()


#------------------------------------ FRAME 7 --------------------------------------------------
			
class Application7(Frame): #OtherOptions Panel
        
	def __init__(self, master):
		Frame.__init__(self, master)
		self.create_widgets(master)
		
	def create_widgets(self, master):

                global action

                self.cbox_actions=ttk.Combobox(self.master,state="readonly")
                self.cbox_actions["values"]=["Select Action","Search","Insert"]
                self.cbox_actions.current(0)
                self.cbox_actions.grid()


                self.cbox_items=ttk.Combobox(self.master,state="readonly")
                self.cbox_items["values"]=["Select Item","DNA","DNA_inserted","primers","antibiotic","organisms","enzymes","marker", "vector"]
                self.cbox_items.current(0)
                self.cbox_items.grid()

                self.btn_result=Button(master, text="Continue")
                self.btn_result["command"]=lambda:self.check_option(master)
                self.btn_result.grid()
                

        def check_option(self,master):

                global db

                if (self.cbox_items.current() != 0) and (self.cbox_actions.current() != 0):
                        
                        item=self.cbox_items.get()
                        action=self.cbox_actions.get()
                        
                        if action == "Search":

                                self.cbox_items.grid_forget()


                                data={"DNA":"code, name",
                                      "DNA_inserted":"DNA_code, copy", 
                                      "primers":"code, locator",
                                      "antibiotic": "code, name",
                                      "organisms":"code, name",
                                      "enzymes":"code, name", 
                                      "marker":"code, name",
                                      "vector":"code, name"}

                                if item != "DNA_inserted":
                                        query="SELECT "+data[item]+" FROM "+item+" order by code"
                                else:
                                        query="SELECT "+data[item]+" FROM "+item+" order by DNA_code"
                                        
                                cursor=db.cursor()
                                cursor.execute(query)
                                instances=cursor.fetchall()

                                possible_items=["Select "+item]

                                for row in instances: #Each option is added to the tuple combo_options

                                        try:
                                                possible_items=possible_items+[row[0]+" - "+row[1]+" - "+row[2]]
                                        except:
                                                possible_items=possible_items+[row[0]+" - "+row[1]]
                                                
                                self.cbox_actions["values"]=possible_items
                                self.cbox_actions.current(0)

                                self.btn_result["command"]=lambda:self.search_option(item)
                        else:
                               
                                self.cbox_items.grid_forget()
                                self.cbox_actions.grid_forget()
                                self.btn_result.grid_forget()
                                self.insert_option(master,item)

        def search_option(self,item):

                global OtherScreen

                code=self.cbox_actions.get()
                code=code.split(' - ')
                
                OtherScreen.destroy()

                InformationPanel=Tk()
                InformationPanel.title(item+": "+code[0])
                InformationPanel.geometry("600x500")
                Application8(InformationPanel, item, code)
                InformationPanel.mainloop()
                             

        def insert_option(self,master,item):


                if item=="DNA_inserted":
                        
                        query="SELECT code, name FROM DNA order by code"
                                        
                        cursor=db.cursor()
                        cursor.execute(query)
                        DNAs=cursor.fetchall()

                        possible_DNA=["Select "+item]

                        for row in DNAs: #Each option is added to the tuple combo_options

                                        possible_DNA=possible_DNA+[row[0]+" - "+row[1]]

                        self.cbox_DNA=ttk.Combobox(self.master,state="readonly")
                        self.cbox_DNA["values"]=possible_DNA
                        self.cbox_DNA.current(0)
                        self.cbox_DNA.grid()
                        

                fieldsdata={"DNA":["name", "type", "description", "sequence"],
                                   "DNA_inserted":["region_start", "region_end", "comment", "number of mutations"],
                                   "primers":["collection", "sequence", "comment"],
                                   "antibiotic":["code", "name"],
                                   "organisms":["name", "description"],
                                   "enzymes":["name", "restriction_sites", "cut_pos_1", "cut_pos_2"],
                                   "marker":["code", "name", "description"],
                                   "vector":["collection", "name", "level", "comment", "sequence", "numer of markers", "number of resistances"]}
                entrys=[]

                for i in range(0, len(fieldsdata[item])):
                        lbl_field=Label(master,text=fieldsdata[item][i])
                        ent_field=Entry(master)
                        lbl_field.grid(row=i+1,column=0)
                        ent_field.grid(row=i+1,column=1)

                        entrys=entrys+[ent_field]

                self.btn_result.grid()
                self.btn_result["command"]=lambda:self.continue_insertion(master,item,entrys,fieldsdata[item])

        def continue_insertion(self, master,item, entrys, fields):

                global OtherScreen
                global OtherScreen2
                global db
                global user_name
                
                control_insert=True

                for entry in entrys:

                        entry_content=entry.get()
                        
                        if entry_content=="":
                                control_insert=False

                if control_insert==True:
                
                        if item == "DNA":

                                query="SELECT SUBSTRING(code,4) from DNA"
                                cursor=db.cursor()
                                cursor.execute(query,)
                                rows=cursor.fetchall()
                                maxim=0
                                
                                for sample in rows:
                                        num=int(sample[0])
                                        if num > maxim:
                                                maxim=num

                                code="DNA"+str(maxim+1)

                                add_item="INSERT INTO DNA (code, sequence, name, description, type) VALUES (%s, %s, %s, %s, %s)"
                                data_item=(code, entrys[3].get(),entrys[0].get(),entrys[2].get(),entrys[1].get())

                        elif item == "vector":
                                
                                query="SELECT SUBSTRING(id,"+str(len(entrys[0].get())+1)+") from glycerol where id like '"+entrys[0].get()+"%' "
                                cursor=db.cursor()
                                cursor.execute(query,)
                                rows=cursor.fetchall()
                                maxim=0
                                if len (rows) != 0:
                                        for sample in rows:
                                                num=int(sample[0])
                                                if num > maxim:
                                                        maxim=num

                                        code=entrys[0].get()+str(maxim+1)
                        
                                else:
                                        print ("Start a new collection?")
                                        code=entrys[0].get()+"1"

                                
                                add_glycerol="INSERT INTO glycerol (id, type, comment, date) VALUES (%s, %s, %s, %s)"
                                data_glycerol=(code, "vector", entrys[0].get()+" collection "+user_name, datetime.date.today())
                                cursor.execute(add_glycerol, data_glycerol)

                                add_item="INSERT INTO vector (code, level, name, sequence, comment) VALUES (%s, %s, %s, %s, %s)"
                                data_item=(code, entrys[2].get(),entrys[1].get(),entrys[3].get(),entrys[4].get())
                                
                        elif item == "DNA_inserted":

                                DNA_code=self.cbox_DNA.get()
                                DNA_code=DNA_code.split(" - ")
                                DNA_code=DNA_code[0]

                                query="SELECT copy from DNA_inserted where DNA_code='"+DNA_code+"'"


                                cursor=db.cursor()
                                
                                cursor.execute(query,)
                                rows=cursor.fetchall()
                                maxim=0

                                for sample in rows:
                                        num=int(sample[0])
                                        if num > maxim:
                                                maxim=num
                                copy=int(maxim)+1

                                add_item="INSERT INTO DNA_inserted (DNA_code, copy, region_start, region_end, comment) VALUES (%s, %s, %s, %s, %s)"
                                data_item=(DNA_code, copy, entrys[0].get(),entrys[1].get(),entrys[2].get())
                                

                                
                        elif item == "antibiotic":
                                add_item="INSERT INTO antibiotic (code, name) VALUES (%s, %s)"
                                data_item=(entrys[0].get(),entrys[1].get())

                        elif item == "marker":
                                add_item="INSERT INTO marker (code, name, description) VALUES (%s, %s, %s)"
                                data_item=(entrys[0].get(),entrys[1].get(),entrys[2].get())
                        
                        else:

                                query="SELECT code from "+item
                                cursor=db.cursor()
                                cursor.execute(query,)
                                rows=cursor.fetchall()
                                maxim=0
                                
                                for sample in rows:
                                        num=int(sample[0])
                                        if num > maxim:
                                                maxim=num
                                code=int(maxim)+1
                                

                                if item == "primers":

                                        query="SELECT SUBSTRING(locator,"+str(len(entrys[0].get())+1)+") from primers where locator like '"+entrys[0].get()+"%' "
                                        cursor=db.cursor()
                                        cursor.execute(query,)
                                        rows=cursor.fetchall()
                                        maxim=0
                                        if len (rows) != 0:
                                                for sample in rows:
                                                        num=int(sample[0])
                                                        if num > maxim:
                                                                maxim=num

                                                locator=entrys[0].get()+str(maxim+1)
                                
                                        else:
                                                print ("Start a new collection?")
                                                locator=entrys[0].get()+"1"


                                        add_item="INSERT INTO primers (code, locator, sequence, comment) VALUES (%s, %s, %s, %s)"
                                        data_item=(code, locator, entrys[1].get(),entrys[2].get())

                                elif item == "enzymes":
                                        
                                        add_item="INSERT INTO enzymes (code, name, restriction_sites, cut_pos_1, cut_pos_2) VALUES (%s, %s, %s, %s, %s)"
                                        data_item=(code, entrys[0].get(),entrys[1].get(),entrys[2].get(),entrys[3].get())
                                        
                                elif item == "organisms":
                                        add_item="INSERT INTO organisms (code, name, description) VALUES (%s, %s, %s)"
                                        data_item=(code, entrys[0].get(),entrys[1].get())
                                        
                        cursor=db.cursor()
                        cursor.execute(add_item, data_item)


                        if item != "vector" and item != "DNA_inserted":
                                db.commit()

                                OtherScreen.destroy()
                        else:
                                if item == "DNA_inserted":
                                        code=[DNA_code, copy]

                                        if int(entrys[-1].get()) >0:

                                                OtherScreen2=Tk()
                                                OtherScreen2.title(item)
                                                OtherScreen2.geometry("600x500")
                                                Application9(OtherScreen2, code, int(entrys[-1].get()), 1, item, "mutation", 0)
                                                OtherScreen.destroy()
                                                OtherScreen2.mainloop()
                                        else:
                                                db.commit()
                                                OtherScreen.destroy()
                                                
                                elif item == "vector":
                                        if int(entrys[-1].get()) >0 or int(entrys[-2].get()) >0:
                                                OtherScreen2=Tk()
                                                OtherScreen2.title(item)
                                                OtherScreen2.geometry("600x500")
                                                Application9(OtherScreen2, code, int(entrys[-1].get()), 1, item, "antibiotic", int(entrys[-2].get()))
                                                OtherScreen.destroy()
                                                OtherScreen2.mainloop()

                                        
#-------------------------------- Information Panel -------------------------
        
                        
class Application8(Frame): #Information Panel
        
	def __init__(self, master, item, code):
                global db
		Frame.__init__(self, master)

		information={"DNA":"code, name, description, type, sequence",
                             "DNA_inserted":"DNA_inserted.DNA_code, DNA.name, DNA_inserted.copy, DNA_inserted.comment, DNA_inserted.region_start, DNA_inserted.region_end",
                             "primers":"code, locator, sequence, comment",
                             "antibiotic": "code, name",
                             "organisms":"code, name, description",
                             "enzymes":"code, name, restriction_sites, cut_pos_1, cut_pos_2",
                             "marker":"code, name",
                             "vector":"glycerol.comment, glycerol.date, vector.code, vector.name, vector.level, vector.comment, vector.sequence"}

		if item == "DNA_inserted":
                        query="SELECT "+information[item]+" from DNA, DNA_inserted WHERE DNA.code=DNA_inserted.DNA_code and DNA_inserted.DNA_code=DNA.code and DNA_inserted.DNA_code=%s and DNA_inserted.copy=%s"
                        params=(code[0],code[1],)
                elif item == "vector":
                        query="SELECT "+information[item]+" from glycerol, vector where glycerol.id=vector.code and vector.code=%s"
                        params=(code[0],)
                else:
                        query="SELECT "+information[item]+" from "+item+" where code=%s"
                        params=(code[0],)

                cursor=db.cursor()
                cursor.execute(query,params)
                item_information=cursor.fetchall()

                feature_list=information[item].split(", ")

                for i in range(0, len(item_information[0])):
                        lbl_feature=Label(master, text=feature_list[i]+": ")
                        ent_feature=Entry(master, width=200)
                        ent_feature.insert(0,str(item_information[0][i]))
                        ent_feature["state"]="readonly"
                        lbl_feature.grid(sticky='W', row=i, column=0)
                        ent_feature.grid(sticky='W', row=i, column=1)
                        
                if item == "DNA_inserted":

                        query="SELECT mutation.position, mutation.mutation from mutation, DNA_inserted where mutation.DNA_code=DNA_inserted.DNA_code and mutation.copy=DNA_inserted.copy and DNA_inserted.DNA_code=%s and DNA_inserted.copy=%s"
                        params=(item_information[0][0],item_information[0][2],)
                        cursor.execute(query,params)
                        mutations=cursor.fetchall()
                        
                        for i in range(0, len(mutations)):
                                       lbl_feature=Label(master, text="Mutation position - Mutation:")
                                       ent_feature=Entry(master, width=200)
                                       ent_feature.insert(0,str(mutations[i][0])+" - "+mutations[i][1])
                                       ent_feature["state"]="readonly"
                                       lbl_feature.grid(sticky='W', column=0)
                                       ent_feature.grid(sticky='W', column=1)
                                       
                elif item == "vector":

                        params=(item_information[0][2],)

                        query="SELECT resistance.antibiotic_code, resistance.position FROM vector, resistance WHERE vector.code=resistance.vector_code and vector.code=%s"
                        cursor.execute(query,params)
                        resistances=cursor.fetchall()
                        for i in range(0, len(resistances)):
                               lbl_feature=Label(master, text="Resistance:")
                               ent_feature=Entry(master, width=200)
                               ent_feature.insert(0,str(resistances[i][0]))
                               ent_feature["state"]="readonly"
                               lbl_feature.grid(sticky='W', column=0)
                               ent_feature.grid(sticky='W', column=1)

                
                        query="SELECT vector_has_marker.marker_code, vector_has_marker.position FROM vector, vector_has_marker WHERE vector.code=vector_has_marker.vector_code and vector.code=%s"
                        cursor.execute(query,params)
                        markers=cursor.fetchall()
                        for i in range(0, len(markers)):
                               lbl_feature=Label(master, text="Marker:")
                               ent_feature=Entry(master, width=200)
                               ent_feature.insert(0,str(markers[i][0]))
                               ent_feature["state"]="readonly"
                               lbl_feature.grid(sticky='W', column=0)
                               ent_feature.grid(sticky='W', column=1)


#------------------------------------ FRAME 9 --------------------------------------------------
			
class Application9(Frame): #Other2 Panel
        
	def __init__(self, master,code, numberiterations, iteration, item, field, other):
		Frame.__init__(self, master)
##		
		self.btn_nextposition=Button(master,text="Continue")


		if field == "mutation":
                        self.lbl_position=Label(master, text="Position")
                        self.lbl_mutation=Label(master, text="Mutation")
                        self.ent_position=Entry(master)
                        self.ent_mutation=Entry(master)

                        self.lbl_position.grid(row=1, column=0)
                        self.lbl_mutation.grid(row=2, column=0)
                        self.ent_position.grid(row=1, column=1)
                        self.ent_mutation.grid(row=2, column=1)


                        
                else:
                        self.cbox_possiblevalues=Combobox(self.master, state="readonly")

                        self.lbl_position=Label(master, text="Position")
                        self.ent_position=Entry(master)

                        
                        if field == "marker":
                        
                                query="SELECT code FROM marker"

                        elif field == "antibiotic":

                                query="SELECT code FROM antibiotic"
 

                        cursor=db.cursor()
                        cursor.execute(query,)
                        rows=cursor.fetchall()
                                
                        possible_values=[]
                        
                        for element in rows:
                                
                                possible_values=possible_values+[element[0]]

                        self.cbox_possiblevalues["values"]=possible_values
                        self.cbox_possiblevalues.width=100
                        self.cbox_possiblevalues.grid()

                        self.lbl_position.grid(row=1, column=0)
                        self.ent_position.grid(row=1, column=1)

                self.btn_nextposition["command"]=lambda:self.add_position(master, code, numberiterations, iteration, item, field, other)
                self.btn_nextposition.grid()
                
	
        def add_position(self, master, code, numberiterations, iteration, item, field, other):
                global OtherScreen2
                global db

                if item == "DNA_inserted":
                        position=self.ent_position.get()
                        mutation=self.ent_mutation.get()

                        add_iteration="INSERT INTO mutation (DNA_code, copy, position, mutation) VALUES (%s, %s, %s, %s)"
                        data_iteration=(code[0], code[1], position, mutation)
                        
                elif item == "vector":
                        value_selected=self.cbox_possiblevalues.get()
                        position=self.ent_position.get()
                        
                        if value_selected != "" and position != "":
                                if field == "marker":
                                        
                                        add_iteration="INSERT INTO vector_has_marker (marker_code, vector_code, position) VALUES (%s, %s, %s)"
                                        
                                elif field == "antibiotic":
                                        
                                        add_iteration="INSERT INTO resistance (antibiotic_code, vector_code, position) VALUES (%s, %s, %s)"
                                        
                                data_iteration=(value_selected, code, position)


                cursor=db.cursor()
                cursor.execute(add_iteration, data_iteration)


                if iteration==numberiterations and other==0:

                        db.commit()
                        OtherScreen2.destroy()
                else:
                                
                        
                        OtherScreen2.destroy()
                        OtherScreen2=Tk()
                        OtherScreen2.title(item)
                        OtherScreen2.geometry("600x500")
                        if iteration==numberiterations:
                                iteration=1
                                numberiterations=other
                                other=0
                                field="marker"
                        else:
                                iteration=iteration+1
                        Application9(OtherScreen2, code, numberiterations,iteration, item, field, other) #Show ConstrutionScreen
                        OtherScreen2.mainloop()


#------------------------------------ FRAME 10 --------------------------------------------------
			
class Application10(Frame): #Users Screen
        
	def __init__(self, master):
		Frame.__init__(self, master)
		self.create_widgets(master)
		
	def create_widgets(self, master):

                self.btn_add_user=Button(master, text="Add User")
                self.btn_remove_user=Button(master, text="Remove User") #FALTA

                self.btn_add_user.grid()
                self.btn_remove_user.grid()

                self.btn_add_user["command"]=lambda:self.add_user(master)
        def add_user(self,master):

                self.btn_add_user.grid_forget()
                self.btn_remove_user.grid_forget()



		self.lbl_name=Label(master,text="Name:").grid(row=1,sticky=W)
		#self.grid()
		self.lbl_pwd=Label(master, text="Password:").grid(row=2,sticky=W)
		self.lbl_pwd2=Label(master, text="Confirm password:").grid(row=3,sticky=W)
		self.lbl_priv=Label(master, text="Privilege level:").grid(row=4,sticky=W)
		
		self.ent_name=Entry(master) #Entry where writting the user name
		self.ent_name.grid(row=1,column=1)

		self.ent_pwd=Entry(master) #Entry where writting the user password
		self.ent_pwd.config(show = "*") #"Hide" the password
		self.ent_pwd.grid(row=2,column=1)

		self.ent_pwd2=Entry(master) #Entry where writting the user password
		self.ent_pwd2.config(show = "*") #"Hide" the password
		self.ent_pwd2.grid(row=3,column=1)

		self.cbox_levelpriv=Combobox(self.master, state="readonly")
		self.cbox_levelpriv["values"]=["1", "2", "3", "4"]
		self.cbox_levelpriv.grid(row=4, column=1)
		

		self.btn_submit=Button(master,text="Submit")
		self.btn_submit.grid(row=5)
		self.btn_submit["command"]=lambda:self.add_user2(master)

	def add_user2(self,master):
                global UserScreen
                global db

                if self.ent_pwd2.get() == self.ent_pwd.get():
                        add_user="CREATE USER '"+self.ent_name.get()+"'@'%' IDENTIFIED BY '"+ self.ent_pwd.get()+"' WITH MAX_QUERIES_PER_HOUR 1000 MAX_UPDATES_PER_HOUR 1000 MAX_CONNECTIONS_PER_HOUR 1000 MAX_USER_CONNECTIONS 100"

                        priv_level={"1":"SELECT",
                                    "2":"SELECT, INSERT",
                                    "3":"SELECT, INSERT, UPDATE, DELETE",
                                    "4":"SELECT, INSERT, UPDATE, DELETE, CREATE USER"}

                        priv_chosen=self.cbox_levelpriv.get()

                        set_priv="GRANT "+priv_level[priv_chosen]+" ON *.* TO '"+self.ent_name.get()+"'@'%'"

                        
                        cursor=db.cursor()
                        cursor.execute(add_user)
                        cursor.execute(set_priv)

                        UserScreen.destroy()

                        

                
                                                  
#-------------------------------- MAIN PROGRAM -------------------------

control=False
WelcomeScreen=Tk()
WelcomeScreen.title("Welcome Screen")
WelcomeScreen.geometry("420x120")
Application1(WelcomeScreen)
WelcomeScreen.mainloop() #Show Welcome Screen
control2=False


while control == True: #control changes to True when user and password are ok
	SearchScreen=Tk()
	SearchScreen.title("Search Panel") 
	SearchScreen.geometry("600x500")
	Application2(SearchScreen)
	SearchScreen.lift()
        if control==True:
                SearchScreen.mainloop() #Show Search Screen. It continues until control changes to False
        if control2 == True:
                ResultScreen=Tk()
                ResultScreen.title("Result Panel")
                ResultScreen.attributes('-fullscreen', True)
                Application3(ResultScreen)
                ResultScreen.mainloop()
                               

try:
        db.close()
except:
        pass
