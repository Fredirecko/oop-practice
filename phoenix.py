class Phoenix:
    """Class that represents a phoenix creature.
    
    Attributes:
        health (int): the health expressed as an interger associated with the instance of phoenix.
        is_alive(bool): the boolean that indicates whether the phoenix is alive or dead.
        
    Methods:
        death(): an if/else statement that check the phoenix's health. If the health is <= 0 it prints, 
                "The phoenix crumbles to the ground and dies!". If the phoenix's health is > 0 it prints, "The 
                phoenix is alive and well!".
        reborn(): an if/else statement that checks the phoenix's is_alive(bool) attribute. If is_alive == False
                the phoenix's health is reset to 10, is_alive is set to True, and prints, "The phoenix is reborn!" 
                If is_alive != False than it prints,"The phoenix is already alive and well! The phoenix's health is
                {health}".
    """
    
    
    def __init__(self, health=10, is_alive=True):
        """Initialize the values of the instance attributes of an instance of Phoenix.
        
        Args:
            health(int): initializes all phoenix instances with 10 health. 
            is_alive(bool): all phoenix's begin with a boolean value of True.
        """
        self.health = health
        self.is_alive = is_alive
        
    def death(self):
        """Check death state of phoenix."""
        if self.health <=0:
            self.is_alive=False
            print("The phoenix crumbles to the ground and dies!")
        else:
            print("The phoenix is alive and well!")
            
    def reborn(self):
        """Check death state of phoenix and ressurrect phoenix, if phoenix dead."""
        if self.is_alive == False:
            self.is_alive = True
            self.health = 10
            print("The phoenix is reborn!")
        else:
            print(f"The phoenix is already alive and well! The phoenix's health is {self.health}.")
        
phoenix = Phoenix()
print(phoenix.health)