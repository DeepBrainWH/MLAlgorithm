# 基于直方图均衡化的图像增强
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "./data/9.jpg"
# 直方图均衡化增强图像
def hist():
    image1 = cv2.imread(image_path)
    image_channel = cv2.split(image1)
    for i in range(3):
        # plt.hist(image_channel[i].ravel(), 256, [0, 256])
        # plt.show()
        cv2.equalizeHist(image_channel[i], image_channel[i])

    cv2.merge(image_channel, image1)
    return image1

# 拉普拉斯算法增强
def laplus():
    image1 = cv2.imread(image_path)
    kernel = np.array([[0,-1,0],
                       [-1,7,-1],
                       [0,-1,0]])
    dist= cv2.filter2D(image1, cv2.CV_8UC3, kernel)
    return dist

# 对数变换增强图像
def log_image():
    image1 = cv2.imread(image_path)
    image_log = np.uint8(15*np.log(np.array(image1)+1))
    cv2.normalize(image_log, image_log, 0, 255, cv2.NORM_MINMAX)
    cv2.convertScaleAbs(image_log, image_log)
    return image_log

# gamma变换图像增强
def gamma():
    image = cv2.imread(image_path)
    fgamma = 2.5
    image_gamma = np.uint8(np.power((np.array(image) / 255.0), fgamma) * 255.0)
    cv2.normalize(image_gamma, image_gamma, 0, 255, cv2.NORM_MINMAX)
    cv2.convertScaleAbs(image_gamma, image_gamma)
    return image_gamma

if __name__ == '__main__':
    # image = cv2.imread("./data/6.jpg")
    # shape = image.shape
    # height = shape[1] // 2
    # width = shape[0] // 2
    # image = cv2.resize(image, (height, width))
    # cv2.imwrite("data/7.jpg", image)
    # result = hist()
    cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
    result = log_image()
    cv2.imshow("image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
    # original_image = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
    # image = laplus()
    # image = hist()
    # image = log_image()
    # image = gamma()
    # cv2.imshow("original_image", original_image)
    # cv2.imshow("image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()