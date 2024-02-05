class ClimateChangeProgram:
    def __init__(self):
        self.responses = {}

    def run_iteration(self, iteration_number):
        if iteration_number == 1:
            self.identify_and_acknowledge_issue()
        elif iteration_number == 2:
            self.introduce_sustainable_practices()
        elif iteration_number == 3:
            self.encourage_energy_conservation()
        elif iteration_number == 4:
            self.promote_green_transportation()
        else:
            print("Invalid iteration number")

    def identify_and_acknowledge_issue(self):
        print("Iteration 1: Identify and Acknowledge the Issue")
        awareness = input("Are you aware of climate change? (yes/no): ")
        self.responses["Awareness"] = awareness
        print(f"User is aware of climate change: {awareness}")

    def introduce_sustainable_practices(self):
        print("Iteration 2: Introduce Sustainable Practices")
        engage_sustainable = input("Do you engage in sustainable practices? (yes/no): ")
        self.responses["Engage Sustainable Practices"] = engage_sustainable

        if engage_sustainable.lower() == "yes":
            actions = input("Specify sustainable actions (e.g., recycling, reducing energy consumption): ")
            self.responses["Sustainable Actions"] = actions
            print(f"User's sustainable actions: {actions}")

            print("Providing information on the environmental impact of their actions...")
            # Placeholder for environmental impact information

    def encourage_energy_conservation(self):
        print("Iteration 3: Encourage Energy Conservation")
        energy_consumption = input("How would you describe your energy consumption habits?: ")
        self.responses["Energy Consumption Habits"] = energy_consumption

        if "high" in energy_consumption.lower():
            print("Suggesting energy-efficient alternatives...")
            # Placeholder for suggesting alternatives

        print(f"User's energy consumption habits: {energy_consumption}")
        print("Highlighting the importance of collective efforts in energy conservation...")

    def promote_green_transportation(self):
        print("Iteration 4: Promote Green Transportation")
        transportation_choice = input("What is your preferred mode of transportation?: ")
        self.responses["Transportation Choice"] = transportation_choice

        if transportation_choice.lower() in ["car", "suv"]:
            print("Encouraging the use of public transport, cycling, or electric vehicles...")
            # Placeholder for promoting green transportation

        print(f"User's transportation choice: {transportation_choice}")
        print("Providing information on sustainable transportation options...")

# Main program
climate_program = ClimateChangeProgram()

# Run each iteration
for iteration_number in range(1, 5):
    climate_program.run_iteration(iteration_number)

# Display collected responses
print("\nCollected Responses:")
for key, value in climate_program.responses.items():
    print(f"{key}: {value}")