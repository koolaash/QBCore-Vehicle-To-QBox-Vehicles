import re

def parse_input_line(line):
    """Parse a line of input into a dictionary"""
    pattern = r"\s*\{\s*model\s*=\s*'([^']+)',\s*name\s*=\s*'([^']+)',\s*brand\s*=\s*'([^']+)',\s*price\s*=\s*(\d+),\s*category\s*=\s*'([^']+)',\s*type\s*=\s*'([^']+)',\s*shop\s*=\s*'([^']+)'\s*\},?"
    match = re.match(pattern, line.strip())
    if not match:
        return None
    
    return {
        'model': match.group(1),
        'name': match.group(2),
        'brand': match.group(3),
        'price': int(match.group(4)),
        'category': match.group(5),
        'type': match.group(6),
        'shop': match.group(7)
    }

def convert_to_lua(vehicle):
    """Convert vehicle dictionary to Lua format"""
    new_price = int(vehicle['price'] * 1)
    return f"""    {vehicle['model']} = {{
        name = '{vehicle['name']}',
        brand = '{vehicle['brand']}',
        model = '{vehicle['model']}',
        price = {new_price},
        category = '{vehicle['category']}',
        type = '{vehicle['type']}',
        hash = `{vehicle['model']}`,
    }},"""

def process_file(input_file, output_file):
    """Process input file and write to output file"""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip():  # Skip empty lines
                vehicle = parse_input_line(line)
                if vehicle:
                    lua_output = convert_to_lua(vehicle)
                    outfile.write(lua_output + '\n\n')

if __name__ == "__main__":
    input_filename = 'input.txt'
    output_filename = 'output.lua'
    
    print(f"Processing {input_filename} to {output_filename}...")
    process_file(input_filename, output_filename)
    print("Conversion complete!")
    print("Made by kool_damon")