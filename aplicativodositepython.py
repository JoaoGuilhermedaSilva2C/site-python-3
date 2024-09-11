import flet as ft

# Feito por João Guilherme da Silva Rodrigues Inácio 2º C

def main(page: ft.Page):
    page.title = "Aplicativo para Criptografar/Descriptografar Conteúdo (Cifra de César)"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    file_path = ft.TextField(label="Caminho do Arquivo", width=300)
    shift_input = ft.TextField(label="Chave (Valor da Rotação)", value="3", width=100)
    output_label = ft.Text(value="", color=ft.colors.GREEN)

    def caesar_cipher(text, shift, decrypt=False):
        if decrypt:
            shift = -shift
        result = ""
        for char in text:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            else:
                result += char
        return result

    def validate_input():
        if not file_path.value.strip():
            return "Por favor, forneça o caminho do arquivo."
        try:
            shift_value = int(shift_input.value)
            return None  # Sem erros
        except ValueError:
            return "A chave deve ser um número inteiro válido."

    def encrypt_file(e):
        error_message = validate_input()
        if error_message:
            output_label.value = error_message
            page.update()
            return
        
        try:
            shift_value = int(shift_input.value)
            with open(file_path.value, 'r') as file:
                file_data = file.read()
                encrypted_data = caesar_cipher(file_data, shift_value)
            
            with open(file_path.value, 'w') as file:
                file.write(encrypted_data)
            
            output_label.value = "Conteúdo criptografado com sucesso!"
        except FileNotFoundError:
            output_label.value = "Arquivo não encontrado. Verifique o caminho."
        except Exception as ex:
            output_label.value = f"Erro ao criptografar: {str(ex)}"
        page.update()

    def decrypt_file(e):
        error_message = validate_input()
        if error_message:
            output_label.value = error_message
            page.update()
            return
        
        try:
            shift_value = int(shift_input.value)
            with open(file_path.value, 'r') as file:
                encrypted_data = file.read()
                decrypted_data = caesar_cipher(encrypted_data, shift_value, decrypt=True)
            
            with open(file_path.value, 'w') as file:
                file.write(decrypted_data)
            
            output_label.value = "Conteúdo descriptografado com sucesso!"
        except FileNotFoundError:
            output_label.value = "Arquivo não encontrado. Verifique o caminho."
        except Exception as ex:
            output_label.value = f"Erro ao descriptografar: {str(ex)}"
        page.update()

    page.add(
        ft.Column(
            [
                file_path,
                shift_input,
                ft.Row(
                    [
                        ft.ElevatedButton("Criptografar", on_click=encrypt_file),
                        ft.ElevatedButton("Descriptografar", on_click=decrypt_file),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                output_label,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)