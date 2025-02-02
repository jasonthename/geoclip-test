# GeoCLIP Test
# <p align="center">🌎 GeoCLIP: Clip-Inspired Alignment between Locations and Images for Effective Worldwide Geo-localization</p>

A simple Python Flask file upload web app that uses GeoCLIP to predict the location where the image was taken.

# Setup

Install GeoCLIP via pip

```pip install geoclip```

# Usage

```python app.py```

1. Navigate to http://localhost:5000
2. Upload your image and predict the location

Acknowledgments
The GeoCLIP project incorporates code from Joshua M. Long's Random Fourier Features Pytorch. For the original source, visit [here](https://github.com/jmclong/random-fourier-features-pytorch).

# Citation

```
@inproceedings{geoclip,
  title={GeoCLIP: Clip-Inspired Alignment between Locations and Images for Effective Worldwide Geo-localization},
  author={Vivanco, Vicente and Nayak, Gaurav Kumar and Shah, Mubarak},
  booktitle={Advances in Neural Information Processing Systems},
  year={2023}
}
```
