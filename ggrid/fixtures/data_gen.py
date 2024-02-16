import json
# Let's correct the approach to ensure categories are properly assigned to their corresponding shelves within each section.

# Resetting the counters and lists to ensure proper assignment
section_id = 1
shelf_id = 1
category_id = 1
fixture = []

# Detailed category assignments for shelves within each section
category_assignments = {
    "Produce": {
        "Apples": ["Gala Apple", "Fuji Apple", "Granny Smith Apple", "Honeycrisp Apple", "Empire Apple", "Red Delicious Apple"],
        "Citrus": ["Navel Orange", "Mandarin Orange", "Lemon", "Lime"],
        "Leafy Greens": ["Spinach", "Kale", "Lettuce", "Arugula"]
    },
    "Meats": {
        "Beef": ["Ground Beef", "Steak", "Beef Ribs"],
        "Poultry": ["Chicken Breast", "Chicken Thighs", "Turkey"],
        "Pork": ["Pork Chops", "Ham", "Bacon"]
    },
    "Dairy": {
        "Milk": ["Whole Milk", "Skim Milk", "Butter"],
        "Cheese": ["Cheddar Cheese", "Mozzarella Cheese"],
        "Yogurt": ["Greek Yogurt", "Regular Yogurt", "Flavored Yogurt"]
    },
    "Bakery": {
        "Breads": ["White Bread", "Whole Wheat Bread"],
        "Pastries": ["Croissant", "Danish"],
        "Cakes": ["Cheesecake", "Chocolate Cake", "Carrot Cake"]
    },
    "Canned Goods": {
        "Vegetables": ["Canned Corn", "Canned Peas", "Canned Carrots"],
        "Fruits": ["Canned Peaches", "Canned Pears", "Canned Pineapple"],
        "Soups": ["Chicken Soup", "Tomato Soup", "Beef Stew"]
    },
    "Frozen Foods": {
        "Vegetables": ["Frozen Peas", "Frozen Corn"],
        "Meals": ["Frozen Pizza", "Frozen Lasagna"],
        "Desserts": ["Ice Cream", "Frozen Yogurt"]
    }
}

# Function to add categories to fixture
def add_categories(shelf_name, categories):
    global category_id
    for category in categories:
        fixture.append({
            "model": "ggrid.category",
            "pk": category_id,
            "fields": {
                "name": category,
                "shelf": shelf_id  # Linking category to the correct shelf
            }
        })
        category_id += 1

for section_name, shelves in category_assignments.items():
    # Add section
    fixture.append({
        "model": "ggrid.section",
        "pk": section_id,
        "fields": {"name": section_name}
    })
    section_id += 1
    
    for shelf_name, categories in shelves.items():
        # Add shelf
        fixture.append({
            "model": "ggrid.shelf",
            "pk": shelf_id,
            "fields": {
                "name": shelf_name,
                "section": section_id - 1  # Linking shelf to the correct section
            }
        })
        
        # Add categories to this shelf
        add_categories(shelf_name, categories)
        
        shelf_id += 1

# Output corrected mock data
json_output_corrected = json.dumps(fixture, indent=2)
json_output_corrected
f = open("data.json", "w")
f.write(json_output_corrected)
f.close()