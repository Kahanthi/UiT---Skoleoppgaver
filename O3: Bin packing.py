class Bin:
    def __init__(self, maxWeight=10):
        self.maxWeight = maxWeight
        self.totalWeight = 0
        self.objects = []

    def addItem(self, weight):
        if self.totalWeight + weight <= self.maxWeight:
            self.objects.append(weight)
            self.totalWeight += weight
            return True
        else:
            return False

    def getNumberOfObjects(self):
        return len(self.objects)

    def __str__(self):
        output = ""
        for e in self.objects:
            output += str(e) + " "
        return output

def main():
    bins = []  # A list to store the containers

    while True:
        weight_str = input("Enter the weight of the object (or 'q' to quit): ")

        if weight_str.lower() == 'q':
            break

        try:
            weight = float(weight_str)
            added = False

            for bin in bins:
                if bin.addItem(weight):
                    added = True
                    break

            if not added:
                new_bin = Bin()
                new_bin.addItem(weight)
                bins.append(new_bin)

        except ValueError:
            print("Invalid input. Please enter a valid weight.")

    print("Total number of containers:", len(bins))

    for i, bin in enumerate(bins, 1):
        print(f"Container {i} contents: {bin}")

if __name__ == "__main__":
    main()