import os
from odoo import models, fields
import logging
import qrcode
import base64
import os

_logger = logging.getLogger(__name__)
#_logger.error("Erreur loggée depuis ma_methode")
#try:
#    import qrcode
#    # Autres imports si nécessaire
#    QR_CODE_AVAILABLE = True
#except ImportError:
#    QR_CODE_AVAILABLE = False


#_logger.info("Information loggée depuis ma_methode")


class qrcode_module(models.Model):
    #_logger.warning("Erreur loggée depuis ma_methode")
    _name = 'qrcode_module.qrcode_module'  # Clé unique pour Odoo
    _description = 'Description de Mon Modele'

    nom = fields.Char('Nom', required=True)
    description = fields.Text('https://', required=True)

    # Champ binaire pour l'image
    image_champ = fields.Binary("Image QR Code")

    def generer_qrcode(self):
        chemin_dossier_images = os.path.abspath(os.path.join(os.path.dirname(__file__), '../images/'))
        _logger.warning(chemin_dossier_images)
        nom_fichier = self.nom + ".png"
        chemin_complet = chemin_dossier_images + '/' + nom_fichier

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data("https://" + self.description)  # ou toute autre donnée que vous voulez dans le QR Code
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(chemin_complet)

        # Lire l'image et la convertir en données binaires
        with open(chemin_complet, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

            # Stocker l'image encodée dans le champ binaire
        self.image_champ = encoded_string
        _logger.warning(chemin_complet)
        os.remove(chemin_complet)
        return chemin_complet