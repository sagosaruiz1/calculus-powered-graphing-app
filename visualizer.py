import matplotlib.pyplot as plt


def generate_plot(x_values, y1_values, y2_values, deriv_values, f1_str, f2_str, mode):
    plt.figure(figsize=(10,6));

    plt.plot(x_values, y1_values, label=f"f(x) = {f1_str}", color='blue', lw=2)
    plt.plot(x_values, deriv_values, label=f"f'(x)", color='red', linestyle='--')

    if mode == "Between Curves":
        plt.plot(x_values, y2_values, label=f"g(x) = {f2_str}", color='purple', lw=2)
    else:
        plt.axhline(0, color='black', lw=1)
        plt.title(f"Area under Curve: {f1_str}")

    plt.fill_between(x_values, y1_values, y2_values, color='orange', alpha=0.3, label="Integral Area")


    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.title(f"Calculus Visualization for {func_str}", fontsize=14)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)

    plt.savefig("calculus_output.png")
    print("Success: Graph saved as 'calculus_output.png'")

    plt.show()