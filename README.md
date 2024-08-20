
---

# Object Detection Algorithm

## Description

This project is a color-based object detection algorithm. It uses a custom algorithm to detect objects based on their color in an image or video stream. The implementation focuses on detecting objects within a specified color range and can be customized for various applications such as tracking objects, filtering images, or enhancing visual processing systems.

## Installation

### Prerequisites

To run this project, you'll need the following:

- Python 3.x
- `opencv-python`
- `numpy`

You can install these dependencies using pip:

```bash
pip install opencv-python numpy
```

### Clone the Repository

```bash
git clone https://github.com/leon4113/object-detection-algorithm.git
cd object-detection-algorithm
```

## Usage

After setting up the environment, you can run the object detection script:

### Running the Detection

1. **Using `main.py`:** This is the main entry point for the project. It processes the input images or video streams to detect objects based on the specified color ranges.

   ```bash
   python main.py --input <path_to_image_or_video> --output <output_path> --color <color_range>
   ```

   Example:

   ```bash
   python main.py --input sample_image.jpg --output detected_output.jpg --color "lower_color_bound,upper_color_bound"
   ```

2. **Fine-Tuning HSV Ranges (`HSV_finetuning.py`):** This script helps fine-tune the HSV color ranges used in object detection. It allows you to interactively adjust the HSV values to get the best detection results.

   ```bash
   python HSV_finetuning.py --input <path_to_image_or_video>
   ```

   Example:

   ```bash
   python HSV_finetuning.py --input sample_image.jpg
   ```

### Arguments

- `--input`: Path to the input image or video file.
- `--output`: Path to save the output with detected objects.
- `--color`: The color range for detection, specified as "lower_bound,upper_bound" in HSV format.

### Customization

You can customize the detection algorithm by modifying the HSV range values in the script to detect different colors.

## Dependencies

- Python 3.x
- OpenCV
- NumPy

Ensure you have these installed in your environment.

## Contributors

- **Leon4113** (GitHub: [leon4113](https://github.com/leon4113))

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

