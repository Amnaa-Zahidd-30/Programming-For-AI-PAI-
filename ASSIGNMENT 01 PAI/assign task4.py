class Image:
    def __init__(self, pixeldata):
        self.pixeldata = pixeldata

    def applytransformation(self, transformationfunction):
        self.pixeldata = transformationfunction(self.pixeldata)

    def getcopy(self):
        pixels = [row[:] for row in self.pixeldata]
        return Image(pixels)

def fliphorizontal(pixeldata):
    newdata = [row[::-1] for row in pixeldata]
    return newdata

def adjustbrightness(pixeldata, brightnessvalue):
    newdata = [[value + brightnessvalue for value in row] for row in pixeldata]
    return newdata

def rotate90degrees(pixeldata):
    rotated = [[row[i] for row in pixeldata[::-1]] for i in range(len(pixeldata[0]))]
    return rotated

class AugmentationPipeline:
    def __init__(self):
        self.steps = []  

    def addstep(self, transformfunction):
        self.steps.append(transformfunction)

    def processimage(self, originalimage):
        augmentedimages = []
        for transform in self.steps:
            copyimage = originalimage.getcopy() 
            copyimage.applytransformation(transform)
            augmentedimages.append(copyimage.pixeldata)
        return augmentedimages
    
originalPixels = [
    [10, 20, 30],
    [40, 50, 60]
]
img = Image(originalPixels)

pipeline = AugmentationPipeline()
pipeline.addstep(fliphorizontal)
pipeline.addstep(lambda pixels: adjustbrightness(pixels, 10))
pipeline.addstep(rotate90degrees)
augmentedresults = pipeline.processimage(img)

print("Original Image:", originalPixels)
print("Augmented Images:")

for i in range(len(augmentedresults)):
    print("Result", i + 1, ":", augmentedresults[i])
