# input the temperature in Farenheit
# calculate Celsius as C = (F - 32).(0.5556)
# output in Celsius
def main():
    # function that converts temperature from degrees Celsius to Farenheit
    print("--- Temperature Converter ---")
    fstr = input("What is the Farenheit temperature? ")
    f = float(fstr)
    f = round((f - 32) * (0.5556))
    print("the temperature is: ", f, "degrees Celsius")

main()
