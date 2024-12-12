import numpy as np

# কাস্টম ডেটা টাইপ তৈরি করছি
employee_dtype = np.dtype([
    ('IDs', 'i4'),               # কর্মচারীর ID, 32-বিট পূর্ণসংখ্যা (integer)
    ('Name', 'U20'),             # কর্মচারীর নাম, 20 অক্ষরের ইউনিকোড স্ট্রিং
    ('Age', 'i4'),               # কর্মচারীর বয়স, 32-বিট পূর্ণসংখ্যা (integer)
    ('Salary', 'f4'),            # কর্মচারীর বেতন, 32-বিট ফ্লোটিং পয়েন্ট সংখ্যা (float)
    ('Join_Date', 'U10')         # যোগদান তারিখ, 10 অক্ষরের স্ট্রিং (ফরম্যাট: 'YYYY-MM-DD')
])

# কর্মচারীদের তথ্য
employee_data = np.array([
    (1, 'Alice', 30, 55000.50, '2015-08-15'),
    (2, 'Bob', 45, 65000.75, '2010-05-10'),
    (3, 'Charlie', 28, 48000.00, '2019-02-23'),
    (4, 'David', 38, 72000.25, '2013-07-19'),
    (5, 'Eve', 26, 52000.80, '2020-09-30')
], dtype=employee_dtype)

# কর্মচারীদের তথ্য প্রিন্ট করা
print("Employee Data:")
print(employee_data)

# কিছু নির্দিষ্ট কলাম একসাথে বের করা
print("\nEmployee Names:")
print(employee_data['Name'])

print("\nEmployee Salaries:")
print(employee_data['Salary'])

# একটি কর্মচারীর তথ্য বের করা
print("\nDetails of Employee with ID 2:")
print(employee_data[employee_data['IDs'] == 2])





