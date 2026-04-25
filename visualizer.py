import matplotlib.pyplot as plt


def generate_plot(x_values, y1_values, y2_values, deriv_values, f1_str, f2_str, mode, df_str):
    plt.figure(figsize=(10,6))

    pretty_f1 = f1_str.replace("**", "^").replace("*", "")
    pretty_f2 = f2_str.replace("**", "^").replace("*", "")
    pretty_df = df_str.replace("**", "^").replace("*", "")

    plt.plot(x_values, y1_values, label=f"$f(x) = {pretty_f1}$", color='blue', lw=2)
    plt.plot(x_values, deriv_values, label=f"$f'(x)= {pretty_df}$", color='red', linestyle='--')

    if mode == "Between Curves":
        plt.plot(x_values, y2_values, label=f"$g(x) = {pretty_f2}$", color='purple', lw=2)
        plt.title(f"Area Between ${pretty_f1}$ and ${pretty_f2}$", fontsize=14)
    else:
        plt.axhline(0, color='black', lw=1)
        plt.title(f"Area under the Curve: ${pretty_f1}$", fontsize=14)

    plt.fill_between(x_values, y1_values, y2_values, color='orange', alpha=0.3, label="Integral Area")


    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)

    plt.savefig("calculus_output.png")
    print("Success: Graph saved as 'calculus_output.png'")

    plt.show()