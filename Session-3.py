# Name: Suchitra Yadawad
# Date: 09-08-2026
# Module 3: Core Fundamentals


# Task 1: Matrix Slicling and List Manipulation

# Data Setup
data_stream = list(range(21))

print("\n" + "=" * 40)
print("TASK 1: MATRIX SLICING AND LIST MANIPULATION")
print("=" * 40)

print(f"Original List: {data_stream}")

# Extract even numbers in reverse order
even_reverse = data_stream[20:0:-2]

print(f"Even numbers in reverse order: {even_reverse}")

# Extract middle five elements
middle_five = data_stream[8:13]

print(f"Middle five elements: {middle_five}")

# Mutability Test

data_stream[2:4] = ["MODIFIED", "MODIFIED"]

data_stream.append(99)
data_stream.insert(0, 0.5)

print(f"Final List: {data_stream}")
print(f"Final Length: {len(data_stream)}")

# ============================================================
# Task 2: Immutable Records & Tuple Unpacking
# ============================================================

# 1. The Record
employee = (101, "Alice Smith", "Data Engineer", "London")
print("\n" + "=" * 40)
print("TASK 2: IMMUTABLE RECORDS & TUPLE UNPACKING")
print("=" * 40)

print("Employee Record:", employee)

# 2. Unpacking
emp_id, name, role, location = employee

print("Employee ID:", emp_id)
print("Name:", name)
print("Role:", role)
print("Location:", location)

# 3. Extended Unpacking
employee_details = (101, "Alice Smith", "Data Engineer", "London", "Full-Time", 75000)

head, *mid, tail = employee_details

print("Head:", head)
print("Middle:", mid)
print("Tail:", tail)

# 4. Immutability Proof
# employee[3] = "New York"
# TypeError: 'tuple' object does not support item assignment

# ============================================================
# Task 3: Deduplication and Set Hashability
# ============================================================

print("\n" + "=" * 40)
print("TASK 3: DEDUPLICATION AND SET HASHABILITY")
print("=" * 40)

# 1. Cleaning Data
user_ids = [1001, 1002, 1001, 1005, 1003, 1002, 1008]
unique_ids = set(user_ids)

print("Original User IDs:", user_ids)
print("Unique IDs:", unique_ids)

# 2. Immutability Constraint
# unique_ids.add([1, 2])
# TypeError: unhashable type: 'list'

# 3. Set Growth
unique_ids.add(1009)
unique_ids.update([1010, 1011])

print("Updated Unique IDs:", unique_ids)

# ============================================================
# Task 4: Mathematical Set Operations
# ============================================================

print("\n" + "=" * 40)
print("TASK 4: MATHEMATICAL SET OPERATIONS")
print("=" * 40)

# 1. The Scenario
frontend_devs = {"HTML", "CSS", "JS", "React", "Python"}
backend_devs = {"Python", "Java", "NodeJS", "Go", "JS"}

# 2. Operations

# Full Stack: Union
all_skills = frontend_devs.union(backend_devs)
print("Union - All Skills:", all_skills)

# Overlap: Intersection
common_skills = frontend_devs.intersection(backend_devs)
print("Intersection - Common Skills:", common_skills)

# Specialists: Difference
backend_only = backend_devs.difference(frontend_devs)
print("Difference - Backend Only:", backend_only)

# Unique to One: Symmetric Difference
unique_skills = frontend_devs.symmetric_difference(backend_devs)
print("Symmetric Difference - Unique Skills:", unique_skills)

# ============================================================
# Task 5: The "Collection Conversion" Pipeline
# ============================================================

print("\n" + "=" * 40)
print('TASK 5: "COLLECTION CONVERSION" PIPELINE')
print("=" * 40)

# 1. The Flow
numbers_tuple = (4.5, 2.1, 8.7, 1.3, 6.2)
print("Original Tuple:", numbers_tuple)

# Convert Tuple into List
numbers_list = list(numbers_tuple)
print("Converted List:", numbers_list)

# Sort the List in ascending order
numbers_list.sort()
print("Sorted List:", numbers_list)

# Convert List into Set
numbers_set = set(numbers_list)
print("Converted Set:", numbers_set)

# Add a duplicate value and check the size
size_before = len(numbers_set)
numbers_set.add(numbers_list[0])
size_after = len(numbers_set)

print("Set Size Before Duplicate:", size_before)
print("Set Size After Duplicate:", size_after)

# Convert Set back into Tuple
final_tuple = tuple(numbers_set)
print("Final Tuple:", final_tuple)

# 2. Memory Identity
print("List Memory Address:", id(numbers_list))
print("Set Memory Address:", id(numbers_set))