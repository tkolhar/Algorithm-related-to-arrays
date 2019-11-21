def sort_positive(arr):
    pos = []
    for i in range(0, len(arr)):
        if arr[i] > 0:
           pos.append(arr[i])
    pos.sort()
    j=0
    for i in range(0, len(arr)):
        if arr[i]>=0:
           arr[i] = pos[j]
           j +=1
    return arr

def main():
    arr = [28, -6, -3, 8, 4, 1, -5, -8, 23, 2]
    pos = sort_positive(arr)  
    print(pos)

if __name__ == "__main__":
   main()            
