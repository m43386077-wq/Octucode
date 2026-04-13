#كلاس للوصفات 
class Recipe:

    # تهيئة: اسم، مكونات، وقت طهي، تعليمات 
    def __init__(self, name, ingredients, cooking_time, instructions):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.instructions = instructions
        
    # ميثود للطباعة 
    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Cooking Time: {self.cooking_time} minutes")
        print(f"Instructions: {self.instructions}")        


# فانكشن لإنشاء وصفة 
def create_recipe():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma separated): ")
    cooking_time = input("Enter the cooking time in minutes: ")
    instructions = input("Enter the cooking instructions: ")
    return Recipe(name, ingredients, cooking_time, instructions)

# إنشاء وصفة وعرضها 
print("Welcome to the Recipe Collection!")
my_recipe = create_recipe()

print("Recipe added successfully!\n")

print("Displaying Recipe....\n")
my_recipe.display_recipe()
