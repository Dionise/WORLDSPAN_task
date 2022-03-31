# Exercise 1, __call__ the class!

class StatPostInit:
    """
    This needs amending!
    """

    def __init__(self, a_parameter: str):
        """
        Sets a_parameter to this initial value.
        :param a_parameter: A parameter
        """
        self.a_parameter = a_parameter

    def show_parameter(self):
        print(f"The parameter is set to: {self.a_parameter}")

    def change_parameter(self, new_parameter: str):
        self.a_parameter = new_parameter
        print(f"The parameter is set to: {self.a_parameter}")

if __name__ == "__main__":
    instance = StatPostInit(a_parameter="a string value")
    instance.show_parameter()
    # Modify the StatPostInit class so the parameter a_parameter can be modified, post initialisation, thus:
    instance.change_parameter(new_parameter="a_parameter is now |mutable| and can be changed from outside the object")
    # Finally, what is the one word that describes the new ability you have added, to the StatPostInit class?
    