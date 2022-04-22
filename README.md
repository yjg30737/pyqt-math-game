# pyqt-math-game
Basic math problem solving game made out of PyQt5

## Detailed Description

![image](https://user-images.githubusercontent.com/55078043/164683116-75f2dada-233f-42a8-ad62-dbc234f9b7f4.png)

This app generates a lot of different math problems with its AI(by pymeg, check "Included Packages" below). 

Math problem is pretty basic(plus and minus only).

User can solve this problem with writing the answer in line edit and press return(enter) key or click submit button.

If submitted answer is right, right message will pop up, if it is wrong, wrong message will pop up.

Took about 40 minutes to make this.

## Requirements
* PyQt5 >= 5.15

## Setup
`pip3 install git+https://github.com/yjg30737/pyqt-math-game.git --upgrade`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-style-setter.git">pyqt-style-setter</a> - for its dark-gray style
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-setter">pyqt-custom-titlebar-setter</a> - for its customized title bar (not OS default title bar)
* <a href="https://github.com/yjg30737/pyqt-toast.git">pyqt-toast</a> - for show the right/wrong message
* <a href="https://github.com/yjg30737/pymeg.git">pymeg</a> - for generate the random math problem
* <a href="https://github.com/yjg30737/pyqt-responsive-label.git">pyqt-responsive-label</a> - for responsive label accordance with window size 
* <a href="https://github.com/yjg30737/pyqt-rounded-corners-lineedit.git">pyqt-rounded-corners-lineedit</a> - self-explanatory, stylish rounded corners line edit

## Example
Code Sample
```python
from pyqt_math_game import MathGameApp

if __name__ == "__main__":
    import sys

    app = MathGameApp(sys.argv)
    app.exec_()
```
