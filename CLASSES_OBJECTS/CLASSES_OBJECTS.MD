# 🐍 PYTHON CLASSES & OBJECTS: INTERACTIVE GUIDE

"""
================================================================================
💡 CONCEPT DEFINITIONS
================================================================================
CLASS:  A blueprint, template, or prototype that defines the attributes (data) 
        and methods (behavior) that objects of this type will have.

OBJECT: A distinct instance created from a class blueprint. It contains real, 
        live data unique to itself and can execute behaviors.
================================================================================
"""

# ================================================================================
# 🛠️ EXAMPLE 1: Individual Class Definition (The Blueprint)
# ================================================================================
class IndividualProfile:
    """Defines a blueprint for tracking individual user profiles."""
    
    # Class Attribute (Shared by all user profiles)
    community = "Python Developers Network"

    # Constructor (Initializes unique individual attributes)
    def __init__(self, username, programming_language, experience_years):
        self.username = username                  # Individual unique attribute
        self.language = programming_language      # Individual unique attribute
        self.experience = experience_years        # Individual unique attribute

    # Instance Method (An action performed by an individual object)
    def introduce(self):
        return f"Hi, I am {self.username}! I specialize in {self.language}."

    # Instance Method (Modifies individual state data)
    def upgrade_experience(self):
        self.experience += 1
        return f"Congrats {self.username}! Experience updated to {self.experience} years."


# ================================================================================
# 🚀 EXAMPLE 2: Creating and Interacting with Individual Objects (Instances)
# ================================================================================
if __name__ == "__main__":
    print("🌐 --- Network Information ---")
    print(f"Community Platform: {IndividualProfile.community}\n")

    # 1. Creating Individual Object #1 (Alice)
    user_alice = IndividualProfile(username="Alice_Dev", programming_language="Python", experience_years=3)
    
    # 2. Creating Individual Object #2 (Bob)
    user_bob = IndividualProfile(username="Bob_Coder", programming_language="Java", experience_years=5)

    print("🔍 --- Displaying Individual States ---")
    # Interacting with Alice's object data and methods
    print(f"[Object: user_alice] Name: {user_alice.username} | Years: {user_alice.experience}")
    print(f"Action: {user_alice.introduce()}")
    
    print("-" * 50)
    
    # Interacting with Bob's object data and methods
    print(f"[Object: user_bob] Name: {user_bob.username} | Years: {user_bob.experience}")
    print(f"Action: {user_bob.introduce()}")

    print("\n⚡ --- Triggering Individual Actions & Updates ---")
    # Alice levels up her experience, changing only her object state, not Bob's
    print(user_alice.upgrade_experience())
    print(f"Verified Alice New Experience: {user_alice.experience} years")
    print(f"Verified Bob Unchanged Experience: {user_bob.experience} years"




----
🚀
**Happy Coding!** Practice these concepts by writing your own Python code.
