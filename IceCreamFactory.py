from collections import deque
import time
import sys

class IceCreamFactory:
    def __init__(self, flavors, production_times):
        """
        Initialize the IceCreamFactory.
        Parameters:
        - flavors (list): List of ice cream flavors.
        - production_times (list): List of production times for each flavor.
        """
        self.flavors = flavors
        self.production_times = production_times
        self.queue = deque(zip(flavors, production_times))

    def round_robin_scheduler(self, quantum):
        """
        Simulate ice cream production using Round Robin scheduling.

        Parameters:
        - quantum (int): Time quantum for Round Robin scheduling.
        """
        while self.queue:
            flavor, time_left = self.queue.popleft()
            if time_left <= quantum:
                print(f"\n\n\t\tProducing {flavor} ice cream... ({time_left} seconds)")
                time.sleep(time_left)
                print(f"\n\t\t{flavor} ice cream production complete!\n")
            else:
                print(f"\n\n\t\tProducing {flavor} ice cream (time left: {time_left - quantum} seconds)")
                self.queue.append((flavor, time_left - quantum))

    def fcfs_scheduler(self):
        """Simulate ice cream production using First-Come, First-Served (FCFS) scheduling."""
        while self.queue:
            flavor, time_left = self.queue.popleft()
            print(f"\n\t\tProducing {flavor} ice cream... ({time_left} seconds)")
            time.sleep(time_left)
            print(f"\n\n\t\t{flavor} ice cream production complete!\n")

    def simulate_production(self, scheduling_algorithm, quantum=None):
        """
        Simulate ice cream production based on the specified scheduling algorithm.

        Parameters:
        - scheduling_algorithm (str): The scheduling algorithm to use ("Round Robin" or "FCFS").
        - quantum (int): Time quantum for Round Robin scheduling. Ignored if the algorithm is not Round Robin.
        """
        print(f"\n\n\t\tStarting ice cream production simulation with {scheduling_algorithm} scheduling:")
        if scheduling_algorithm == "Round Robin":
            self.round_robin_scheduler(quantum)
            print("\n\n\t\tProduction simulation completed.\n\t\tThank you for choosing us. Have a great day :)\n\n")
        elif scheduling_algorithm == "FCFS":
            self.fcfs_scheduler()
            print("\n\n\t\tProduction simulation completed.\n\t\tThank you for choosing us. Have a great day :)\n\n")
        else:
            print("\n\n\t\tInvalid choice.\n\t\t Please select a valid scheduling algorithm.")

# Get user input for ice cream flavors and production times
try:
    flavors = input("\n\t\tEnter ice cream flavors (comma-separated): ").split(',')
    production_times = [int(time) for time in input("\n\t\tEnter production times (comma-separated in seconds): ").split(',')]
    print("\n\t\tOKAY!!\n")
except ValueError:
    print("\n\t\tInvalid input. Please enter valid values for production times.")
    sys.exit(1)

# Create an IceCreamFactory object
ice_cream_factory = IceCreamFactory(flavors, production_times)

# Get user input for scheduling algorithm
print("\n\n\t\tHow do you want to schedule it?\n\n")
print("\t\t\t1. Round Robin")
print("\t\t\t2. First-Come, First-Served (FCFS)")

try:
    selected_algorithm = int(input("\n\t\tEnter the number: "))
    if selected_algorithm not in [1, 2]:
        raise ValueError("\n\t\t:((((((\n\nInvalid choice. Please select a valid scheduling algorithm.")
except ValueError as e:
    print(e)
    sys.exit(1)

# Start the simulation based on the selected algorithm
if selected_algorithm == 1:
    try:
        quantum_time = int(input("\n\t\tEnter time quantum for Round Robin scheduling (in seconds): "))
    except ValueError:
        print("\n\t\tInvalid input. Please enter a valid time quantum.")
        sys.exit(1)
    ice_cream_factory.simulate_production("Round Robin", quantum_time)
elif selected_algorithm == 2:
    ice_cream_factory.simulate_production("FCFS")
