import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class E4E:
    """
    chapter : the chapter number for which you are generating figures
    base_dir : the directory (folder) under which chapter subfolders and figures will be written
    """
    def __init__(self, chapter, base_dir="./"):
        assert os.path.exists(base_dir), f"Directory {base_dir} does not exists"
        self.chapter = chapter
        mpl.rcParams["figure.dpi"] = 300
        if isinstance(chapter, str):
            self.fig_dir = f"{base_dir}/Appendix {chapter}/"
        else:
            self.fig_dir = f"{base_dir}/Chapter {chapter}/"
        self.color_1 = "#444444"
        self.color_2 = "#777777"
        self.color_3 = "#AAAAAA"
        self.color_4 = "#DDDDDD"
        self.colors = [self.color_1, self.color_2, self.color_3, self.color_4]
        self.alpha_err = 0.333
        self.arrow_props = {
            "width": 1,
            "color": self.color_1,
            "headwidth": 5,
            "headlength": 7,
        }
        self.font_size_2d = 7

        os.makedirs(self.fig_dir, exist_ok=True)

    def save_fig_named(self, name):
        plt.tight_layout()
        for ext in ["svg",  "eps", "png"]:
            try:
                fmt = f"{self.chapter:02d}"
            except Exception:
                fmt = self.chapter
            plt.savefig(f"{self.fig_dir}/CH{fmt}_{name}_sweet.{ext}", transparent=True)

    def save_fig(self, fig_num):
        self.save_fig_named(f"F{fig_num:02d}")

    def aspect_square(self, ax):
        c = ax.axis()
        ax.set_aspect((c[1] - c[0]) / (c[3] - c[2]))

    def horizontal_line(self, y_0, clr=None):
        if clr is None:
            clr = self.color_3
        c = plt.axis()
        plt.autoscale(False)
        plt.plot([c[0], c[1]], [y_0, y_0], "--", linewidth=1, color=clr)

    def vertical_line(self, x_0, clr=None, ax=plt):
        if clr is None:
            clr = self.color_3
        c = ax.axis()
        ax.autoscale(False)
        ax.plot([x_0, x_0], [c[2], c[3]], "--", linewidth=1, color=clr)

    def err_plot(self, y_mean, y_se, x=None, color=None, ax=plt):
        if x is None:
            x = np.arange(len(y_mean))
        if color is None:
            color = self.color_2
        ax.fill_between(
            x,
            y_mean - 2 * y_se,
            y_mean + 2 * y_se,
            color=color,
            alpha=self.alpha_err,
            linewidth=1,
        )
