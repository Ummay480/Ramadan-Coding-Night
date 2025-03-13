import streamlit as st

def main():
    st.title("🧮 Simple Calculator")
    st.write("This is a simple calculator app built with Streamlit.")

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number",value=0.0)
    with col2:
        num2 = st.number_input("Enter second number",value=0.0)

    operation = st.selectbox("Choose operation", ["Addition (+)", "Subtraction (-)", "Multipplication (*)", "Division (/)"])

    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (*)":
                result = num1 * num2    
                symbol = "*"
            else:
                if num2 == 0:
                    st.error("Error: Division by zero")
                    return
                else:
                 result = num1 / num2
                 symbol = "/"

            st.success(f"The result of {num1} {symbol} {num2} is {result}")
             
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

#Run the main function if the script is executed directly
if __name__ == "__main__":
    main()

                
                         
    
