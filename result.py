def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d_remove = d.replace("$","")
    d_nulles = d_remove.replace(".00",".0")
    d_nulles2 = float(d_nulles)
    return d_nulles2
    pass
def percent_to_float(p):
    p_remove = p.replace("%","")
    p_floats = float(p_remove)/100
    return p_floats
    pass
main()
