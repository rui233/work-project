# Predict the name of the drink on the picture by using the inference 

import cv2 as cv 
import torch
import matplotlib.pyplot as plt
from torchvision import transforms
from torch.autograd import Variable




img = cv.imread('./capture/0.jpg',cv.IMREAD_COLOR)

def inference():
    device = torch.device("cuda")
    print(device)
    ToPIL = transforms.ToPILImage()
    img0 = ToPIL(img)
    Reshape = transforms.Resize(256)
    Crop = transforms.CenterCrop(224)
    img1 = Reshape(img0)
    img2 = Crop(img1)
    Tensor = transforms.ToTensor()
    img_tensor = Tensor(img2)
    print(img_tensor.shape)
    fixed_tensor = Variable(torch.unsqueeze(img_tensor,dim = 0).float(),requires_grad = False).cuda()
    print(fixed_tensor.shape)
    print(fixed_tensor)
    Model = torch.load('./model/finefuned_resnet18_model.pkl')
    Model.to(device)
    Model.eval()
    with torch.no_grad():
        
        output = Model(fixed_tensor) 
        _, preds = torch.max(output, 1)
    print(output)
    print(preds)


if __name__ == '__main__':
    inference()