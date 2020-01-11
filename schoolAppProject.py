
class TODO:
    
    """ 
                            ============ Description of class ============
    
    TODO class initiates a new TODO list. TODO items can be added to a list and viewed for reference. You initialize this class with a TODO list name. The add_TODO method is where you add new TODO items to your list. The TODO_viewer method is used to print your TODO list (name and list).
    
    The list is stored in the class attribute TODO_list as a list.
    """
    
    TODO_list = []
    
    def __init__(self, TODO_list_name):
        """ 
                                    ============ __init__ ============
            enter TODO_list_name parameter as a string.
        """
        
        self.TODO_list_name = TODO_list_name
        
        
    def add_TODO(self, description, due_date, classification, priority, course = "n/a", classroom = "n/a"):
        
        """ 
                                    ============ add_TODO ============
            The add_TODO method is used to create a new todo item to be added to the list.
            description is a string.
            due_date is a date entered as string.
            classification accepts string values "Personal", "Academic", "Work", "Leisure"
            priority accepts string values of "Urgent", "Intermediate", and "Optional"
            course is string.
            classroom is a string.
        """
        
        self.description = description
        self.due_date = due_date
        self.classification = classification
        self.priority = priority
        self.course = course
        self.classroom = classroom
        
        new_item = ["Description: " + self.description,"Due date: " + self.due_date,"Classification: " + self.classification,"Priority: " + self.priority,"Course: " + self.course,"Classroom: " + self.classroom]
        
        self.TODO_list.append(new_item)
    
    
    def TODO_viewer(self):
        """ 
            ============ TODO_viewer ============
            method to print todo list and title
        """
        print(self.TODO_list_name)
        print(self.TODO_list)
        
class Tracker:
    """ 
        ============ Title ============
       The Tracker class is used to create a tracker for a students classess. You initilize the class with a tracker name. The add_class method is used to add a new class to the tracker. The tracker_viewer method is used to view the tracker. The tracker stores the classes in the class attribute class_list as a list. 
    """
    class_list = []
    
    def __init__(self, class_tracker_name):
        self.class_tracker_name = class_tracker_name
        
        
    def add_class(self,class_code, professor, start_time, end_time, classroom):
        """ 
            ============ add_class ============
            class_code accepts a string or int.
            professor accepts a string.
            start_time accepts the time as a string
            end_time accepts the time as a string
            classroom accepts a string
        """
        self.class_code = class_code
        self.professor = professor
        self.start_time = start_time
        self.end_time = end_time
        self.classroom = classroom
        
        new_item = ["Class code: " + self.class_code,"Professor: " + self.professor, "Start time: " + self.start_time, "End time: " + self.end_time, "Classroom: " + self.classroom]
        
        self.class_list.append(new_item)
    
    
    def tracker_viewer(self):
        """ 
            ============ Title ============
           print the class_list 
        """
        print(self.class_tracker_name)
        print(self.class_list)
        
        
        
        
        
        
        