def towerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towerOfHanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    towerOfHanoi(n - 1, auxiliary, destination, source)

n = 4  
towerOfHanoi(n, 'A', 'C', 'B') 