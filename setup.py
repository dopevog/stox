from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='stox',
    packages=['stox'],
    version='0.3',
    description='Stock Price Prediction And Analysis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Vedant Kothari',
    author_email='stox.org@gmail.com',
    url='https://github.com/cstox/stox',
    keywords=['stock price prediction','stock analysis','stock signals''stock ai'],
    classifiers=['Programming Language :: Python :: 3',
                 'Natural Language :: English',
                 'Topic :: Utilities'],
    install_requires=['numpy==1.19.5','pandas-datareader','pytrends','pandas','requests','scikit-learn','keras','tensorflow','matplotlib','pandas-ta',]
)
