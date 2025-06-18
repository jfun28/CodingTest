
n = int(input())

file_extensions = {}

for _ in range(n):
    filename = input()
    extension = filename.split('.')[1]
    file_extensions[extension] = file_extensions.get(extension, 0) + 1

for extension in sorted(file_extensions):
    print(f'{extension} {file_extensions[extension]}')

# n=int(input())

# file_list=[]
# extent_list=[]
# file_name={}

# for _ in range(n):
#     file_list.append(input())


# for file in file_list:
#     extent_list.append(file.split('.')[1])

# for extent in extent_list:
#     if not extent in file_name:
#         file_name[extent]=1
#     else:
#         file_name[extent]+=1

# sorted_file_name=sorted(file_name)

# for name in sorted_file_name:
#     print(f'{name} {file_name[name]}')