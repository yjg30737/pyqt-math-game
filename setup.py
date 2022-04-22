from setuptools import setup, find_packages

setup(
    name='pyqt-math-game',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_math_game.ico': ['math.svg']},
    description='Basic math problem solving game made out of PyQt5',
    url='https://github.com/yjg30737/pyqt-math-game.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-style-setter @ git+https://git@github.com/yjg30737/pyqt-style-setter.git@main',
        'pyqt-custom-titlebar-setter @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-setter.git@main',
        'pyqt-toast @ git+https://git@github.com/yjg30737/pyqt-toast.git@main',
        'pymeg @ git+https://git@github.com/yjg30737/pymeg.git@main',
        'pyqt-responsive-label @ git+https://git@github.com/yjg30737/pyqt-responsive-label.git@main',
        'pyqt-rounded-corners-lineedit @ git+https://git@github.com/yjg30737/pyqt-rounded-corners-lineedit.git@main'
    ]
)