import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button


# ============================================================
# HILBERT CURVE
# ============================================================

class HilbertCurve:

    def __init__(self, order):

        if order < 1:
            raise ValueError("Order must be at least 1")

        self.order = order
        self.size = 2 ** order
        self.total_points = self.size * self.size

    def d_to_xy(self, d):

        x = 0
        y = 0

        t = d
        s = 1

        while s < self.size:

            rx = 1 & (t // 2)
            ry = 1 & (t ^ rx)

            if ry == 0:

                if rx == 1:
                    x = s - 1 - x
                    y = s - 1 - y

                x, y = y, x

            x += s * rx
            y += s * ry

            t //= 4
            s *= 2

        return x, y

    def generate(self):

        points = []

        for d in range(self.total_points):
            points.append(self.d_to_xy(d))

        return points


# ============================================================
# VISUALIZER
# ============================================================

class HilbertVisualizer:

    def __init__(self, order=4):

        self.order = order
        self.curve = HilbertCurve(order)
        self.points = self.curve.generate()

        self.current_point = 1
        self.running = False

        # ----------------------------------------------------
        # Figure
        # ----------------------------------------------------

        self.fig, self.ax = plt.subplots(
            figsize=(9, 9)
        )

        plt.subplots_adjust(
            bottom=0.25
        )

        # ----------------------------------------------------
        # Curve line
        # ----------------------------------------------------

        self.line, = self.ax.plot(
            [],
            [],
            linewidth=2
        )

        # ----------------------------------------------------
        # Current point
        # ----------------------------------------------------

        self.current_marker, = self.ax.plot(
            [],
            [],
            marker="o",
            markersize=8,
            linestyle=""
        )

        # ----------------------------------------------------
        # Start point
        # ----------------------------------------------------

        self.start_marker, = self.ax.plot(
            [],
            [],
            marker="o",
            markersize=8,
            linestyle=""
        )

        # ----------------------------------------------------
        # End point
        # ----------------------------------------------------

        self.end_marker, = self.ax.plot(
            [],
            [],
            marker="s",
            markersize=8,
            linestyle=""
        )

        # ----------------------------------------------------
        # Animation
        # ----------------------------------------------------

        self.animation = FuncAnimation(
            self.fig,
            self.update,
            frames=self.get_frames,
            interval=30,
            repeat=False,
            cache_frame_data=False
        )

        # ----------------------------------------------------
        # Buttons
        # ----------------------------------------------------

        play_axis = plt.axes(
            [0.10, 0.08, 0.12, 0.05]
        )

        self.play_button = Button(
            play_axis,
            "Play"
        )

        self.play_button.on_clicked(
            self.play
        )

        pause_axis = plt.axes(
            [0.24, 0.08, 0.12, 0.05]
        )

        self.pause_button = Button(
            pause_axis,
            "Pause"
        )

        self.pause_button.on_clicked(
            self.pause
        )

        restart_axis = plt.axes(
            [0.38, 0.08, 0.12, 0.05]
        )

        self.restart_button = Button(
            restart_axis,
            "Restart"
        )

        self.restart_button.on_clicked(
            self.restart
        )

        # ----------------------------------------------------
        # Speed slider
        # ----------------------------------------------------

        speed_axis = plt.axes(
            [0.58, 0.09, 0.30, 0.03]
        )

        self.speed_slider = Slider(
            speed_axis,
            "Speed",
            1,
            100,
            valinit=30,
            valstep=1
        )

        self.speed_slider.on_changed(
            self.change_speed
        )

        # ----------------------------------------------------
        # Setup graph
        # ----------------------------------------------------

        self.setup_plot()

    # ========================================================
    # SETUP GRAPH
    # ========================================================

    def setup_plot(self):

        self.ax.clear()

        self.ax.set_aspect("equal")

        self.ax.set_xlim(
            -0.5,
            self.curve.size - 0.5
        )

        self.ax.set_ylim(
            -0.5,
            self.curve.size - 0.5
        )

        self.ax.set_xticks(
            range(self.curve.size)
        )

        self.ax.set_yticks(
            range(self.curve.size)
        )

        self.ax.grid(True)

        self.ax.set_title(
            f"Hilbert Space-Filling Curve\n"
            f"Order {self.order} | "
            f"Grid {self.curve.size} x {self.curve.size} | "
            f"Points {self.curve.total_points}"
        )

        self.line, = self.ax.plot(
            [],
            [],
            linewidth=2
        )

        self.current_marker, = self.ax.plot(
            [],
            [],
            marker="o",
            markersize=8,
            linestyle=""
        )

        self.start_marker, = self.ax.plot(
            [],
            [],
            marker="o",
            markersize=8,
            linestyle=""
        )

        self.end_marker, = self.ax.plot(
            [],
            [],
            marker="s",
            markersize=8,
            linestyle=""
        )

    # ========================================================
    # GENERATE FRAME NUMBERS
    # ========================================================

    def get_frames(self):

        for i in range(
            1,
            len(self.points) + 1
        ):
            yield i

    # ========================================================
    # UPDATE ANIMATION
    # ========================================================

    def update(self, frame):

        if not self.running:
            return (
                self.line,
                self.current_marker,
                self.start_marker,
                self.end_marker
            )

        visible_points = self.points[:frame]

        x = [
            point[0]
            for point in visible_points
        ]

        y = [
            point[1]
            for point in visible_points
        ]

        # Draw curve
        self.line.set_data(
            x,
            y
        )

        # Current point
        self.current_marker.set_data(
            [x[-1]],
            [y[-1]]
        )

        # Start point
        self.start_marker.set_data(
            [self.points[0][0]],
            [self.points[0][1]]
        )

        # End point only after reaching it
        if frame == len(self.points):

            self.end_marker.set_data(
                [self.points[-1][0]],
                [self.points[-1][1]]
            )

        else:

            self.end_marker.set_data(
                [],
                []
            )

        self.ax.set_title(
            f"Hilbert Space-Filling Curve\n"
            f"Order {self.order} | "
            f"Point {frame} / {len(self.points)}"
        )

        return (
            self.line,
            self.current_marker,
            self.start_marker,
            self.end_marker
        )

    # ========================================================
    # PLAY
    # ========================================================

    def play(self, event=None):

        self.running = True

        self.animation.event_source.start()

    # ========================================================
    # PAUSE
    # ========================================================

    def pause(self, event=None):

        self.running = False

        self.animation.event_source.stop()

    # ========================================================
    # RESTART
    # ========================================================

    def restart(self, event=None):

        self.running = True

        self.current_point = 1

        self.line.set_data(
            [],
            []
        )

        self.current_marker.set_data(
            [],
            []
        )

        self.end_marker.set_data(
            [],
            []
        )

        self.animation.frame_seq = (
            self.animation.new_frame_seq()
        )

        self.animation.event_source.start()

    # ========================================================
    # SPEED
    # ========================================================

    def change_speed(self, value):

        speed = int(value)

        # Higher slider value = faster animation
        interval = max(
            1,
            101 - speed
        )

        self.animation.event_source.interval = interval

    # ========================================================
    # SHOW
    # ========================================================

    def show(self):

        self.running = True

        plt.show()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("=" * 50)
    print("       HILBERT SPACE-FILLING CURVE")
    print("=" * 50)

    print()
    print("Order 1  ->  2 x 2    ->  4 points")
    print("Order 2  ->  4 x 4    ->  16 points")
    print("Order 3  ->  8 x 8    ->  64 points")
    print("Order 4  ->  16 x 16  ->  256 points")
    print("Order 5  ->  32 x 32  ->  1024 points")
    print("Order 6  ->  64 x 64  ->  4096 points")
    print()

    try:

        order = int(
            input("Enter Hilbert curve order (1-6): ")
        )

        if order < 1 or order > 6:
            raise ValueError

    except ValueError:

        print("Invalid order. Using order 4.")

        order = 4

    visualizer = HilbertVisualizer(order)

    visualizer.show()