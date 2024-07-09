import mss
from pynput.mouse import Button, Controller

# Initialisation du contrôleur de souris
mouse = Controller()

# Coordonnées du pixel à surveiller (à adapter selon votre écran)
x_pixel = 1161
y_pixel = 393

# Couleur à surveiller (format RGB)
couleur_attendue = (75, 219, 106)

# Taille de la zone de capture autour du pixel
zone_capture = 1

# Fonction pour vérifier la couleur du pixel
def verifier_couleur_pixel(capture, x, y, couleur_attendue):
    pixel = capture.pixel(x, y)
    return pixel == couleur_attendue

# Déterminer les coordonnées de la région à capturer
x_capture = max(0, x_pixel - zone_capture)
y_capture = max(0, y_pixel - zone_capture)
largeur_capture = min(x_pixel + zone_capture, 1920) - x_capture  # Ajuster la largeur selon votre résolution d'écran
hauteur_capture = min(y_pixel + zone_capture, 1080) - y_capture  # Ajuster la hauteur selon votre résolution d'écran

# Boucle principale
while True:
    with mss.mss() as sct:
        monitor = {"left": x_capture, "top": y_capture, "width": largeur_capture, "height": hauteur_capture}
        capture = sct.grab(monitor)
        
        # Vérifier la couleur du pixel
        if verifier_couleur_pixel(capture, x_pixel - x_capture, y_pixel - y_capture, couleur_attendue):
            # Effectuer un clic de souris
            mouse.position = (x_pixel, y_pixel)
            mouse.click(Button.left)
            print("Clic gauche effectué.")
            break
