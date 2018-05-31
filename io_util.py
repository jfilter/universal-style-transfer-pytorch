from PIL import Image

from torchvision.utils import make_grid


def save_image(tensor, filename):
    grid = make_grid(tensor, padding=0)
    ndarr = grid.mul(255).clamp(0, 255).byte().permute(1, 2, 0).cpu().numpy()
    im = Image.fromarray(ndarr)
    im.save(filename, format == 'JPEG', quality=90, subsampling=0)
