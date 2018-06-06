## Universal Style Transfer

This is an improved verion of the PyTorch implementation of [Universal Style Transfer via Feature Transforms](https://arxiv.org/pdf/1705.08086.pdf).

You can find the original PyTorch implemention [here](https://github.com/sunshineatnoon/PytorchWCT).

The official Torch implementation can be found [here](https://github.com/Yijunmaverick/UniversalStyleTransfer) and Tensorflow implementation can be found [here](https://github.com/eridgd/WCT-TF).

## Changes

- Use Pipenv (`pip install pipenv && pipenv install`)
- Simplify I/O (e.g. remove padding)
- Only use JPEG
- Update to PyTorch v0.4.0
- Added a script to download the models

There is still a lot work left. Feel free to fork or send PRs.

## Prepare images

Put content and image pairs in `images/content` and `images/style` respectively. Note that correspoding content image and style image should have same names.

## Usage

```
pipenv run python WCT.py --cuda
```

## Acknowledgments

Build upon the work of Deepthi Venkatesh.

## License

MIT.
