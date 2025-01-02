def weathering_model():
    with open('Input.txt', 'r') as file:
        lines = file.readlines()
        a = float(lines[0])
        b = float(lines[1])
        c = float(lines[2])
        x = float(lines[3])
    
    # Quadratic equation calculation
    W = a * x**2 + b * x + c
    
    print(f"Weathering index (W): {W}")

weathering_model()