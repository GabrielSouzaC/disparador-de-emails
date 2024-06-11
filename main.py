import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# config do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'seu@gmail.com'
application_password = 'chave de acesso do gmail'

# destinatários com dados personalizados
destinatarios = [
    {'email': 'destinatário1@gmail.com', 'nome': 'destinatário1'},
    {'email': 'destinatário2@outook.com', 'nome': 'destinatário2'},
    {'email': 'destinatário3@hotmail.com', 'nome': 'destinatário3'}
]

# conexão com o servidor SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # TLS ativo para segurança
server.login(username, application_password)

# loop para enviar e-mails personalizados
for contato in destinatarios:
    # conteúdo do e-mail
    corpo_email = f"Olá {contato['nome']},\n\n...mensagem..."
    assunto = f"Olá, {contato['nome']}! assunto do e-mail"

    # criação do e-mail
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = contato['email']
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo_email, 'plain'))

    # enviar o e-mail
    server.sendmail(username, contato['email'], msg.as_string())

# fechando a conexão SMTP
server.quit()
