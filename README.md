# pyqt-math-game
Basic math problem solving game made out of PyQt5

## Detailed Description

![image](https://user-images.githubusercontent.com/55078043/164683116-75f2dada-233f-42a8-ad62-dbc234f9b7f4.png)

This app generates a lot of different math problems with its AI. 

Math problem is pretty basic(plus and minus only).

User can solve this problem with writing the answer in LINEEDIT and press return(enter) key or click SUBMIT button.

If submitted answer is right, right message will pop up, if it is wrong, wrong message will pop up.

If problem is so hard to solve than user can change the problem with clicking TRY OTHER.

Took about 40 minutes to make this.

## Requirements
* PyQt5 >= 5.15

## Setup
`pip3 install git+https://github.com/yjg30737/pyqt-math-game.git --upgrade`

## Example
Code Sample
```python
from pyqt_math_game import MathGameApp

if __name__ == "__main__":
    import sys

    app = MathGameApp(sys.argv)
    app.exec_()
```
