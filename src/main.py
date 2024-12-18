import os
import json
import random
import matplotlib.pyplot as plt
import cv2
from pycocotools.coco import COCO

# Caminhos para imagens e anotações
ANNOTATION_FILE = './data/annotations/instances_val2017.json'
IMAGE_DIR = './data/val2017/'

# Inicializa o COCO API
coco = COCO(ANNOTATION_FILE)

# Seleciona uma categoria
category_names = coco.loadCats(coco.getCatIds())
category_name = 'person'  # Exemplo: detectando pessoas
category_id = coco.getCatIds(catNms=[category_name])[0]

# Carrega imagens que contêm a categoria selecionada
image_ids = coco.getImgIds(catIds=[category_id])
random_image_id = random.choice(image_ids)

# Carrega a imagem e suas anotações
image_info = coco.loadImgs([random_image_id])[0]
image_path = os.path.join(IMAGE_DIR, image_info['file_name'])
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Carrega anotações (bounding boxes)
annotations = coco.loadAnns(coco.getAnnIds(imgIds=[random_image_id], catIds=[category_id]))

# Desenha as bounding boxes
for ann in annotations:
    x, y, width, height = ann['bbox']
    cv2.rectangle(image, (int(x), int(y)), (int(x+width), int(y+height)), (0, 255, 0), 2)
    plt.text(x, y, category_name, color='red', fontsize=12)

# Exibe a imagem
plt.imshow(image)
plt.axis('off')
plt.title(f"Categoria: {category_name}")
plt.show()
