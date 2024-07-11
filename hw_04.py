# Перше завдання

with open('salary_file.txt', 'w', encoding='utf-8') as f:
    f.write('Alex Korp,3000\n')
    f.write('Nikita Borisenko,2000\n')
    f.write('Sitarama Raju,1000\n')

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
                
            if count == 0:
                return (0, 0)
            
            average = total / count
            return (total, int(average))
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Друге завдання 

with open('cats_file.txt', 'w', encoding='utf-8') as f:
    f.write('60b90c1c13067a15887e1ae1,Tayson,3\n')
    f.write('60b90c2413067a15887e1ae2,Vika,1\n')
    f.write('60b90c2e13067a15887e1ae3,Barsik,2\n')
    f.write('60b90c3b13067a15887e1ae4,Simon,12\n')
    f.write('60b90c4613067a15887e1ae5,Tessi,5\n')
def get_cats_info(path):
    cats_info = []
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats_info
cats_info = get_cats_info("cats_file.txt")
print(cats_info)

# Четверте завдання 

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: change [name] [phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue
        
        command, args = parse_input(user_input)
        print(f"Received command: {command}, args: {args}")  # Додаткове діагностичне повідомлення

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(command, args)
            print("Invalid command.")

if __name__ == "__main__":
    main()

