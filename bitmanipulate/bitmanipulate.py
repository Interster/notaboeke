#%%
# Vanaf die volgende bron:
# https://www.anurag629.club/posts/the-power-of-bit-manipulation-how-to-solve-problems-efficiently

#%%
# Bitwise AND & operator
x = 5 # 0101
y = 3 # 0011

temp = x & y 
print(temp)
print(f'{temp:b}')
print(bin(temp))



# %%
# Bitwise OR | operator
temp = x | y 
print(temp)
print(f'{temp:b}')
print(bin(temp))
# %%

# Bitwise XOR ^ operator
temp = x ^ y 
print(temp)
print(f'{temp:b}')
print(bin(temp))
# %%

# Bitwise NOT ~ operator

temp = ~x 
print(temp)
print(f'{temp:b}')
print(bin(temp))
# %%

# Bitwise left shift << operator

temp = x << 1
print(temp)
print(f'{temp:b}')
print(bin(temp))
# %%


