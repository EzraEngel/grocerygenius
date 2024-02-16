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
        "Apples": [("Gala Apple", 1.99), ("Fuji Apple", 2.29), ("McIntosh Apple", 1.39), ("Empire Apple", 1.89), ("Honeycrisp Apple", 2.99), ("Granny Smith Apple", 1.79), ("Red Delicious Apple", 1.49), ("Golden Delicious Apple", 1.59)],
        "Citrus": [("Navel Orange", 1.29), ("Blood Orange", 2.99), ("Lemon", 1.49), ("Lime", 0.99), ("Grapefruit", 1.99), ("Mandarin Orange", 3.49), ("Tangerine", 0.69), ("Clementine", 4.49)],
        "Leafy Greens": [("Spinach", 2.99), ("Kale", 2.99), ("Romaine Lettuce", 1.99), ("Arugula", 2.49), ("Swiss Chard", 3.49), ("Collard Greens", 2.29), ("Mustard Greens", 1.99), ("Iceberg Lettuce", 1.49)],
        "Other Greens": [("Broccoli", 3.99), ("Brussel Sprouts", 3.99), ("Green Beans", 3.99), ("Asparagus", 3.99), ("Cauliflower", 3.99)],
        "Peppers": [("Bell Pepper Green", 0.99), ("Bell Pepper Red", 1.49), ("Bell Pepper Yellow", 1.49), ("Jalapeño", 0.69), ("Habanero", 0.99), ("Poblano", 1.29)],
        "Berries": [("Strawberry", 4.99), ("Blueberry", 3.99), ("Raspberry", 4.49), ("Blackberry", 4.99), ("Gooseberry", 6.99), ("Currant", 5.99), ("Mulberry", 7.49), ("Elderberry", 8.99)],
        "Stone Fruits": [("Peach", 2.49), ("Plum", 2.99), ("Cherry", 5.99), ("Apricot", 3.49), ("Nectarine", 2.99), ("Mango", 1.99), ("Lychee", 9.99), ("Persimmon", 3.99)],
        "Tomatoes": [("Beefsteak Tomato", 2.99), ("Cherry Tomato", 3.49), ("Heirloom Tomato", 4.99), ("Roma Tomato", 2.49), ("Grape Tomato", 3.29), ("Green Tomato", 2.79), ("Yellow Tomato", 3.59), ("Kumato", 4.29)],
        "Root Vegetables": [("Carrot", 1.49), ("Beetroot", 1.99), ("Turnip", 1.79), ("Radish", 1.99), ("Sweet Potato", 0.99), ("Parsnip", 2.49), ("Rutabaga", 1.59), ("Ginger", 0.99)],
        "Exotic Fruits": [("Dragon Fruit", 6.99), ("Papaya", 3.49), ("Star Fruit", 4.99), ("Passion Fruit", 1.99), ("Guava", 2.49), ("Kiwi Fruit", 0.99), ("Pineapple", 3.99), ("Mangosteen", 11.99)]
    },
    "Deli": {
        "Sliced Meats": [("Turkey Breast", 7.99), ("Ham", 6.49), ("Roast Beef", 9.99), ("Salami", 8.49), ("Prosciutto", 11.99), ("Pastrami", 10.49), ("Chicken Breast", 7.49), ("Corned Beef", 9.89)],
        "Sliced Cheeses": [("Swiss Cheese", 5.99), ("Cheddar Cheese", 5.49), ("Provolone Cheese", 6.99), ("American Cheese", 4.49), ("Gouda Cheese", 8.99), ("Mozzarella Cheese", 7.49), ("Pepper Jack Cheese", 5.89), ("Havarti Cheese", 7.99)],
        "Prepared Salads": [("Potato Salad", 4.99), ("Macaroni Salad", 4.99), ("Coleslaw", 3.99), ("Chicken Salad", 6.99), ("Egg Salad", 5.49), ("Tuna Salad", 7.49), ("Seafood Salad", 8.99), ("Pasta Salad", 5.99)],
        "Rotisserie Chickens": [("Whole Rotisserie Chicken", 7.99), ("Half Rotisserie Chicken", 4.99), ("Rotisserie Chicken Breast", 6.99), ("Rotisserie Chicken Wings", 5.99)],
        "Sandwiches and Wraps": [("Turkey Sandwich", 6.99), ("Ham and Cheese Sandwich", 6.49), ("Chicken Caesar Wrap", 7.49), ("Veggie Wrap", 6.99), ("BLT Sandwich", 5.99), ("Roast Beef Sandwich", 7.99), ("Italian Sub", 8.49), ("Tuna Sandwich", 6.99)],
        "Hot Foods": [("Fried Chicken", 8.99), ("BBQ Ribs", 12.99), ("Meatloaf", 9.99), ("Mashed Potatoes", 4.99), ("Mac and Cheese", 5.99), ("Lasagna", 10.99), ("Chicken Wings", 9.49), ("Pizza Slice", 2.99)],
        "Olives and Antipasti": [("Mixed Olives", 8.99), ("Stuffed Peppers", 9.99), ("Marinated Artichokes", 10.49), ("Sun-Dried Tomatoes", 7.99), ("Mozzarella Balls", 6.49), ("Grilled Mushrooms", 8.49), ("Hummus", 5.99), ("Baba Ganoush", 6.99)],
        "Fresh Dips and Spreads": [("Hummus", 5.99), ("Guacamole", 6.99), ("Pimento Cheese", 7.49), ("Artichoke Dip", 8.49), ("Tzatziki", 5.49), ("Salsa", 4.99), ("Bean Dip", 6.49), ("Spinach Dip", 7.99)]
    },
    "Bakery": {
        "Bread Loaves": [("Sourdough Loaf", 4.99), ("Whole Wheat Bread", 3.49), ("Multigrain Bread", 3.99), ("Rye Bread", 4.49), ("French Baguette", 2.99), ("Ciabatta", 3.89), ("Pumpernickel Bread", 4.99), ("Focaccia", 5.49)],
        "Bagels and Muffins": [("Plain Bagel", 0.99), ("Sesame Bagel", 1.09), ("Blueberry Muffin", 2.49), ("Chocolate Chip Muffin", 2.49), ("Cinnamon Raisin Bagel", 1.09), ("Everything Bagel", 1.19), ("Bran Muffin", 2.29), ("Pumpkin Muffin", 2.79)],
        "Cakes and Cupcakes": [("Chocolate Cake", 15.99), ("Vanilla Cupcake", 2.99), ("Red Velvet Cake", 18.99), ("Carrot Cake", 16.99), ("Lemon Cupcake", 2.99), ("Cheesecake", 19.99), ("Black Forest Cake", 20.99), ("Strawberry Shortcake", 17.99)],
        "Pastries and Croissants": [("Butter Croissant", 2.49), ("Chocolate Croissant", 2.99), ("Danish Pastry", 3.49), ("Apple Turnover", 2.99), ("Pain au Chocolat", 3.19), ("Almond Croissant", 2.89), ("Eclair", 3.99), ("Tiramisu Pastry", 4.49)],
        "Cookies and Biscotti": [("Chocolate Chip Cookie", 1.49), ("Oatmeal Raisin Cookie", 1.49), ("Macadamia Nut Cookie", 1.99), ("Ginger Snap", 0.99), ("Shortbread", 1.79), ("Peanut Butter Cookie", 1.49), ("Almond Biscotti", 2.29), ("Double Chocolate Cookie", 1.99)],
        "Pies and Tarts": [("Apple Pie", 12.99), ("Pecan Pie", 14.99), ("Lemon Meringue Tart", 11.99), ("Blueberry Pie", 13.99), ("Pumpkin Pie", 9.99), ("Key Lime Tart", 10.99), ("Cherry Pie", 12.99), ("Banoffee Pie", 15.99)],
        "Specialty Breads": [("Olive Bread", 5.99), ("Walnut Bread", 6.49), ("Cheese Bread", 6.99), ("Onion Bread", 5.49), ("Garlic Bread", 4.99), ("Potato Bread", 4.49), ("Zucchini Bread", 7.99), ("Cornbread", 5.29)],
        "Gluten-Free Options": [("Gluten-Free Bread", 6.99), ("Gluten-Free Muffins", 4.99), ("Gluten-Free Cookies", 5.49), ("Gluten-Free Cake", 15.99), ("Gluten-Free Pizza Base", 8.99), ("Gluten-Free Brownies", 6.49), ("Gluten-Free Cupcakes", 7.99)]
    },
    "Meat and Seafood": {
        "Beef": [("Ribeye Steak", 14.99), ("Ground Beef", 4.99), ("Sirloin Steak", 9.99), ("Chuck Roast", 7.99), ("Filet Mignon", 19.99), ("Beef Brisket", 8.99), ("T-Bone Steak", 13.99), ("Beef Ribs", 12.49)],
        "Poultry": [("Chicken Breast", 3.99), ("Whole Chicken", 1.49), ("Chicken Thighs", 2.99), ("Chicken Wings", 3.49), ("Turkey Breast", 4.99), ("Ground Turkey", 4.49), ("Duck Breast", 8.99), ("Cornish Hen", 5.99)],
        "Pork": [("Pork Chops", 3.99), ("Bacon", 5.99), ("Ground Pork", 3.49), ("Pork Loin", 2.99), ("Sausage Links", 4.99), ("Ham", 3.29), ("Pork Belly", 5.49), ("Pork Tenderloin", 6.99)],
        "Lamb": [("Lamb Chops", 10.99), ("Ground Lamb", 7.99), ("Lamb Shank", 5.99), ("Rack of Lamb", 14.99), ("Leg of Lamb", 9.99), ("Lamb Ribs", 8.99), ("Lamb Shoulder", 6.99), ("Lamb Stew Meat", 7.49)],
        "Seafood": [("Salmon Fillet", 8.99), ("Shrimp", 12.99), ("Lobster Tails", 15.99), ("Crab Legs", 18.99), ("Tilapia Fillet", 6.99), ("Cod Fillet", 7.99), ("Clams", 4.99), ("Mussels", 4.49)],
        "Fresh Fish": [("Tuna Steak", 9.99), ("Halibut Fillet", 14.99), ("Trout", 7.99), ("Swordfish Steak", 11.99), ("Red Snapper", 8.99), ("Mahi Mahi", 7.99), ("Grouper", 13.99), ("Sea Bass", 17.99)],
        "Shellfish": [("Scallops", 19.99), ("Oysters", 0.99), ("King Crab Legs", 29.99), ("Snow Crab Legs", 19.99), ("Shucked Oysters", 12.99), ("Live Lobsters", 14.99), ("Prawns", 15.99), ("Crayfish", 8.99)],
        "Marinated Meats": [("Marinated Chicken Breast", 4.99), ("Marinated Pork Ribs", 5.99), ("Marinated Beef Steaks", 7.99), ("Marinated Lamb Kebabs", 9.99), ("Marinated Shrimp", 14.99), ("Marinated Salmon", 10.99)]
    },
    "Dairy": {
        "Milk": [("Whole Milk", 3.49), ("2% Milk", 3.29), ("Skim Milk", 3.19), ("Chocolate Milk", 3.99), ("Almond Milk", 2.99), ("Soy Milk", 2.89), ("Oat Milk", 3.79), ("Coconut Milk", 3.49)],
        "Cheese": [("Cheddar Cheese", 4.99), ("Mozzarella Cheese", 5.49), ("Parmesan Cheese", 6.99), ("Goat Cheese", 7.49), ("Blue Cheese", 8.99), ("Gouda Cheese", 5.99), ("Swiss Cheese", 5.49), ("Feta Cheese", 6.29)],
        "Yogurt": [("Greek Yogurt", 3.99), ("Plain Yogurt", 2.99), ("Flavored Yogurt", 4.49), ("Non-Dairy Yogurt", 3.89), ("Low-Fat Yogurt", 3.49), ("Whole Milk Yogurt", 4.29), ("Kefir", 4.99), ("Icelandic Skyr", 5.29)],
        "Butter and Margarine": [("Unsalted Butter", 3.99), ("Salted Butter", 3.89), ("Spreadable Butter", 4.49), ("Light Butter", 2.99), ("Vegan Butter", 5.49), ("Margarine", 2.79), ("Clarified Butter (Ghee)", 6.99), ("Whipped Butter", 3.49)],
        "Eggs": [("Large White Eggs", 2.69), ("Large Brown Eggs", 2.99), ("Organic Eggs", 4.49), ("Free-Range Eggs", 3.99), ("Egg Whites", 4.99), ("Liquid Egg Substitute", 3.49), ("Pasture-Raised Eggs", 5.29), ("Omega-3 Enriched Eggs", 3.89)],
        "Cream and Creamers": [("Heavy Cream", 3.99), ("Half-and-Half", 2.49), ("Whipping Cream", 3.49), ("Light Cream", 2.99), ("Coffee Creamer", 2.79), ("Non-Dairy Creamer", 3.29), ("Sour Cream", 1.99), ("Creme Fraiche", 5.49)],
        "Cultured Dairy": [("Cottage Cheese", 2.99), ("Sour Cream", 1.99), ("Cream Cheese", 2.49), ("Ricotta Cheese", 3.99), ("Mascarpone", 4.89), ("Buttermilk", 2.79), ("Quark", 3.49), ("Labneh", 4.99)]
    },
    "Frozen Foods": {
        "Frozen Vegetables": [("Mixed Vegetables", 2.99), ("Broccoli Florets", 2.49), ("Sweet Corn", 2.29), ("Peas", 1.99), ("Green Beans", 2.59), ("Spinach", 1.89), ("Brussels Sprouts", 3.49), ("Cauliflower", 2.39)],
        "Frozen Fruits": [("Mixed Berries", 3.99), ("Strawberries", 3.49), ("Blueberries", 4.29), ("Mango Chunks", 3.59), ("Pineapple Chunks", 3.29), ("Dark Sweet Cherries", 4.99), ("Peach Slices", 3.89), ("Raspberry", 4.49)],
        "Ice Cream and Desserts": [("Vanilla Ice Cream", 4.99), ("Chocolate Ice Cream", 5.29), ("Gelato", 5.99), ("Sorbet", 4.79), ("Frozen Yogurt", 4.49), ("Ice Cream Sandwiches", 3.99), ("Frozen Cheesecake", 6.99), ("Popsicles", 3.49)],
        "Frozen Meals": [("Pizza", 5.99), ("Lasagna", 7.99), ("Macaroni and Cheese", 6.49), ("Vegetarian Burgers", 4.99), ("Chicken Tenders", 6.99), ("Stir Fry Mixes", 4.89), ("Burritos", 3.79), ("Breakfast Sandwiches", 4.59)],
        "Frozen Seafood": [("Shrimp", 8.99), ("Fish Fillets", 7.49), ("Scallops", 12.99), ("Crab Cakes", 9.99), ("Lobster Tails", 14.99), ("Salmon Burgers", 8.49), ("Tilapia", 6.99), ("Cod", 7.99)],
        "Frozen Meat": [("Chicken Breasts", 9.99), ("Ground Beef", 4.99), ("Pork Chops", 7.99), ("Meatballs", 8.49), ("Sausages", 5.99), ("Turkey Burgers", 9.49), ("Beef Patties", 10.99), ("Duck", 12.99)],
        "Frozen Pizza": [("Pepperoni Pizza", 5.99), ("Cheese Pizza", 5.49), ("Supreme Pizza", 6.99), ("Margherita Pizza", 7.49), ("BBQ Chicken Pizza", 6.49), ("Veggie Pizza", 5.99), ("Thin Crust Pizza", 4.99), ("Deep Dish Pizza", 7.99)],
        "Frozen Bread and Dough": [("Bread Dough", 2.99), ("Croissants", 4.49), ("Bagels", 3.99), ("Pita Bread", 2.79), ("Pizza Dough", 3.49), ("Dinner Rolls", 3.29), ("Garlic Bread", 3.59), ("Pie Crusts", 2.99)]
    },
    "Dry Goods and Pantry": {
        "Cereal and Breakfast Foods": [("Oatmeal", 3.99), ("Granola", 4.49), ("Corn Flakes", 2.99), ("Whole Grain Cereal", 3.89), ("Instant Breakfast Mix", 4.99), ("Pancake Mix", 2.79), ("Breakfast Bars", 5.49)],
        "Pasta and Rice": [("Spaghetti", 1.49), ("Penne", 1.59), ("Basmati Rice", 2.99), ("Brown Rice", 2.49), ("Risotto Rice", 3.99), ("Whole Wheat Pasta", 1.89), ("Ramen Noodles", 0.99)],
        "Canned Goods": [("Diced Tomatoes", 0.99), ("Black Beans", 1.19), ("Corn", 0.89), ("Chicken Broth", 2.29), ("Tuna Fish", 1.99), ("Chickpeas", 1.29), ("Green Beans", 0.79)],
        "Oil and Vinegar": [("Olive Oil", 8.99), ("Vegetable Oil", 2.99), ("Balsamic Vinegar", 5.99), ("Apple Cider Vinegar", 3.49), ("Coconut Oil", 6.49), ("Canola Oil", 2.79)],
        "Spices and Seasonings": [("Sea Salt", 2.49), ("Black Pepper", 3.19), ("Cinnamon", 2.99), ("Curry Powder", 3.59), ("Paprika", 2.89), ("Garlic Powder", 2.79), ("Oregano", 1.99)],
        "Baking Ingredients": [("Flour", 2.29), ("Sugar", 2.49), ("Baking Soda", 0.99), ("Baking Powder", 1.29), ("Vanilla Extract", 4.99), ("Cocoa Powder", 3.49), ("Yeast", 1.49)],
        "Snacks": [("Potato Chips", 3.49), ("Pretzels", 2.99), ("Popcorn", 1.99), ("Trail Mix", 4.99), ("Energy Bars", 1.49), ("Cookies", 3.59), ("Chocolate Bars", 1.99)],
        "Coffee and Tea": [("Ground Coffee", 7.99), ("Green Tea", 4.49), ("Herbal Tea", 3.99), ("Black Tea", 3.49), ("Coffee Pods", 6.99), ("Loose Leaf Tea", 5.29), ("Espresso Beans", 8.49)],
        "Sauces and Condiments": [("Tomato Sauce", 1.99), ("Mustard", 1.49), ("Ketchup", 2.29), ("Soy Sauce", 2.99), ("Hot Sauce", 3.49), ("Barbecue Sauce", 2.79), ("Mayonnaise", 3.89)]
    },
    "Beverages": {
        "Water": [("Spring Water", 0.99), ("Mineral Water", 1.49), ("Sparkling Water", 1.29), ("Flavored Water", 1.09)],
        "Soft Drinks": [("Cola", 1.29), ("Diet Soda", 1.19), ("Root Beer", 1.29), ("Ginger Ale", 1.09), ("Lemon-Lime Soda", 1.19)],
        "Juice": [("Orange Juice", 3.49), ("Apple Juice", 2.99), ("Cranberry Juice", 3.99), ("Grape Juice", 3.29), ("Tomato Juice", 2.79)],
        "Coffee": [("Ground Coffee", 7.99), ("Whole Bean Coffee", 8.49), ("Instant Coffee", 4.99), ("Coffee Pods", 6.99)],
        "Tea": [("Black Tea", 3.49), ("Green Tea", 4.49), ("Herbal Tea", 3.99), ("Chai", 4.99)],
        "Energy Drinks": [("Energy Drink", 2.49), ("Sports Drink", 1.99), ("Electrolyte Beverage", 2.29), ("Energy Shot", 2.99)],
        "Alcoholic Beverages": [("Beer", 1.49), ("Wine", 9.99), ("Spirits", 15.99), ("Hard Seltzer", 8.99)],
        "Dairy Alternatives": [("Almond Milk", 2.99), ("Soy Milk", 2.89), ("Coconut Milk", 3.49), ("Oat Milk", 3.79)]
    },
    "Health and Beauty": {
        "Personal Care": [("Shampoo", 4.99), ("Conditioner", 4.99), ("Body Wash", 5.49), ("Bar Soap", 1.99), ("Deodorant", 3.49), ("Toothpaste", 2.99), ("Mouthwash", 4.29)],
        "Skin Care": [("Facial Cleanser", 6.99), ("Moisturizer", 8.49), ("Sunscreen", 7.99), ("Acne Treatment", 9.49), ("Anti-Aging Cream", 15.99), ("Body Lotion", 5.99)],
        "Hair Care": [("Hair Dye", 6.99), ("Styling Gel", 4.49), ("Hairspray", 5.29), ("Hair Mask", 7.99), ("Leave-In Conditioner", 6.49), ("Dry Shampoo", 5.99)],
        "Oral Care": [("Toothbrush", 2.99), ("Toothpaste", 2.99), ("Dental Floss", 3.49), ("Mouthwash", 4.29), ("Teeth Whitening Strips", 19.99)],
        "Feminine Products": [("Sanitary Pads", 5.49), ("Tampons", 6.99), ("Menstrual Cup", 29.99), ("Panty Liners", 4.49)],
        "Healthcare": [("First Aid Kit", 9.99), ("Pain Reliever", 4.99), ("Cold and Flu Medicine", 6.49), ("Allergy Relief", 12.99), ("Band-Aids", 2.49)],
        "Dietary Supplements": [("Multivitamins", 14.99), ("Protein Powder", 19.99), ("Omega-3 Supplements", 17.99), ("Vitamin D", 9.99), ("Probiotics", 16.99)],
        "Baby Care": [("Diapers", 24.99), ("Baby Wipes", 5.99), ("Baby Shampoo", 4.99), ("Baby Lotion", 7.49), ("Baby Formula", 16.99)]
    },
    "Household Essentials": {
        "Cleaning Supplies": [("All-Purpose Cleaner", 3.99), ("Glass Cleaner", 2.99), ("Disinfectant Wipes", 4.49), ("Bathroom Cleaner", 3.89), ("Floor Cleaner", 5.99), ("Furniture Polish", 4.79)],
        "Laundry Products": [("Laundry Detergent", 9.99), ("Fabric Softener", 6.99), ("Bleach", 3.49), ("Stain Remover", 4.99), ("Dryer Sheets", 4.49), ("Laundry Pods", 10.99)],
        "Paper Goods": [("Paper Towels", 1.99), ("Toilet Paper", 0.89), ("Facial Tissues", 1.29), ("Napkins", 2.49)],
        "Air Fresheners": [("Spray Air Freshener", 2.99), ("Plug-In Air Freshener", 4.99), ("Candles", 5.99), ("Reed Diffusers", 7.49), ("Car Air Freshener", 3.49)],
        "Light Bulbs": [("LED Bulbs", 5.99), ("Incandescent Bulbs", 2.49), ("Halogen Bulbs", 3.99), ("Smart Light Bulbs", 14.99), ("Fluorescent Tubes", 7.99)],
        "Batteries": [("AA Batteries", 4.99), ("AAA Batteries", 4.99), ("9V Batteries", 5.49), ("Rechargeable Batteries", 8.99), ("Button Cell Batteries", 2.99)],
        "Trash Bags": [("Kitchen Trash Bags", 5.49), ("Heavy Duty Trash Bags", 6.99), ("Recycling Bags", 4.99), ("Compostable Trash Bags", 5.99)],
        "Pest Control": [("Ant Killer", 4.49), ("Roach Spray", 5.99), ("Mouse Traps", 6.49), ("Insect Repellent", 7.99), ("Moth Balls", 3.99)]
    }
}


    # "Produce": {
    #     "Apples": ["Gala Apple", "Fuji Apple", "Granny Smith Apple", "Honeycrisp Apple", "Empire Apple", "Red Delicious Apple"],
    #     "Citrus": ["Navel Orange", "Mandarin Orange", "Lemon", "Lime"],
    #     "Leafy Greens": ["Spinach", "Kale", "Lettuce", "Arugula"]
    # },
    # "Meats": {
    #     "Beef": ["Ground Beef", "Steak", "Beef Ribs"],
    #     "Poultry": ["Chicken Breast", "Chicken Thighs", "Turkey"],
    #     "Pork": ["Pork Chops", "Ham", "Bacon"]
    # },
    # "Dairy": {
    #     "Milk": ["Whole Milk", "Skim Milk", "Butter"],
    #     "Cheese": ["Cheddar Cheese", "Mozzarella Cheese"],
    #     "Yogurt": ["Greek Yogurt", "Regular Yogurt", "Flavored Yogurt"]
    # },
    # "Bakery": {
    #     "Breads": ["White Bread", "Whole Wheat Bread"],
    #     "Pastries": ["Croissant", "Danish"],
    #     "Cakes": ["Cheesecake", "Chocolate Cake", "Carrot Cake"]
    # },
    # "Canned Goods": {
    #     "Vegetables": ["Canned Corn", "Canned Peas", "Canned Carrots"],
    #     "Fruits": ["Canned Peaches", "Canned Pears", "Canned Pineapple"],
    #     "Soups": ["Chicken Soup", "Tomato Soup", "Beef Stew"]
    # },
    # "Frozen Foods": {
    #     "Vegetables": ["Frozen Peas", "Frozen Corn"],
    #     "Meals": ["Frozen Pizza", "Frozen Lasagna"],
    #     "Desserts": ["Ice Cream", "Frozen Yogurt"]
    # }

# Function to add categories to fixture
def add_categories(shelf_name, categories):
    global category_id
    for category in categories:
        fixture.append({
            "model": "ggrid.category",
            "pk": category_id,
            "fields": {
                "name": category[0],
                "price": str(category[1]),
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