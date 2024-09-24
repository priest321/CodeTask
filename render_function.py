"""
def generate_function(data):
    function_name = data.get("function")
    args = data.get("args", [])
    kwargs = data.get("kargs", {})
    
    def generated_function(*args, **kwargs):
        name = args[0]
        prices = args[1]
        brand = kwargs.get("brand")
        return name
    
    return generated_function

# Create the function based on the data dictionary
data = {
    "args": ["toyota", "30000"],
    "kargs": {"brand": "rav4"},
    "return": True
}

get_name_function = generate_function(data)

# Call the generated function with the specified arguments
result = get_name_function("toyota", "30000", brand="rav4")
print(result)  # Output: toyota
"""


data = {
	"function": "generate_return_function",
	"kargs": {"name": "toyota", "prices": "30000", "discount": "0.05", "brand": "rav4"},
	"return": ["prices", -, (, "prices", *, "discount", )]
}


function_mapping = {
    "generate_return_function": general_func
}


def general_func(result, **kargs):
    return kargs

def process_data(data:dict):
    function_type = data.get("function")
    result = function_mapping.get(function_type)
    print(result)
    
process_data(data)
    




