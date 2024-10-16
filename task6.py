class ProjectIntegration:
   
    
    def __init__(self):
        print("Welcome to the Big Project Integration!")
    
    def project_1(self):
        # Code for your first project
        print("Running Project 1...")
        # Add functionality from your first project here

    def project_2(self):
        # Code for your second project
        print("Running Project 2...")
        # Add functionality from your second project here
    
    def project_3(self):
        # Code for your third project
        print("Running Project 3...")
        # Add functionality from your third project here
    
    def project_4(self):
        # Code for your fourth project
        print("Running Project 4...")
        # Add functionality from your fourth project here
    
    def project_5(self):
        # Code for your fifth project
        print("Running Project 5...")
        # Add functionality from your fifth project here

    def main(self):
        while True:
            print("\nPlease choose which project to run:")
            print("1. Project 1")
            print("2. Project 2")
            print("3. Project 3")
            print("4. Project 4")
            print("5. Project 5")
            print("0. Exit")
            
            choice = input("Enter the project number: ")
            
            if choice == '1':
                self.project_1()
            elif choice == '2':
                self.project_2()
            elif choice == '3':
                self.project_3()
            elif choice == '4':
                self.project_4()
            elif choice == '5':
                self.project_5()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        

if __name__ == "__main__":
    app = ProjectIntegration()
    app.main()
