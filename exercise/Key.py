
# 🧠 Easy rules for using f-strings in Python:

# 1. Use f"..." or f'...'
#    Always write f-strings inside double quotes " " or single quotes ' '

# 2. Use {} to insert values
#    Put variables or math inside the curly braces { }
#    ❌ Don't put "student_name" in quotes — that just prints the text
#    ✅ Do this: f"{student_name}"

# 3. You can insert numbers, strings, or math
#    Examples:
#    - f"{name}" → puts the value of the name variable
#    - f"{a + b}" → does math and puts the result
#    - f"{x:.2f}" → format a number to 2 decimal places (e.g. 3.14)

student_id = "z123456"
student_name = "JuneY"
score = 100


key = f"{student_id}|{student_name} {score}"
print(key)

