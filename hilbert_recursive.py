import matplotlib.pyplot as plt


def hilbert_curve(order):
    """
    Generate a Hilbert curve recursively.

    Returns a list of (x, y) coordinates.
    """

    # Base case
    if order == 1:
        return [
            (0, 0),
            (0, 1),
            (1, 1),
            (1, 0)
        ]

    # Get the smaller Hilbert curve
    previous = hilbert_curve(order - 1)

    size = 2 ** (order - 1)

    curve = []

    # --------------------------------------------------
    # Bottom-left quadrant
    # Rotate the previous curve
    # --------------------------------------------------

    for x, y in previous:
        curve.append((y, x))

    # --------------------------------------------------
    # Top-left quadrant
    # Move previous curve upward
    # --------------------------------------------------

    for x, y in previous:
        curve.append((x, y + size))

    # --------------------------------------------------
    # Top-right quadrant
    # Move previous curve upward and right
    # --------------------------------------------------

    for x, y in previous:
        curve.append((x + size, y + size))

    # --------------------------------------------------
    # Bottom-right quadrant
    # Rotate the previous curve
    # --------------------------------------------------

    for x, y in reversed(previous):
        curve.append(
            (2 * size - 1 - y, size - 1 - x)
        )

    return curve


def draw_curve(order):

    points = hilbert_curve(order)

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(8, 8))

    plt.plot(
        x,
        y,
        linewidth=2
    )

    # Mark start
    plt.scatter(
        x[0],
        y[0],
        s=80,
        marker="o",
        label="Start"
    )

    # Mark end
    plt.scatter(
        x[-1],
        y[-1],
        s=80,
        marker="s",
        label="End"
    )

    # Number each point
    if order <= 3:

        for i, (px, py) in enumerate(points):

            plt.text(
                px,
                py,
                str(i),
                fontsize=8,
                ha="center",
                va="center"
            )

    size = 2 ** order

    plt.xlim(-1, size)
    plt.ylim(-1, size)

    plt.xticks(range(size))
    plt.yticks(range(size))

    plt.grid(True)

    plt.gca().set_aspect("equal")

    plt.title(
        f"Hilbert Space-Filling Curve\n"
        f"Order {order} | "
        f"{size} × {size} | "
        f"{len(points)} points"
    )

    plt.legend()

    plt.show()


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    print("HILBERT SPACE-FILLING CURVE")
    print("----------------------------")

    try:
        order = int(input("Enter order (1-6): "))

        if order < 1 or order > 6:
            raise ValueError

    except ValueError:
        print("Invalid order. Using order 3.")
        order = 3

    draw_curve(order)