import PyPDF2
import io
from drf_extra_fields.fields import Base64ImageField, Base64FileField
from PIL import Image

class PDFBase64File(Base64FileField):
    ALLOWED_TYPES = ["pdf", "png", "jpg", "jpeg"]

    def get_file_extension(self, filename, decoded_file):
        try:
            PyPDF2.PdfReader(io.BytesIO(decoded_file))
            return "pdf"
        except Exception:
            pass

        try:
            image = Image.open(io.BytesIO(decoded_file))
            format = image.format.lower()
            print(f"Arquivo reconhecido como imagem: {format}")
            if format in self.ALLOWED_TYPES:
                return format
        except Exception:
            print("Erro ao identificar arquivo")

        raise ValueError("Formato de arquivo não suportado.")