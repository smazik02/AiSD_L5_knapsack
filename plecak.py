import csv
import random
import timeit
from copy import deepcopy


# Generuje listę elementów
# Element jest 3-elementową listą z numerem elementu, jego wagą i wartością (waga i wartość to losowa wartość od 1 do 9)
def genItems(n: int) -> list[list[int]]:
    items = [[i+1, random.randint(1, 10), random.randint(1, 10)]
             for i in range(n)]
    return items

# Pobieranie elementu z pliku
# Tu nieużywana
def fromFile(filename: str) -> tuple[list[list[int]], int]:
    items = []
    data = []
    cap = 0
    with open(filename, "r") as file:
        data = [[int(x) for x in line.split()] for line in file]
    items = [[0, 0] for _ in range(data[0][0])]
    cap = data[0][1]
    del data[0]
    for i, line in enumerate(data):
        items[i][0] = i+1
        items[i][1] = line[0]
        items[i][2] = line[1]
    return items, cap


# Funkcja pomocnicza do sortowania listy elementów
# Zwraca stosunek wartości do masy
def getRatio(list: list[int]) -> float:
    return list[2]/list[1]


# Algorytm bruteforce
def bruteForce(items: list[list[int]], cap: int) -> str:
    elems = len(items)
    max = 0
    solution = "Brak rozwiązania"
    for i in range(1, 2**elems+1):
        knapsack = bin(i)[2:].zfill(elems)[::-1]
        massSum = sum(items[j][1]
                      for j in range(elems) if knapsack[j] == "1")
        if massSum > cap:
            continue
        valSum = sum(items[j][2]
                     for j in range(elems) if knapsack[j] == "1")
        if valSum > max:
            max = valSum
            solution = knapsack
    return solution


# Algorytm zachłanny
def greedy(items: list[list[int]], cap: int) -> str:
    copy = deepcopy(items)
    copy.sort(reverse=True, key=getRatio)
    knapsack = bin(0)[2:].zfill(len(copy))[::-1]
    knapsackLst = [*knapsack]
    i = 0
    weight = 0
    while i < len(copy) - 1:
        if weight+copy[i][1] <= cap:
            knapsackLst[copy[i][0]-1] = "1"
            weight += copy[i][1]
            i += 1
        if weight+copy[i][1] > cap:
            break
    knapsack = "".join(knapsackLst)
    return knapsack


# Algorytm dynamiczny
def dynamic(items: list[list[int]], cap: int) -> str:
    V = [[0]*(cap+1) for _ in range(len(items)+1)]
    weight = [items[x][1] for x in range(len(items))]
    value = [items[x][2] for x in range(len(items))]
    for i in range(1, len(items)+1):
        for j in range(1, cap+1):
            if weight[i-1] > j:
                V[i][j] = V[i-1][j]
            else:
                V[i][j] = max(V[i-1][j], V[i-1][j-weight[i-1]] + value[i-1])
    knapsackLst = ['0']*len(items)
    n = len(items)
    c = cap
    while n > 0:
        if V[n][c] > V[n-1][c]:
            knapsackLst[n-1] = '1'
            c -= weight[n-1]
        n -= 1
    knapsack = "".join(knapsackLst)
    return knapsack


results = {items: {cap: {"bruteForce": 0.0, "greedy": 0.0, "dynamic": 0.0}
                   for cap in range(5, 31, 5)} for items in range(2, 21, 2)}

for i in range(2, 21, 2):
    items = genItems(i)
    for cap in range(5, 31, 5):
        res1 = timeit.timeit(setup='from __main__ import bruteForce, items, cap',
                             stmt='bruteForce(items, cap)', number=20)/20
        res2 = timeit.timeit(setup='from __main__ import greedy, items, cap',
                             stmt='greedy(items, cap)', number=20)/20
        res3 = timeit.timeit(setup='from __main__ import dynamic, items, cap',
                             stmt='dynamic(items, cap)', number=20)/20
        results[i][cap]["bruteForce"] = res1*1000
        results[i][cap]["greedy"] = res2*1000
        results[i][cap]["dynamic"] = res3*1000
        print(f"{i} {cap}")
    print("")

with open("results/knapsack_cap30", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Elementy", "bruteForce", "greedy", "dynamic"])
    for n in range(2, 21, 2):
        writer.writerow([str(n), str(results[n][30]["bruteForce"]), str(
            results[n][30]["greedy"]), str(results[n][30]["dynamic"])])

with open("results/knapsack_n20", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Pojemnosc", "bruteForce", "greedy", "dynamic"])
    for cap in range(5, 31, 5):
        writer.writerow([str(n), str(results[20][cap]["bruteForce"]), str(
            results[20][cap]["greedy"]), str(results[20][cap]["dynamic"])])

with open("results/knapsack_bruteforce", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Pojemnosc/Elementy", 2, 4,
                    6, 8, 10, 12, 14, 16, 18, 20])
    for cap in range(5, 31, 5):
        tmp = [str(cap)] + [str(results[x][cap]["bruteForce"])
                            for x in range(2, 21, 2)]
        writer.writerow(tmp)

with open("results/knapsack_greedy", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Pojemnosc/Elementy", 3, 6,
                    9, 12, 15, 18, 21, 24, 27, 30])
    for cap in range(5, 31, 5):
        tmp = [str(cap)] + [str(results[x][cap]["greedy"])
                            for x in range(2, 21, 2)]
        writer.writerow(tmp)

with open("results/knapsack_dynamic", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Pojemnosc/Elementy", 3, 6,
                    9, 12, 15, 18, 21, 24, 27, 30])
    for cap in range(5, 31, 5):
        tmp = [str(cap)] + [str(results[x][cap]["dynamic"])
                            for x in range(2, 21, 2)]
        writer.writerow(tmp)
