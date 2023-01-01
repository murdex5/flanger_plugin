FlangerDialog
A graphical user interface (GUI) for applying a flanger effect to an audio file.

Properties
depth_slider (QSlider): A horizontal slider for adjusting the depth of the flanger effect (0.0 - 1.0).
rate_slider (QSlider): A horizontal slider for adjusting the rate of the flanger effect (0.0 - 1.0).
delay_slider (QSlider): A horizontal slider for adjusting the base delay time of the flanger effect (in seconds).
Methods
apply_flanger(): Applies the flanger effect to the input audio file using the parameters specified by the sliders.
Usage
To use the FlangerDialog, create an instance of the class and call the show() method to display the GUI. The flanger effect can be applied by adjusting the sliders and clicking the "Apply Flanger" button. The resulting audio will be saved to the file "output.wav".

Here is an example of how to use the FlangerDialog:

``` 
import sys
from PyQt5.QtWidgets import QApplication

from flanger_dialog import FlangerDialog

app = QApplication(sys.argv)
dialog = FlangerDialog()
dialog.show()
sys.exit(app.exec_())
``` 