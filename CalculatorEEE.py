import streamlit as st

st.title("GCD and LCM Calculator")

st.write("Enter your integers below.")

first = st.number_input("First Integer", step=1, format="%d")
second = st.number_input("Second Integer", step=1, format="%d")

choice = st.radio(
    "Do you have a third integer to input?",
    ["No", "Yes"]
)

third = None

if choice == "Yes":
    third = st.number_input("Third Integer", step=1, format="%d")


def gcd(a, b):
    steps = []

    while b != 0:
        quotient = a // b
        remainder = a % b

        steps.append(
            f"{a} ÷ {b} = {quotient} remainder {remainder}"
        )

        a = b
        b = remainder

    return a, steps


def lcm(a, b):
    gcd_value, _ = gcd(a, b)

    product = a * b
    result = product // gcd_value

    return gcd_value, product, result


if st.button("Calculate GCD and LCM"):

    if first == 0 or second == 0 or (choice == "Yes" and third == 0):
        st.error("Please enter integers other than 0.")
    else:

        # =========================
        # GCD COMPUTATION
        # =========================

        st.header("GCD Computation")

        gcd_first_second, gcd_steps = gcd(first, second)

        st.write(f"**GCD({first}, {second})**")

        for step in gcd_steps:
            st.write(step)

        st.write(
            f"**GCD({first}, {second}) = {gcd_first_second}**"
        )

        if choice == "Yes":

            final_gcd, gcd_steps = gcd(gcd_first_second, third)

            st.write(
                f"**GCD({gcd_first_second}, {third})**"
            )

            for step in gcd_steps:
                st.write(step)

            st.write(
                f"**GCD({gcd_first_second}, {third}) = {final_gcd}**"
            )

            st.success(f"Final GCD = {final_gcd}")

        else:

            final_gcd = gcd_first_second

            st.success(f"Final GCD = {final_gcd}")


        # =========================
        # LCM COMPUTATION
        # =========================

        st.header("LCM Computation")

        gcd_value, product, first_lcm = lcm(first, second)

        st.write(
            f"LCM({first}, {second})"
        )

        st.write(
            f"= ({first} × {second}) ÷ GCD({first}, {second})"
        )

        st.write(
            f"= {product} ÷ {gcd_value}"
        )

        st.write(
            f"= **{first_lcm}**"
        )

        if choice == "Yes":

            gcd_value_2, product_2, final_lcm = lcm(first_lcm, third)

            st.write("---")

            st.write(
                f"LCM({first_lcm}, {third})"
            )

            st.write(
                f"= ({first_lcm} × {third}) ÷ GCD({first_lcm}, {third})"
            )

            st.write(
                f"= ({first_lcm} × {third}) ÷ {gcd_value_2}"
            )

            st.write(
                f"= {product_2} ÷ {gcd_value_2}"
            )

            st.write(
                f"= **{final_lcm}**"
            )

            st.success(f"Final LCM = {final_lcm}")

        else:

            final_lcm = first_lcm

            st.success(f"Final LCM = {final_lcm}")