nums = [1, 2, 3]
print("Tipo: " + str(type(nums)))

nums.append(3)
nums.append(4)
nums.append(5)
print('Tamanho da lista: ' + str(len(nums)))

nums[3] = 100

nums.insert(0, -1)

print("Lista:" + str(nums))

print(f"Ultimo: {nums[6]}") 
print(f"Ultimo: {nums[-1]}") 
print(f"Antepenultimo: {nums[-2]}") 