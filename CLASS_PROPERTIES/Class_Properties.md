# 🐍 Python Class Properties (`@property`) ⚙️

Python properties allow you to create **managed attributes**. They let you define methods that behave exactly like normal data attributes, giving you total control over how data is accessed, modified, and deleted.

---

## 🛠️ 1. What Are Class Properties?

In Python, the `@property` decorator turns a class method into a "getter". Instead of calling a method with parentheses like `object.get_name()`, you can access it cleanly like a regular variable using `object.name`. 

By using companion decorators like `@name.setter` and `@name.deleter`, you can control exactly what happens when someone tries to change or delete that variable.

### 💻 Complete Code Example
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # We use a leading underscore (e.g., _balance) to mark it as internal/private
        self._balance = balance  

    # 📥 1. THE GETTER: Allows reading the value like an attribute
    @property
    def balance(self):
        print("🔍 Fetching the current balance...")
        return self._balance

    # 📤 2. THE SETTER: intercepts assignments and validates the data
    @balance.setter
    def balance(self, value):
        print(f"⚡ Attempting to set balance to: {value}")
        if value < 0:
            raise ValueError("❌ Balance cannot be negative!")
        self._balance = value

    # 🗑️ 3. THE DELETER: Prevents accidental deletion of vital data
    @balance.deleter
    def balance(self):
        raise AttributeError("🔒 You cannot delete the balance attribute!")

# --- 🧪 Testing the Property Code ---
account = BankAccount("Alice", 1000)

# Accessing the property (Calls the Getter implicitly)
print(account.balance)  # Output: 1000

# Modifying the property safely (Calls the Setter implicitly)
account.balance = 1500
print(account.balance)  # Output: 1500

# Triggering validation errors via the Setter
try:
    account.balance = -50  # This will crash without a try-except block
except ValueError as e:
    print(f"🛑 Blocked! Error: {e}")

# Triggering protection via the Deleter
try:
    del account.balance
except AttributeError as e:
    print(f"🛑 Blocked! Error: {e}")
```

---

## 💡 2. Why Use Properties?

* **🛡️ Data Validation**: You can stop bad data (like negative prices or empty strings) from breaking your application.
* **📦 Encapsulation**: You protect the internal state of your objects while maintaining a beautiful, clean public API.
* **🔄 Computed Values**: You can calculate fields dynamically on the fly (like a `fullname` calculated from `first_name` and `last_name`) without storing unnecessary variables.
* **🔌 Backward Compatibility**: If you start with a simple public variable and realize later that you need validation, you can swap it to a property without rewriting any of the external code that already uses it.

---

## ⚠️ 3. What Will Affect Your Code If You Do NOT Use Properties?

If you choose to bypass properties and use plain attributes instead, your code is highly vulnerable to the following problems:

### 🚨 Problem A: Silently Corrupted Data
Without a setter to act as a gatekeeper, code from anywhere in your project can assign invalid values to your object's internal state.
```python
class BadProduct:
    def __init__(self, price):
        self.price = price # Plain attribute, no properties

item = BadProduct(10)
item.price = -500  # ❌ Critical Error: Python allows this! Your app now has a negative price.
```

### 💥 Problem B: Breaking Existing Code (The Refactoring Nightmare)
If you try to fix the corrupted data issue down the line by creating manual Java-style getter/setter methods (like `set_price()` and `get_price()`), **you will break every single line of code in your project** that previously used `object.price`.
```python
# Old style:
print(item.price)

# If you convert to manual methods later because you didn't use @property:
print(item.get_price()) # ❌ Every file using your class must be found and rewritten!
```

### 📉 Problem C: Out-of-Sync / Stale Data
If you have data variables dependent on each other, failing to compute them dynamically via a property means your variables will fall completely out of sync when updates occur.
```python
class BrokenUser:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = f"{first} {last}" # Stored as a static string once

user = BrokenUser("John", "Doe")
user.first = "Jane"

print(user.fullname) # ❌ Output is still "John Doe"! The data is completely out of sync.
```
----
🚀
**Happy Coding!** Practice these concepts by writing your own Python code.
