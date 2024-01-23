from django import forms

class loginForms(forms.Form):
    nomeLogin = forms.CharField(
        label='Nome do usuário', 
        required= True, 
        max_length=100, 
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu usuario"
                }
            ))
    senhaLogin = forms.CharField(
        label='Senha do usuário', 
        required= True, 
        max_length=100, 
        widget= forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Digite sua senha"
             }
        ))
    
class cadastroForms(forms.Form):
    nomeCadastro = forms.CharField(
        label='Nome de Cadastro', 
        required= True, 
        max_length=100, 
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu usuario"
                }
            ))
    emailCadastro = forms.EmailField(
        label='Email de cadastro', 
        required= True, 
        max_length=100,
        widget= forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Digite seu email"
                }
        )
    )
    senhaCadastro = forms.CharField(
        label='Senha do usuário', 
        required= True, 
        max_length=100, 
        widget= forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Digite sua senha"
             }
        ))
    senhaCadastroConfirma = forms.CharField(
        label='Confirme sua senha', 
        required= True, 
        max_length=100, 
        widget= forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Confirme sua senha"
             }
        ))
    

    def clean_nomeCadastro(self):
        nome = self.cleaned_data.get("nomeCadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não pode haver espaços no Usuário")
            else:
                return nome
            




    def clean_senhaCadastroConfirma(self):
        senhaCadastro = self.cleaned_data.get("senhaCadastro")
        senhaCadastroConfirma = self.cleaned_data.get("senhaCadastroConfirma")

        if senhaCadastro and senhaCadastroConfirma:
                if senhaCadastro != senhaCadastroConfirma:
                    raise forms.ValidationError(" Senhas não são iguais")
                else:
                    return senhaCadastroConfirma