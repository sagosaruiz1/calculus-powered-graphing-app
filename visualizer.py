import matplotlib.pyplot as plt


def generate_plot(x_values, y_values, deriv_values, func_str):

    plt.figure(figsize=(10,6));

    plt.plot(x_values, y_values, label=f"Original: f(x) = {func_str}", color='blue', linewidth=2)

    plt.plot(x_values, deriv_values, label=f"Derivative: f'(x)", color='red', linestyle='--')

    plt.fill_between(x_values, y_values, color='orange', alpha=0.3, label="Integral (Area)")

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.title(f"Calculus Visualization for {func_str}", fontsize=14)
    plt.xlabel("x values", fontsize=12)
    plt.ylabel("y values", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)

    plt.savefig("calculus_output.png")
    print("Success: Graph saved as 'calculus_output.png'")

    plt.show()