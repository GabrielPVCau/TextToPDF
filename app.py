from fpdf import FPDF

# Função para converter TXT em PDF
def txt_to_pdf(txt_path, pdf_path):
    # Criação de um objeto PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Abre o arquivo TXT e lê linha por linha
    with open(txt_path, 'r') as file:
        for line in file:
            # Remove espaços em branco da linha
            line = line.replace(" ", "")
            # Adiciona a linha ao PDF
            pdf.cell(200, 10, txt=line, ln=True)

    # Salva o PDF
    pdf.output(pdf_path)

# Exemplo de uso
txt_to_pdf("example.txt", "output.pdf")
