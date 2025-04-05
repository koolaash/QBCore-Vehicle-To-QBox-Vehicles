
# QBcore Vehicle.lua to Qbox Vehicle.lua

This Python script converts vehicle data from a structured text format into a Lua-compatible table format. It reads entries from an `input.txt` file, processes each line to extract vehicle attributes (model, name, brand, price, etc.), reformats them into a new Lua table structure, and writes the output to `output.lua`.

# Key Feature
✔ Automated Data Parsing – Uses regex to extract vehicle attributes from input lines.

✔ Price Conversion – Automatically adjusts prices (multiplies by `1` [can be changed]).

✔ Lua Table Formatting – Structures output in a clean, readable Lua table format.

✔ File I/O Handling – Reads from input.txt and writes to output.lua.

✔ Error-Resilient – Skips empty or malformed lines.

# Input and output formats
- input
```lua
{ model = 'blista', name = 'Blista', brand = 'Dinka', price = 80000, category = 'compacts', type = 'automobile', shop = 'pdm' },
```

- output
```lua
blista = {
    name = 'Blista',
    brand = 'Dinka',
    model = 'blista',
    price = 69371,
    category = 'compacts',
    type = 'automobile',
    hash = `blista`,
},
```
# How to use 
- Place all your data in `input.lua` 
- Run the `main.py`
- Open `output.lua`

# Requirements
- Python 3.x
- Input file (input.txt) with properly formatted entries