import pyautogui

# Coordonnées du pixel à surveiller
x_pixel = 1161
y_pixel = 393

# Couleur à surveiller (format RGB)
couleur_attendue = (75, 219, 106)

# Fonction pour vérifier la couleur du pixel
def verifier_couleur_pixel(x, y, couleur_attendue):
    couleur_pixel = pyautogui.pixel(x, y)
    return couleur_pixel == couleur_attendue

# Variable pour garder trace de si le clic a été effectué
clic_effectue = False

# Boucle principale
while not clic_effectue:
    if verifier_couleur_pixel(x_pixel, y_pixel, couleur_attendue):
        # Si la couleur du pixel correspond à la couleur attendue, effectuer un clic gauche
        pyautogui.click()
        print("Clic gauche effectué.")
        # Mettre à jour la variable pour indiquer que le clic a été effectué
        clic_effectue = True
