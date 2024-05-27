import LabelingGUI
import numpy as np

from SpecularHighlightData import SpecularHightlightDatum, PointLabel
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":

    images = (np.random.rand(1000, 7, 7) * 255).astype(np.uint8)

    data_points = [
        SpecularHightlightDatum(images[i], i, PointLabel.UNLABELED)
        for i in range(images.shape[0])
    ]

    viewer_app = QApplication(["Specular Highlight Labeling"])
    viewer = LabelingGUI.MainWindow(None)
    viewer.show()

    # Launch the Qt application
    viewer_app.exec()
