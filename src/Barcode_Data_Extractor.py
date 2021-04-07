from pyzxing import BarCodeReader
import json
import cv2
import numpy as np


class BCR:
    def __init__(self):
        pass

    def decode_file(self, file):
        response = file.read()
        # frame = cv2.imdecode(response)
        frame = cv2.imdecode(np.fromstring(
            response, np.uint8), cv2.IMREAD_COLOR)

        # print("frame ", frame)

        return self.decode_array(frame)

    def decode_array(self, img):
        reader = BarCodeReader()
        results = reader.decode_array(img)

        print("results ", results)

        if 'raw' in results[0]:
            result_string = results[0]['raw'].decode("utf-8")
            # print(result_string.split('\n'))

            barcode_data_split = [s.strip() for s in result_string.split('\n')]
            # print(barcode_data_split)

            barcode_dict = {}

            with open("LicenseCodes.json") as f:
                codes = json.load(f)
                # print(codes['DAB']['val'])
                barcode_dict = {codes[s[:3]]['val']: s[3:]
                                for s in barcode_data_split if s[:3] in codes}

            # print(barcode_dict)

            # print(json.dumps(barcode_dict, indent=4, sort_keys=False))

            return json.dumps(barcode_dict, indent=4, sort_keys=False)
        else:
            return "Could not detect barcode"


if __name__ == "__main__":

    reader = BarCodeReader()
    results = reader.decode("2D-Gen-Back-DL-01.png")
    # Or file pattern for multiple files
    # results = reader.decode('/PATH/TO/FILES/*.png')
    # print(results[0]['raw'].decode("utf-8"))

    # Or a numpy array
    # Requires additional installation of opencv
    # pip install opencv-python
    # results = reader.decode_array(img)

    result_string = results[0]['raw'].decode("utf-8")
    # print(result_string.split('\n'))

    barcode_data_split = [s.strip() for s in result_string.split('\n')]
    print(barcode_data_split)

    barcode_dict = {}

    with open("LicenseCodes.json") as f:
        codes = json.load(f)
        # print(codes['DAB']['val'])
        barcode_dict = {codes[s[:3]]['val']: s[3:]
                        for s in barcode_data_split if s[:3] in codes}

    # print(barcode_dict)
    print(json.dumps(barcode_dict, indent=4, sort_keys=False))

    print("main")
