import flet
from flet import *

def main(page):
    dict_values = {
        'nome' : '',
        'nascimento' : '',
        'sexo' : '',
        'doencas' : '',
        'cirurgias_recentes' : '',
        'tipo_sangue' : '',
        'doacao' : '',
        'cpf' : '',
        'obs':'',
    }

    def gera_cadastro(e):
        dict_values['nome'] = nome.controls[1].value
        dict_values['nascimento'] = nascimento.controls[1].value
        dict_values['sexo'] = sexo.controls[1].value
        dict_values['doencas'] = doencas.controls[1].value
        dict_values['cirurgias_recentes'] = cirurgia_recentes.controls[1].value
        dict_values['tipo_sangue'] = tipo_sangue.controls[1].value
        dict_values['doacao'] = doacao.controls[1].value
        dict_values['cpf'] = cpf.controls[1].value
        dict_values['obs'] = obs.controls[1].value
        dict_values['aceita_termo'] = aceita_termo.value

        for val in dict_values.values():
            if not val:
                page.banner.open = True
                page.update()
                return
            
        print('É possível cadastrar o usuário.\n')
        print(dict_values)

    def fecha_banner(e):
        page.banner.open = False
        page.update()

    page.banner = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(
            icons.DANGEROUS_SHARP,
            color=colors.RED_400,
            size=40
        ),
        content=Text('Todos os campos devem ser preenchidos.', color=colors.BLACK87, weight='bold'),
        actions=[
            TextButton(
                'Entendi',
                on_click=fecha_banner
            )
        ]
    )
    
    page.title = 'Cadastro de paciente'
    page.theme_mode = ThemeMode.LIGHT
    
    titulo = Row(
        controls=[
            Icon(icons.PERSON,color=colors.BLACK),
            Text(value='Cadastro de usuário no banco de dados.', size=25, weight='bold')])

    nome = Row(
        controls=[
            Icon(icons.PERSON_ADD_ALT_1, color=colors.BLUE_500),
            TextField(label='Preencha com o nome completo.', autofocus=True)])

    nascimento = Row(
        controls=[
            Icon(icons.CALENDAR_MONTH_OUTLINED, color=colors.BLUE_100),
            TextField(label='Preencha a data de nascimento.')
        ]
    )
    
    sexo = Row(
        controls=[
            Icon(icons.TRANSGENDER_ROUNDED, color=colors.BLUE),       
            Dropdown(
                label="Informe o sexo.",
                hint_text="Sexo",
                options=[
                    flet.dropdown.Option("Feminino"),
                    flet.dropdown.Option("Masculino"),
                    flet.dropdown.Option("Prefiro não informar"),
        ])])

    doencas = Row(
        controls=[
            Icon(icons.HEALTH_AND_SAFETY_OUTLINED, color=colors.DEEP_PURPLE),
            TextField(label='O paciente possui alguma doença? Se sim, informe abaixo')
        ])
          
    cirurgia_recentes = Row(
        controls=[
            Icon(icons.LOCAL_HOSPITAL_ROUNDED, color=colors.RED),
            Dropdown(
                label='Realizou cirurgia nos últimos 6 meses?',
                hint_text='Informe Sim ou Não',
                options=[
                    flet.dropdown.Option("Sim"),
                    flet.dropdown.Option("Não")
        ]  ) ] )

    tipo_sangue = Row(
        controls=[
            Icon(icons.MONITOR_HEART,color=colors.GREEN),     
            Dropdown(
                label='Informe o tipo sanguíneo.',
                hint_text='Tipo sanguíneo',
                options=[
                    flet.dropdown.Option("A+"),
                    flet.dropdown.Option("A-"),
                    flet.dropdown.Option("B+"),
                    flet.dropdown.Option("B-"),
                    flet.dropdown.Option("AB+"),
                    flet.dropdown.Option("AB-"),
                    flet.dropdown.Option("O+"),
                    flet.dropdown.Option("O-")
        ])]) 
    
    doacao = Row(
        controls=[
            Icon(icons.BLOODTYPE_OUTLINED, color=colors.RED),
            Dropdown(
                label='Já doou sangue antes?',
                hint_text='Informe Sim ou Não',
                options=[
                    flet.dropdown.Option("Sim"),
                    flet.dropdown.Option("Não")
        ])])
    
    cpf = Row(
        controls=[
            Icon(icons.NUMBERS_OUTLINED),    
            TextField(label='Preencha o CPF do paciente')])
        
    obs =Row(
        controls=[
        Icon(icons.EDIT_NOTE, color=colors.BLACK),
        TextField(label='Alguma observação?')])
    
    aceita_termo = Checkbox(label="Aceito o termo de compromisso.")

    botao_cadastro = FilledButton(text='Cadastrar Paciente', on_click=gera_cadastro)


    page.add(
        Row(
            controls=[
                titulo
            ]
        ),
        Row(
            controls=[
                nome
            ]
        ),
        Row(
            controls=[
                nascimento,
            ]
        ),
        Row(
            controls=[
                sexo,
            ]
        ),
        Row(
            controls=[
                doencas,
            ]
        ),
        Row(
            controls=[
                cirurgia_recentes,
            ]
        ),
        Row(
            controls=[
                tipo_sangue,
            ]
        ), 
        Row(
            controls=[
                doacao,
            ]
        ),
        Row(
            controls=[
                cpf,
            ]
        ), 
        Row(
            controls=[
                obs,
            ]
        ),
        Row(
            controls=[
                aceita_termo,
            ]
        ),
        Row(
            controls=[
                botao_cadastro,
            ]
        )
    )

flet.app(target=main)
