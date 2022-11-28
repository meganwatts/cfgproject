import requests

user = input("Who is the user? Olivia/Megan ")
if user == "Megan":
    app_id = "ddaf1b46"
    app_key = "22ca23af7481a2718c3e3889bac0cf52"
elif user == "Olivia":
    app_id = "d13f3378"
    app_key = "c565b141f1289b921f22834414f67eb0"

def recipe_search(ingredient):
    url = "https://api.edamam.com/search?q={}&app_id={}&app_key={}".format(ingredient, app_id, app_key)
    result = requests.get(url)
    data = result.json()
    return data["hits"]

def run():
    ingredient = input("Enter an ingredient: ")

    results = recipe_search(ingredient)

    recipe_results = []
    # empty outer list created; recipe/label/uri/calories then saved as inner lists
    for result in results:
        recipe = result["recipe"]
        label = recipe["label"]
        uri = recipe["uri"]
        calories = recipe["calories"]
        print(label)
        print(uri)
        print(calories)
        recipe_results.append([label, uri, calories])
        print()

    # to order the list created by calories, not weight (ascending) - Googled this
    recipe_results.sort(key = lambda x: x[2])

    return(recipe_results)

# to create the text file containing the search results
with open("project.txt", "w+") as file:
    search_results = run()

    file.write(str(search_results))

run()
