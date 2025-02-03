import PyPDF2
import io
from drf_extra_fields.fields import Base64ImageField, Base64FileField


class PDFBase64File(Base64FileField):
    ALLOWED_TYPES = ['pdf']

    def get_file_extension(self, filename, decoded_file):
        try:
            PyPDF2.PdfReader(io.BytesIO(decoded_file))
        except PyPDF2.utils.PdfReadError as e:
            print(e)
        else:
            return 'pdf'