"""
    interfaces.py
    Autor: Iago Magalhães
    Descrição:
        - entender o conceito de interfaces através de exemplos
"""

# No exemplo a seguir, você terá a perspectiva de um engenheiro de dados que precisa extrair
# texto de vários tipos diferentes de arquivos não estruturados, como PDFs e e-mails. Você
# criará uma interface informal que define os métodos que estarão nas classes PdfParsere
# EmlParserconcretas:

class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass

# InformalParserInterfacedefine os dois métodos .load_data_source()e .extract_text().
# Esses métodos são definidos, mas não implementados. A implementação ocorrerá assim
# que você criar classes concretas que herdam de InformalParserInterface.